# Creating a New Repository on GitHub and Cloning it Locally

Here's how to create a new repository on GitHub and clone it locally:

#### On GitHub:

- **Navigate to your Github.** Select "Repositories" and click "New repository".

- **Choose a name and description.** Provide a clear and descriptive name for your repository. Optionally, you can add a brief description of the project's purpose.

- **Set visibility.** Decide whether you want your repository to be public (visible to everyone) or private (only accessible to you and authorized collaborators).

- **Initialize with README (optional).** You can choose to include a README file which serves as a project introduction.

- **Create repository.** Click "Create repository" to finalize the process.

Refer this [link](https://scribehow.com/shared/Create_GitHub_repository__bSsp-mXbRymThx1dJHXXHw) with images to create new repo using above steps.

## Cloning the Repository Locally:

- **Open your terminal.** Launch your terminal application (Command Prompt on Windows or Terminal on macOS/Linux).

- **Navigate to your desired directory.** Use the cd command to navigate to the location where you want to store your local copy of the repository.

- **Copy the clone URL.** On the GitHub webpage for your newly created repository, navigate to the "Code" section and copy the HTTPS clone URL under the "clone with HTTPS" option.

- **Clone the repository.**  In your terminal, use the git clone command followed by the copied URL. For example:

```bash
sande@DESKTOP-RCQ4124 MINGW64 ~/OneDrive/Documents/Learning
$ git clone https://github.com/sandeepsiyadri/learn-git.git
Cloning into 'learn-git'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.

sande@DESKTOP-RCQ4124 MINGW64 ~/OneDrive/Documents/Learning
$ ls -lrth
drwxr-xr-x 1 sande 197609   0 Mar 24 20:46 learn-git/

sande@DESKTOP-RCQ4124 MINGW64 ~/OneDrive/Documents/Learning
$ cd learn-git/

sande@DESKTOP-RCQ4124 MINGW64 ~/OneDrive/Documents/Learning/learn-git (main)
$ ls -lrth
total 1.0K
-rw-r--r-- 1 sande 197609 75 Mar 24 20:46 README.md
```

- **Verify the clone.** The git clone command will download the repository files to your specified directory. Once complete, you can navigate into the newly created folder using cd to confirm the files are present.

That's it! You've successfully created a new repository on GitHub and cloned it locally to your machine.# Creating a New Repository on GitHub and Cloning it Locally

Here's how to create a new repository on GitHub and clone it locally:

#### On GitHub:

- **Navigate to your Github.** Select "Repositories" and click "New repository".

- **Choose a name and description.** Provide a clear and descriptive name for your repository. Optionally, you can add a brief description of the project's purpose.

- **Set visibility.** Decide whether you want your repository to be public (visible to everyone) or private (only accessible to you and authorized collaborators).

- **Initialize with README (optional).** You can choose to include a README file which serves as a project introduction.

- **Create repository.** Click "Create repository" to finalize the process.

Refer this [link](https://scribehow.com/shared/Create_GitHub_repository__bSsp-mXbRymThx1dJHXXHw) with images to create new repo using above steps.

## Cloning the Repository Locally:

- **Open your terminal.** Launch your terminal application (Command Prompt on Windows or Terminal on macOS/Linux). Download and install [git bash](https://git-scm.com/downloads). 

- **Navigate to your desired directory.** Use the cd command to navigate to the location where you want to store your local copy of the repository.

- **Copy the clone URL.** On the GitHub webpage for your newly created repository, navigate to the "Code" section and copy the HTTPS clone URL under the "clone with HTTPS" option.

- **Clone the repository.**  In your terminal, use the git clone command followed by the copied URL. For example:

```bash
sande@DESKTOP-RCQ4124 MINGW64 ~/OneDrive/Documents/Learning
$ git clone https://github.com/sandeepsiyadri/learn-git.git
Cloning into 'learn-git'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.

sande@DESKTOP-RCQ4124 MINGW64 ~/OneDrive/Documents/Learning
$ ls -lrth
drwxr-xr-x 1 sande 197609   0 Mar 24 20:46 learn-git/

sande@DESKTOP-RCQ4124 MINGW64 ~/OneDrive/Documents/Learning
$ cd learn-git/

sande@DESKTOP-RCQ4124 MINGW64 ~/OneDrive/Documents/Learning/learn-git (main)
$ ls -lrth
total 1.0K
-rw-r--r-- 1 sande 197609 75 Mar 24 20:46 README.md
```

- **Verify the clone.** The git clone command will download the repository files to your specified directory. Once complete, you can navigate into the newly created folder using cd to confirm the files are present.

That's it! You've successfully created a new repository on GitHub and cloned it locally to your machine.