# Stage 1: Build the React application
FROM node:16-alpine AS build

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json to install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the React app for production
RUN npm run build

# Stage 2: Run the Express server and serve the React app
FROM node:16-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy only the server code and React build from the build stage
COPY --from=build /app/dist ./dist
COPY --from=build /app/src/server ./src/server
COPY --from=build /app/node_modules ./node_modules
COPY --from=build /app/package*.json ./

# Expose the port for the Express server
EXPOSE 3000

# Command to start the Express server
CMD ["node", "dist/server.js"]
