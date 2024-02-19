FROM node:20.11.1-alpine3.19

WORKDIR /app

COPY src/.  .

RUN npm i .

EXPOSE 4000

CMD ["node", "index.js"]
