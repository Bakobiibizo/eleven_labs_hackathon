FROM python:3.10

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install -r requirements.txt
RUN apt update && apt install ffmpeg -y

COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]