FROM node:20-alpine
WORKDIR /app
COPY package.json package-lock.json* ./
RUN npm install --include=dev webpack webpack-cli
COPY . .
EXPOSE 3000
CMD ["npx", "webpack", "serve"]
