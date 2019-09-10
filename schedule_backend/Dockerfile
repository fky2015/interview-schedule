FROM python:3
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app

# Use sed because of potential file owner issue
ENV DJANGO_PRODUCTION=1
RUN apt-get update && \
    apt-get install -y nginx supervisor && \
    rm -rf /var/lib/apt/lists/* && \
    pip install -r requirements.txt --no-cache-dir && \
    rm -rf /var/lib/apt/lists/* && \
    echo "daemon off;" >> /etc/nginx/nginx.conf && \
    python manage.py collectstatic --noinput

COPY deploy/nginx-app.conf /etc/nginx/sites-available/default
COPY deploy/supervisor-app.conf /etc/supervisor/conf.d/
EXPOSE 80
ENTRYPOINT [ "/bin/bash", "deploy/entrypoint.sh" ]
CMD ["supervisord", "-n"]
