# Set the base image 
FROM node:14-alpine 

# set maintainer
LABEL maintainer="mehrdad"
LABEL description="Dockerfile for a Node.js application, created for the first Jenkins project."
# Add metadata labels
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="My Node.js Application" \
      org.label-schema.description="A simple Node.js web application" \
      org.label-schema.url="https://example.com/app" \
      org.label-schema.vcs-url="https://github.com/myusername/my-app.git" \
      org.label-schema.vendor="My Organization" \
      org.label-schema.version="1.0.0" \
      org.label-schema.schema-version="1.0"
      
# Create and set the working directory
WORKDIR /app 

# Copy the package.json and package-lock.json files and install dependencies
COPY package*.json ./
RUN npm install --production

# Copy the rest of the application files
COPY main.js ./main/
COPY test.js ./test/

# Tell Docker what port to expose
EXPOSE 8000 

# Add a health check to ensure the container is running properly
HEALTHCHECK --interval=30s --timeout=5s \
CMD wget -qO- http://localhost:8000/healthcheck \
  | grep -q "Healthy" || (sleep 5 && wget -qO- http://localhost:8000/healthcheck \
  | grep -q "Healthy") || (sleep 5 && wget -qO- http://localhost:8000/healthcheck \
  | grep -q "Healthy") || exit 1
  
# Use multi-stage builds to reduce the size of the final image
FROM node:14-alpine
WORKDIR /app
COPY --chown=node:node --from=0 /app .
CMD ["npm", "start"]
