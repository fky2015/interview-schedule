FROM python:3
RUN mkdir -p /usr/src/app
RUN mkdir -p /usr/src/web_frond_end/admin/dist
WORKDIR /usr/src/app
COPY schedule_backend /usr/src/app
COPY web_front_end /usr/src/web_front_end

# Use sed because of potential file owner issue

RUN apt-get update && \
    apt-get install -y nginx supervisor && \
    rm -rf /var/lib/apt/lists/* && \
    pip install -r requirements.txt --no-cache-dir && \
    rm -rf /var/lib/apt/lists/* && \
    echo "daemon off;" >> /etc/nginx/nginx.conf && \
    python manage.py collectstatic --noinput
ENV DJANGO_PRODUCTION=1

COPY ./schedule_backend/media /usr/share/nginx/html

COPY schedule_backend/deploy/nginx-app.conf /etc/nginx/sites-available/default
COPY schedule_backend/deploy/supervisor-app.conf /etc/supervisor/conf.d/
EXPOSE 80
ENTRYPOINT [ "/bin/bash", "deploy/entrypoint.sh" ]
CMD ["supervisord", "-n"]
