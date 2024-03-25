# Base Image
FROM python:3.9-slim

LABEL maintainer="Sandeep Siyadri"

# Setup the project working directory 
WORKDIR /app

# Copy files from outside to the docker image
COPY greet.py .

# Using ENTRYPOINT to set the primary command. Executed at the runtime and cannot be overridden. 
ENTRYPOINT ["python", "greet.py"]

# Using CMD to provide default arguments. This can be overridden during the run time. This is passed as argument for the Entrypoint. 
CMD ["World"]