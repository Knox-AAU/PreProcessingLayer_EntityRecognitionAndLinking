FROM python:3.9
EXPOSE 3000
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip install --no-cache-dir --upgrade -r models.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]
