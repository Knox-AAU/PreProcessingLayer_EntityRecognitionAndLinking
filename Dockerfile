FROM ubuntu:latest
WORKDIR /app
RUN apt-get update -y && apt-get install python3-pip build-essential -y
COPY . .
RUN pip install -U pip setuptools wheel
RUN pip install -U spacy
RUN pip install --extra-index-url https://repos.knox.cs.aau.dk da_core_news_cstm

CMD ["python3", "./main.py"]
