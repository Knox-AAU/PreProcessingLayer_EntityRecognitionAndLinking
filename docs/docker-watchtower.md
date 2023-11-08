# Using Docker and Watchtower

The Entity Recognition and Linking layer uses Docker and Watchtower to automate and effectively run the layer on the KNOX server.

Here you can find a short explaination of the Dockerfile that is present in the repository and an explaination of how Watchtower works and is setup.

## Dockerfile

The Dockerfile is setup to use `Python3.9`.

It exposes the port 3000 outside the docker container.

```docker
RUN pip install --no-cache-dir --upgrade -r requirements.txt
```

> Installs the appropriate requirements that is present in the requirements.txt file.
> {.is-info}

<br><br>

```docker
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]
```

> Runs the `uvicorn` server on the public ip of the docker container using port `3000`.
> {.is-info}

## Watchtower

Using watchtower, we are able to always keep the docker image on the KNOX server up-to-date. This is done by having the Watchtower container running on the KNOX server.

> Watchtower works by looking at the running containers of the server and checking the repositories for a newer version tag of containers.
> {.is-info}

As we are using GHCR to house our docker containers, for watchtower to know a new version is available, we need to upload the new container each time a new version is ready. This can fortunately be automated using github actions.

### GitHub Actions and Tags

Inside the repository under Actions, a workflow can be found called Docker Publish. The workflow is a yml file, and it looks like the following:

```yml
# This workflow will install Python dependencies, run tests and lint with a single version of Python
# For more information see: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python

name: Docker Publish

on:
  schedule:
    - cron: "15 23 * * *"
  push:
    # "trigger" for the building and publishing will be tags in the format of e.g. '1.0.1'.
    tags: ["*.*.*"]
  pull_request:
    branches: [main]
  workflow_dispatch:

env:
  # Use the GitHub Container Repository
  REGISTRY: ghcr.io
  # github.repository as <account>/<repo>
  IMAGE_NAME: ${{ github.repository }}

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write

    steps:
      - uses: actions/checkout@v3
      - name: Log into registry ${{ env.REGISTRY }}
        if: github.event_name != 'pull_request'
        uses: docker/login-action@28218f9b04b4f3f62068d7b6ce6ca5b26e35336c
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - name: Extract Docker metadata
        id: meta
        uses: docker/metadata-action@98669ae865ea3cffbcbaa878cf57c20bbf1c6c38
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
      - name: Build and push Docker image
        uses: docker/build-push-action@ad44023a93711e3deb337508980b4b5e9bcdc5dc
        with:
          #The root folder of the project
          context: ./
          # The Dockerfile
          file: ./Dockerfile
          push: ${{ github.event_name != 'pull_request' }}
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
```

What this action does, is simply every time a new tag is created in the repository using the format `X.X.X` e.g. `1.0.1`, a new container is build from using the Dockerfile and it is then pushed to the GitHub Container Repository.

To create a new tag, use the following commands in the terminal while cd'd into the repository:

```bash
git tag *TAG* main
git push origin *TAG*
```

Here is an example of a new version tag being made for version 1.0.1:

```bash
git tag 1.0.1 main
git push origin 1.0.1
```

After using those commands, version 1.0.1 will be created and the Action file will see this and create a new container with this tag for watchtower to see when it eventually updates.

### Running the docker container

For watchtower to work, you need to correctly run the docker container for the Entity Recognition and Linking layer. This is done by running the container directly through the GitHub Container Repository.
This is done using the following command:

```docker
docker run -d -p 3000:3000 ghcr.io/knox-aau/preprocessinglayer_entityrecognitionandlinking:latest
```

> The command above, pulls the latest image from ghcr.io and runs the container daemonized with the port 3000 being forwarded to the server.

### If watchtower has stopped

If watchtower has stopped, it can be started again using the following command:

```bash
docker run -d \
--interval 1800 \
--name watchtower \
-v /var/run/docker.sock:/var/run/docker.sock \
containrrr/watchtower
```

> The above command runs watchtower and polls for new images every 1800 seconds (30 min). This can be changed to your liking.
>
> Further more, you can add --trace to run it more verbose and see more details.

You can see the logs of watchtower using the following command:

```bash
docker logs watchtower
```
