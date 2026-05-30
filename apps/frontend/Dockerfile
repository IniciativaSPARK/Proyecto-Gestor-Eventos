# Stage 1: Build
FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Stage 2: Serve (SSR Runtime)
FROM node:20-alpine
WORKDIR /app
COPY --from=build /app/dist/frontend /app/dist/frontend
COPY package*.json ./
RUN npm install --omit=dev

EXPOSE 4000
CMD ["node", "dist/frontend/server/main.js"]