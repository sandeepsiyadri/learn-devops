# CMD vs ENTRYPOINT
In Docker, both CMD and ENTRYPOINT  instructions used to specify what command should be run when a container starts. However, they have different purposes and behaviors.

### CMD

- The CMD instruction sets the default command to be executed when the container starts.
- CMD can be overridden at runtime by passing arguments to docker run after specifying the image name.
- If the Dockerfile contains multiple CMD instructions, only the last one will take effect.

### ENTRYPOINT

- The ENTRYPOINT instruction sets the primary command that should be executed when the container starts.
- It's used to provide a fixed command that cannot be overridden at runtime.
- Arguments passed to docker run will be appended to the entrypoint command.

 
## Example 1

Let's create a real-world example using a Python application that accepts command-line arguments. 

- We'll create a simple Python script that greets a user with a custom message.

```python
# greet.py
import sys

def greet(name):
    print(f"Hello, {name}!\nWelcome to DevOps learning.\nAuthor - Sandeep Siyadri")

if __name__ == "__main__":
    args = sys.argv[1:]
    if args:
        greet(args[0])
    else:
        greet("There")
```

This script accepts a name as a command-line argument and greets the user with "Hello, {name}!..." If no argument is provided, it defaults to greeting "There".

- Dockerfile to containerize this application.

```Dockerfile
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
```
- Notice the default greeting in the *greet.py* script is set to *"There"* whereas the default CMD in the Dockerfile is defined as *"World"*. So when we run the container without any argument, *${name}* will print *"World"* otherwise print the *argument* whatever passed during the runtime.

- Let's build the image.

```
ubuntu@ip-172-31-29-224:~/python-example$ docker build -t greeting-app .
Sending build context to Docker daemon  3.072kB
Step 1/5 : FROM python:3.9-slim
3.9-slim: Pulling from library/python
8a1e25ce7c4f: Pull complete 
1103112ebfc4: Pull complete 
6e52db3290c0: Pull complete 
937bce5dbc70: Pull complete 
05e63546fee1: Pull complete 
Digest: sha256:df78d66895cd3b12ec57c451f9776192a535688e27ab8a72c03896b17dbb4b98
Status: Downloaded newer image for python:3.9-slim
 ---> 500c1b793e9d
Step 2/5 : WORKDIR /app
 ---> Running in 8bed47b0c853
Removing intermediate container 8bed47b0c853
 ---> f20db9f7794e
Step 3/5 : COPY greet.py .
 ---> 45b887dd3385
Step 4/5 : ENTRYPOINT ["python", "greet.py"]
 ---> Running in 4652b100a38a
Removing intermediate container 4652b100a38a
 ---> 86be353eaa0e
Step 5/5 : CMD ["World"]
 ---> Running in c1c50da087cf
Removing intermediate container c1c50da087cf
 ---> dbf8d7d594bf
Successfully built dbf8d7d594bf
Successfully tagged greeting-app:latest

ubuntu@ip-172-31-29-224:~/python-example$ docker images
REPOSITORY          TAG        IMAGE ID       CREATED          SIZE
greeting-app        latest     dbf8d7d594bf   5 seconds ago    126MB
```

- Run the container *without* specifying user argument.

```
ubuntu@ip-172-31-29-224:~/python-example$ docker run greeting-app
Hello, World!
Welcome to the Docker Learning.
Presenter: Sandeep Siyadri
```

- Run the container specifying user argument.

```
ubuntu@ip-172-31-29-224:~/python-example$ docker run greeting-app Shiva
Hello, Shiva!
Welcome to the Docker Learning.
Presenter: Sandeep Siyadri
```
## Note

- In a Dockerfile, only the **last CMD instruction** will take effect. So there is no practical use case to define multiple CMD instructions within the same Dockerfile.
- This behavior ensures clarity and avoids confusion about the container's default behavior.

## Let's Explore more about CMD and ENTRYPOINT

Let's understand the usage of double quotes in the **CMD** instruction.

```
CMD ["echo", "Hello World!"]
```
This CMD instruction sets a command with two arguments - "echo" and "Hello World!" .

```
CMD ["echo Hello World!"]
```

This passes a single argument: "echo Hello World!"

Alternatively, we can use without quotes.

