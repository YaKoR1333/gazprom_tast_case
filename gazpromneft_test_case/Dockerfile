FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/application_app

COPY ./req.txt /usr/src/req.txt
RUN pip install --upgrade pip
RUN pip install -r /usr/src/req.txt

COPY . /usr/src/application_app

#CMD ["python", "manage.py", "migrate"]