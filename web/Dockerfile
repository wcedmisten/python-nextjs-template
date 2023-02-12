FROM node:hydrogen-bullseye

WORKDIR /frontend

COPY frontend/package.json /frontend/package.json

RUN npm install

COPY frontend/ /frontend/

RUN npm run export

FROM nginx:alpine

WORKDIR /root/
COPY --from=0 /frontend/out /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
COPY mime.types /etc/nginx/mime.types
