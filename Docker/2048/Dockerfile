# Stage 1: Building the application
FROM ubuntu:22.04 as builder

RUN apt-get update \
    && apt-get install -y zip curl \
    && curl -o /2048.zip -L https://codeload.github.com/jabir000/2048/zip/master \
    && unzip /2048.zip -d / \
    && mv /2048-master /2048

# Stage 2: Setting up the Nginx server
FROM nginx:stable-alpine

# Copy only the built application from the builder stage
COPY --from=builder /2048 /usr/share/nginx/html

# Optional: if you need to customize the Nginx configuration
# COPY your-custom-nginx.conf /etc/nginx/nginx.conf

# For Nginx, the daemon is already set to off in the base image
EXPOSE 80

# The CMD is already set to start Nginx in the base image, so no need to repeat it
# CMD ["nginx", "-g", "daemon off;"]