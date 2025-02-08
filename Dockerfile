FROM node:14

# Set the working directory in the container
WORKDIR /app

# Copy local files to the container
COPY . .

# Install dependencies
RUN npm install

# Expose the port the app runs on
EXPOSE 3000

# Define the command to run the app
CMD ["npm", "start"]
