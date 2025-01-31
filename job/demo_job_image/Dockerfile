# Dockerfile

FROM python:3.9

WORKDIR /app

COPY process_data.py .

RUN pip install pandas google-cloud-storage

CMD ["python", "process_data.py"]

