FROM python:3.10.0

WORKDIR /home/

RUN echo "change"

RUN git clone https://github.com/Bokdol11859/django_pinterest.git

WORKDIR /home/django_pinterest

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD [ "bash", "-c",  "python manage.py collectstatic --noinput --settings=pragmatic.settings.deploy && python manage.py migrate --settings=pragmatic.settings.deploy && gunicorn pragmatic.wsgi --env DJANGO_SETTINGS_MODULE=pragmatic.settings.deploy --bind 0.0.0.0:8000"]