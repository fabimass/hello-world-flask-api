FROM python:3

# Create directory in container image for app code
RUN mkdir -p /usr/src/app

# Copy app code to /usr/src/app in container image
COPY . /usr/src/app

# Set working directory context
WORKDIR /usr/src/app

# Install dependencies
RUN pip install -r requirements.txt

# Command for container to execute
ENTRYPOINT [ "python", "app.py" ]