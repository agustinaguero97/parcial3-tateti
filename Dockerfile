FROM python:3

RUN https://github.com/agustinaguero97/parcial3-tateti.git
WORKDIR /parcial3-tateti

RUN pip install -r requirements.txt

CMD ["python", "./test_tateti.py"]
