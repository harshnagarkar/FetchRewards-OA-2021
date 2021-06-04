FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
RUN apk --update add bash curl
# ENV STATIC_URL /static
# ENV STATIC_PATH /var/www/app/static
COPY ./ /app
WORKDIR /app
# COPY ./requirements.txt /var/www/requirements.txt
# COPY uwsgi.ini /etc/uwsgi/
RUN pip install -r requirements.txt
EXPOSE 5000
EXPOSE 80
# CMD [ "python3","main.py" ] 