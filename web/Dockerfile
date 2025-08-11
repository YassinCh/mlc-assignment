FROM node:21.7.1-alpine3.19

# Create a directory for the app and set its ownership to the 'node' user
RUN mkdir -p /home/node/app/node_modules && chown -R node:node /home/node/app

# Switch to a non-root user, the 'node' user is provided by the node image
USER node

# Set the working directory to the home directory of node
WORKDIR /home/node/app

# Copy package.json and package-lock.json to the working directory
COPY --chown=node:node ./package*.json ./

# Configure npm to disable progress messages and install dependencies
RUN npm config set progress=false && npm install

# Copy the rest of the application files to the working directory
COPY --chown=node:node . .

# Expose the default port on which the server runs
EXPOSE 5173

# Run a development server by default
CMD ["npm", "run", "dev", "--", "--host"]
