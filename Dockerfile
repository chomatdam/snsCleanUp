FROM python:3

ADD . /app

RUN pip install --trusted-host pypi.python.org -r ./app/requirements.txt

CMD [ "python", "./app/scripts/cleanUpSNS.py" ]