FROM node:18.16-alpine
WORKDIR /frontend
RUN yarn install
COPY . /frontend
RUN yarn build
EXPOSE 8080
CMD yarn serve

