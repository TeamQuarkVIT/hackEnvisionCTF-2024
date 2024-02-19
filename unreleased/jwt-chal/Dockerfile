FROM node:20.11.1-alpine3.19
    
# Setup app
RUN mkdir -p /app

# Add application
WORKDIR /app
COPY src/package.json .

# Install dependencies
RUN npm i

COPY src/. .

# Expose the port node-js is reachable on
EXPOSE 5000

# Start the node-js application
CMD ["npm", "start"]

