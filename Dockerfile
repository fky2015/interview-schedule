FROM python:3
RUN mkdir -p /usr/src/app
# RUN mkdir -p /usr/src/web_frond_end/admin/dist
WORKDIR /usr/src/app
COPY schedule_backend/requirements.txt /usr/src/app/
# Use sed because of potential file owner issue

RUN apt-get update && \
    apt-get install -y nginx supervisor && \
    rm -rf /var/lib/apt/lists/* && \
    pip install -r requirements.txt --no-cache-dir && \
    echo "daemon off;" >> /etc/nginx/nginx.conf
ENV DJANGO_PRODUCTION=1

COPY web_front_end /usr/src/web_front_end


# RUN mkdir -p /usr/share/nginx/html/media
COPY schedule_backend/media /usr/share/nginx/html/media

COPY schedule_backend/deploy/nginx-app.conf /etc/nginx/sites-available/default
COPY schedule_backend/deploy/supervisor-app.conf /etc/supervisor/conf.d/
COPY schedule_backend /usr/src/app
RUN python manage.py collectstatic --noinput

EXPOSE 80
ENTRYPOINT [ "/bin/bash", "deploy/entrypoint.sh" ]
CMD ["supervisord", "-n"]
