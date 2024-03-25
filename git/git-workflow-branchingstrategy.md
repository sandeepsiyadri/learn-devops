# Git Workflow - Branching Strategies

The Git workflow refers to the sequence of steps and practices that developers follow when using Git for version control. While there are various Git workflows, centralized workflow is the basic workflow and here's an explanation:

- #### Initialize Repository:
First, developers [initialize](create-new-repository-clone.md) a Git repository either by creating a new one or by cloning an existing repository from a remote source (like GitHub or GitLab).


- #### Work on Files: 
Developers work on files within the repository, making changes, adding new features, fixing bugs, etc.

- #### Stage Changes: 
Once the changes are made, developers stage the changes they want to commit. Staging allows developers to select which changes they want to include in the next commit.

```git add <file1> <file2> ...```

```
sande@DESKTOP-RCQ41I3 MINGW64 ~/OneDrive/Documents/Learning/learn-git (main)
$ git checkout -b feature-developer1-changes
Switched to a new branch 'feature-developer1-changes'

sande@DESKTOP-RCQ41I3 MINGW64 ~/OneDrive/Documents/Learning/learn-git (feature-developer1-changes)
$ ls -lrth
total 6.0K
-rw-r--r-- 1 sande 197609  75 Mar 24 20:46 README.md
-rw-r--r-- 1 sande 197609 257 Mar 24 21:13 greet.py
-rw-r--r-- 1 sande 197609 485 Mar 24 21:18 Dockerfile

sande@DESKTOP-RCQ41I3 MINGW64 ~/OneDrive/Documents/Learning/learn-git (feature-developer1-changes)
$ git add greet.py Dockerfile 
```


- #### Commit Changes: 
After staging changes, developers commit them to the repository along with a descriptive commit message. Commits create a snapshot of the repository at that point in time.

```git commit -m "Descriptive commit message"```

```
$ git commit -m "added greet script and Dockerfile to create image"
[feature-developer1-changes 778ef11] added greet script and Dockerfile to create image
 2 files changed, 28 insertions(+)
 create mode 100644 Dockerfile
 create mode 100644 greet.py
```


- #### Push Changes: 
Once the changes are committed locally, developers push them to a remote repository. This makes the changes accessible to other developers working on the project.

```git push origin <branch_name>```

```
$ git push origin feature-developer1-changes
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 823 bytes | 823.00 KiB/s, done.
Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
remote: 
remote: Create a pull request for 'feature-developer1-changes' on GitHub by visiting:
remote:      https://github.com/sandeepsiyadri/learn-git/pull/new/feature-developer1-changes
remote:
To https://github.com/sandeepsiyadri/learn-git.git
 * [new branch]      feature-developer1-changes -> feature-developer1-changes
```

- #### Pull Changes: 
To incorporate changes made by other developers, developers pull the latest changes from the remote repository into their local repository.


```git pull origin <branch_name>```


- #### Resolve Conflicts (if any): 
If there are conflicting changes between the local and remote repositories, developers resolve these conflicts manually.

- #### Review Changes: 
Developers review each other's code through pull requests or code reviews before merging changes into the main branch.

- #### Merge Changes:
Once the changes are reviewed and approved, developers merge them into the main branch (e.g., master or main).


- #### Update Local Repository:
After merging changes into the main branch, developers pull the latest changes from the remote repository to update their local repository.

```git pull origin <main_branch>```


This fundamental workflow outlines the typical sequence of actions that developers follow while the usage of Git for version manage in a centralized environment. 

## But ...

While the centralized workflow is a simple and straightforward approach to version control, it's not commonly used in real-world development scenarios, especially in larger or distributed teams. 

In most cases, teams adopt branching strategies that allow for feature branching, continuous integration, and efficient collaboration, which are better supported by workflows like Gitflow, GitHub Flow, or variations thereof.

The advanced workflows offer benefits such as:

- #### **Isolation of Features:**
Developers can work on features or bug fixes in isolation without affecting the stability of the main codebase.

- #### **Parallel Development:**
Multiple developers can work on different features concurrently, speeding up development and allowing for better collaboration.

- #### **Release Management:**
Clear branching strategies facilitate the management of releases, including feature freezes, release candidates, and hotfixes.

- #### **Code Review and Quality Assurance:**
Pull requests and code reviews are integral parts of these workflows, ensuring code quality, knowledge sharing, and collaboration among team members.

- #### **Continuous Integration and Deployment:**
These workflows often integrate with continuous integration/continuous deployment (CI/CD) pipelines, enabling automated testing, deployment, and delivery of code changes.

Overall, while the centralized workflow provides a basic model for version control, real-world development typically requires more sophisticated branching strategies and workflows to support collaboration, code quality, and efficient release management.

## Gitflow Workflow
The Gitflow Workflow is a branching model that defines a strict branching structure for development.

- It distinguishes between feature branches, release branches, hotfix branches, and the main development branch.
- Development work primarily occurs in *feature* branches branched off from the *development* branch.
- Once a feature is complete, it is merged back into the *development* branch.
- Periodically, *release* branches are created from the *development* branch to prepare for production releases.
- *Hotfix* branches are used to quickly address critical issues in production, branched off from the *main* branch.

Here's an example of how branches can be named in the Gitflow workflow:

```
main (or master)
develop
feature/user-authentication
feature/payment-gateway-integration
release/v1.2.0
hotfix/bug-fix-login-issue
```
By following a consistent naming convention for branches in the Gitflow workflow, developers can easily understand the purpose of each branch and how they fit into the overall development process.

### Note
It's not mandatory to adhere strictly to its rules. The Gitflow workflow serves as a guideline or template but teams can adapt and customize based on the specific requirements of their projects and development processes.

## PR code review and quality assurance

In the real-time software development workflows, code review and quality assurance are integrated into the process of creating and merging pull requests (PRs), often in conjunction with automated pipelines.

### Here's how it typically works:

 #### **1. Creation of Pull Request (PR):**

- When a developer completes their work on a feature or bug fix, they create a PR to merge their changes into the main branch (e.g., master or main) or develp branch.
- The PR includes a summary of the changes, along with any relevant context or documentation.

 #### **2. Automated Pipelines:**

- Upon creation of the PR, automated pipelines, often referred to as continuous integration (CI) pipelines, are triggered.
- These pipelines perform various tasks such as compiling the code, running automated tests, checking for code style adherence, and performing other quality checks.

 #### **3. Code Review:**

- The PR undergoes review by other developers on the team. They provide feedback, suggestions, and possibly identify issues or areas for improvement.
- Code review is an important aspect of maintaining code quality, sharing knowledge, and ensuring consistency within the codebase.

 #### **4. Iterative Changes:**

- Based on the feedback received during code review, the developer may make additional changes to address comments or concerns.
- The process of review and iteration continues until the PR is approved by the team.

 #### **5. Merge:**

- Once the PR is approved and all checks pass (including the automated pipeline), the changes are merged into the main branch.
- The merged changes become part of the codebase and are typically included in subsequent releases or deployments.

## To Summarize...

Ultimately, the goal of adopting a workflow like Gitflow is to provide structure and organization to the development process, but teams have the flexibility to adapt and tailor the workflow to best fit their project's needs and constraints. As long as the team agrees on the workflow and follows it consistently, they can achieve efficient collaboration and code management.
