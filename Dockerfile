# build
FROM node:11.12.0-alpine as build-vue
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY ./frontend/frontend/package*.json ./
RUN npm install
COPY ./frontend/frontend .
ARG build_type
RUN npm run $build_type

# production
FROM nginx:stable-alpine as production
ENV APP_NAME=FlaskApp
ENV DB_USER=b994f4285d5410
ENV DB_PASSWORD=0b190067
ENV DB_HOST=us-cdbr-east-02.cleardb.com
ENV DB_PORT=3306
ENV DB_NAME=heroku_8a93ca0fef811b1
WORKDIR /app
RUN apk update && apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache
COPY --from=build-vue /app/dist /usr/share/nginx/html
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
COPY ./server/requirements.txt ./
RUN pip install -r requirements.txt
RUN pip install gunicorn
COPY ./server .
CMD gunicorn -b 0.0.0.0:5000 app:app --daemon && \
      sed -i -e 's/$PORT/'"$PORT"'/g' /etc/nginx/conf.d/default.conf && \
      nginx -g 'daemon off;'
