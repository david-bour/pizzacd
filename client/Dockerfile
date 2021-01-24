FROM node:latest AS base

FROM base AS build
RUN wget https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64.deb && dpkg -i dumb-init_*.deb
ENTRYPOINT ["dumb-init"]

RUN apt-get update \
    && apt-get autoclean \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

ENV CLIENT_USER node
ENV CLIENT_HOME /home/$CLIENT_USER
ENV ANGULAR_DIR $CLIENT_HOME/client

ENV PATH $ANGULAR_DIR/node_modules/.bin:$PATH

WORKDIR $ANGULAR_DIR

COPY --chown=$CLIENT_USER:$CLIENT_USER package.json .
COPY --chown=$CLIENT_USER:$CLIENT_USER yarn.lock .
RUN yarn install \
    && chown -R $CLIENT_USER:$CLIENT_USER node_modules

COPY . $ANGULAR_DIR

FROM build as compile
# ========================================
# angular bundle compilation
# ========================================
ENV CLIENT_USER node
ENV CLIENT_HOME /home/$CLIENT_USER
ENV ANGULAR_DIR $CLIENT_HOME/client
ENV PATH $ANGULAR_DIR/node_modules/.bin:$PATH
WORKDIR $ANGULAR_DIR
COPY --from=build /home/node/client .
RUN yarn build --configuration="production" --output-path=dist

# ========================================
# nginx
# ========================================
# Set the nginx conf file to use
FROM nginx:latest AS webserver
RUN mkdir -p /home/node/client/dist
RUN mkdir -p /home/node/client/landing/dist
COPY --from=compile /home/node/client/dist /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY --from=build "/home/node/client/nginx/nginx.conf" /etc/nginx/conf.d/default.conf

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]