```
CMD echo Hello World!
```

But this is **not recommended** because the shell might interpret spaces as delimiter between separate arguments and could lead to unexpected behaviour if the command includes spaces.

#### Let's understand practically with the below example -

### Example 2

Consider the below Dockerfile 

```Dockerfile
# Dockerfile-cmd
FROM alpine
ENTRYPOINT ["/bin/sh", "-c"]
CMD ["echo", "Hello World!"]
```
- Build and run

```
ubuntu@ip-172-31-29-224:~/example2$ docker build -t cmd-vs-entrypoint -f Dockerfile-cmd .
Sending build context to Docker daemon  2.048kB
Step 1/3 : FROM alpine
 ---> 05455a08881e
Step 2/3 : ENTRYPOINT ["/bin/sh", "-c"]
 ---> Using cache
 ---> 2b6cf36a0669
Step 3/3 : CMD ["echo", "Hello World!"]
 ---> Using cache
 ---> abeab2342f9c
Successfully built abeab2342f9c
Successfully tagged cmd-vs-entrypoint:latest


ubuntu@ip-172-31-29-224:~/example2$ docker images
REPOSITORY          TAG        IMAGE ID       CREATED             SIZE
cmd-vs-entrypoint   latest     abeab2342f9c   58 minutes ago      7.38MB


ubuntu@ip-172-31-29-224:~/example2$ docker run cmd-vs-entrypoint

ubuntu@ip-172-31-29-224:~/example2$
```

- Docker run prints nothing.
- Let's update the CMD instruction as below -

```Dockerfile
# Dockerfile-cmd2
FROM alpine
ENTRYPOINT ["/bin/sh", "-c"]
CMD ["echo Hello World!"]
```
- Build and run the container

```
ubuntu@ip-172-31-29-224:~/example2$ docker build -t cmd-vs-entrypoint2 -f Dockerfile-cmd2 .

ubuntu@ip-172-31-29-224:~/example2$ docker run cmd-vs-entrypoint2
Hello World!
```

- Now the docker run prints *Hello World!*. 

### Understand the difference:

#### CMD ["echo", "Hello World!"]
- Passes two separate arguments to the ENTRYPOINT: "echo" and "Hello World!".
- Results in the command ```/bin/sh -c echo Hello World!```, which prints *nothing*.
- In this case, the shell interprets each argument separately. ```/bin/sh -c echo``` executes a new shell instance without any commands to print, hence no output.
- ```Hello World!``` is then parsed as a command to the new shell, but it's not a valid command, so nothing happens.

#### CMD ["echo Hello World!"]
- Passes a single argument, "echo Hello World!", to the ENTRYPOINT.
- Retains the spaces as intended, effectively executing as ```/bin/sh -c "echo Hello World!"```, correctly printing *"Hello World!"*.


### Note
- There's no ENTRYPOINT will be defined in the Dockerfile always. 
- It is not that we need to use single set of double quotes in the CMD always. 

### Which is the better approach?

```
CMD ["echo", "$MESSAGE", "to", "$FILENAME"] 
                VS
CMD ["echo $MESSAGE to $FILENAME"]
                VS 
CMD echo $MESSAGE to $FILENAME
```

 - The most suitable approach depends on your specific requirements and the context of your Dockerfile.

##### CMD ["echo", "$MESSAGE", "to", "$FILENAME"]:

- This option uses an **array** to specify the command and its arguments. 
- Each argument is treated as a separate string, and variables like $MESSAGE and $FILENAME won't be expanded by the shell. Instead, they will be passed as literal strings to the echo command. 
- This means that if you want to use environment variables as part of the command, you need to ensure they are set and available at runtime within the container.

##### CMD ["echo $MESSAGE to $FILENAME"]:

- In this option, the entire command, including variable references, is specified as a ***single string*** within the array. 
- However, within the array, variables won't be expanded by the shell, so $MESSAGE and $FILENAME will be **treated as literal strings**. 
- This approach is not suitable if you intend to use environment variables directly in the command.

##### CMD echo $MESSAGE to $FILENAME:

- This option specifies the command without using an array. It relies on the default shell (/bin/sh) to interpret the command line, allowing variable expansion. 
- This approach is convenient if you want to use environment variables directly in the command and have them expanded by the shell.
