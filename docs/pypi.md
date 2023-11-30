# Pypi Repository

For the purpose of our pipeline, we have created a pip repository which is hosted in a docker container on the _knox-web01.srv.aau.dk_ server. It runs off of [pypiserver](https://github.com/pypiserver/pypiserver).

As of writing this, a ticket has been send to ITS to create a domain name for the server at the internal domain [http://pypi.knox.cs.aau.dk](http://pypi.knox.cs.aau.dk). Internal meaning it is only accessible when at Campus or through VPN.

## Compose File Location

The _compose.yml_ file is located in _/srv/data/pip-repo/_ in the _knox-web01.srv.aau.dk_ server.

## Uploading

Uploading can be done using [twine](https://github.com/pypa/twine). If the server is not yet setup to the domain [http://pypi.knox.cs.aau.dk](http://pypi.knox.cs.aau.dk), it should still be running on the web01 server. Because of this, here are two ways to upload to the pip repository:

### By SSH

First you need to SSH into the server using the following command:

```BASH
ssh USERNAME@student.aau.dk@knox-web01.srv.aau.dk -L 8081:localhost:8081
```

The above command SSH's you into the server and forwards the port 8081 on the server into your local machine. You should now be able to go to <http://localhost:8081/simple> in your browser and see the repository.

To upload using twine, run the following command:

```BASH
twine upload -r http://localhost:8081 --sign PACKAGENAME.whl
```

Uploading requires no authentication as the repository is only available when on campus anyways.

### By Domain (if domain is up)

When the domain is eventually up, the following twine command is also applicable

```BASH
twine upload -r http://pypi.knox.cs.aau.dk --sign PACKAGENAME.whl
```

## Installing through the repository

To install packages from the repository you simply use pip.
Again because we at this state don't know when the domain will be available, two methods are possible.

You can either connect to the web01 server with the command:

```BASH
ssh USERNAME@student.aau.dk@knox-web01.srv.aau.dk -L 8081:localhost:8081
```

And afterwards in another terminal run the pip command:

```BASH
pip3 install --index-url http://localhost:8081/simple PACKAGE-NAME
```

If the domain is available simply replace the localhost:8081 with the domain:

```BASH
pip3 install --index-url http://pypi.knox.cs.aau.dk/simle PACKAGE-NAME
```

## Creating a whl package from Spacy

If you have trained a model, you can use spacy to create a whl package for the repository.

This is done with the command

```BASH
spacy package MODEL-FOLDER OUTPUT-LOCATION --name package-name --build wheel
```

Example command:

```BASH
spacy package trainedmodel/updated_da_model model_packages --name core_news_knox_lg --build wheel
```

Note that we have left out the "da" before core in the --name, this is added by default through the meta.json file in the model.
