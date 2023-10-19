# Getting Started

A guide for setting up and getting started with the Entity Recognition and Linker part of the pipeline.

## Setting up

This subsection will guide you through both setting up to work on the repository, and how to get it all running on the server!

### Development

> #### **Requirements**
>
> - Python3
> - Uvicorn
> - FastAPI
> - SpaCy
> - Wheel
> - Setuptools
>
> <br>

<br>

To get started developing on the code for this part of the pipeline, simply clone the repository to where you want using

```BASH
git clone https://github.com/Knox-AAU/PreProcessingLayer_EntityRecognitionAndLinking ERAL
cd ERAL
```

After cloning the repository, you need to install the requirements. Make sure you have `python3` and `pip` installed for this. You can install all the requirements using the following command:

```BASH
pip install -r requirements.txt
```

#### Running local

To run Entity Recognizer and Linker, we use `Uvicorn`. Uvicorn works like node for `python3`. Simply run the following command to start the server:

```BASH
uvicorn main:app
```

### Running on the server

The server uses Docker and watchtower to maintain the up to date code on the github repository you can read more on this [here](LINK TO DOCS ON WATCHTOWER).

Inside the Dockerfile in the repository, we have the following CMD specified for running the server:

```DOCKER
CMD ["uvicorn", "main:app", "--host", "0.0.0.0". "--port", "3000"]
```

This CMD starts the `uvicorn` server but also adds the parameters **host** and **port**. This ensures that instead of the server running locally inside the Docker Container, it is ran using the public IP. That way, we are able to find the `uvicorn` server inside the KNOX server.

## Accessing Locally through SSH

It is possible to get access to the `uvicorn` server running the Entity Recognition and Linking layer locally using SSH. This is done by forwarding the port the server is running on using the SSH. If the `uvicorn` server is ran on port `3000`, you can access the server locally by doing the following SSH command:

```BASH
ssh *USERNAME@student.aau.dk*@knox-preproc01.srv.aau.dk -L 3000:localhost:3000
```

This forwards what is running on port `3000` on the KNOX server to your local machine. You should now be able to access the `uvicorn` server from your own browser at
[http://localhost:3000](http://localhost:3000).
