FROM node:current-buster-slim

WORKDIR /app

COPY src/. /app

RUN npm install
EXPOSE 4000

CMD ["node", "index.js"]
