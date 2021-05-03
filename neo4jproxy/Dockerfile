FROM nginx:latest AS webserver
RUN apt-get update && apt-get install -y --no-install-recommends \
    htop tcpdump net-tools
RUN rm /etc/nginx/conf.d/default.conf
RUN rm /etc/nginx/nginx.conf
COPY ./default.conf /etc/nginx/conf.d/default.conf
COPY ./nginx.conf /etc/nginx/nginx.conf
CMD ["nginx", "-g", "daemon off; "]