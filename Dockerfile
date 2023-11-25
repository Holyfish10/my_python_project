FROM python:3.12.0-slim
LABEL authors="erik"

WORKDIR /usr/app/src

RUN pip install requests python-dotenv

COPY . .

CMD ["python", "-u","/usr/app/src/main.py"]