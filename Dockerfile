FROM node:16-alpine

WORKDIR /app

# Copy package.json first
COPY package.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application
COPY . .

# Expose port 8080
EXPOSE 8080

# Command to run the server
CMD ["npm", "start"]