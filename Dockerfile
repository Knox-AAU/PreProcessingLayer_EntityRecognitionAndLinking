FROM ubuntu:latest
WORKDIR /app
RUN apt-get update -y && apt-get install python3-pip build-essential -y
COPY . .
RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app"]
