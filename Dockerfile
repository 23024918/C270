FROM node:14

# Set the working directory in the container
WORKDIR /app

# Clone the repository
RUN git clone https://github.com/23024918/C270.git .

# Install dependencies
RUN npm install

# Expose the port the app runs on
EXPOSE 3000

# Define the command to run the app
CMD ["npm", "start"]
