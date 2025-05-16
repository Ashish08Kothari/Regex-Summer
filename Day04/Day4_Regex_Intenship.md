# Day4_Regex_Internship

## Git and GitHub

### **What is Git?**
Git is a distributed version control system (VCS).
It helps multiple people work on the same code project or documents by tracking and managing changes to the files.

### **What is VCS?**
Every time you make a change, whether it's adding a sentence to a document or altering a line of code, the VCS records and saves the outcome.

### **Why VCS?**
- **Backup and Restore**: Files are safe against accidental losses or mistakes.
- **Collaboration**: Multiple people can work on the same project simultaneously.
- **Branching and Merging**: Users can experiment and bring changes back in line without losing work.
- **Tracking Changes**: You can see specific changes made and by whom.

### **Installing Git**
Step-by-step installation and configuring Git:
```bash
$ git config --global user.name  
> Sets your name for Git commits globally. "Paul Philips"
$ git config --global user.email  
> Sets your email for Git commits globally. paulphilips@email.com"
$ git config --list  
> Lists all the Git configuration settings.
```

### **Creating Local Git Repo**
```bash
$ git init  
> Initializes a new Git repository in your current directory.
```

### **Git Commit**
A git commit  
> Records staged changes to the repository. captures a snapshot of the project's currently staged changes.

### **Negative Cases and Fixes**
- **Undo uncommitted changes**: `git restore .  
> Reverts all changes in the working directory to the last commit.`
- **Unstage changes**: `git restore --staged <file>  
> Removes the specified file from the staging area.`
- **Discard staged changes**: `git restore <file>  
> Discards changes made to the specified file in the working directory.`
- **Retrieve staged changes**: `git restore --worktree index.html  
> Recovers the staged version of 'index.html'.`
- **Uncommit**: 
  - Keep changes: `git reset --soft HEAD^  
> Undo the last commit but keep the changes staged.`
  - Discard changes: `git reset --hard HEAD^  
> Undo the last commit and discard the changes.`

### **Logging in Git**
Useful log commands:
```bash
git log  
> Displays commit history. -p -2  
> Shows the last 2 commits with the diff.
git log  
> Displays commit history. --stat  
> Displays a summary of changes for each commit.
git log  
> Displays commit history. --pretty=oneline  
> Shows each commit on a single line.
git log  
> Displays commit history. --pretty=format:"%h - %an, %ar : %s"  
> Formats log output with hash, author, relative date, and message.
git log  
> Displays commit history. -S function_name  
> Searches for commits that added or removed 'function_name'.
git log  
> Displays commit history. --grep="fix bug"  
> Searches commit messages for the phrase 'fix bug'.
git log  
> Displays commit history. --since="2024-01-01"  
> Shows commits made after January 1, 2024.
git log  
> Displays commit history. --until="2024-01-01"  
> Shows commits made before January 1, 2024.
git log  
> Displays commit history. --author="Paul"  
> Shows commits made by 'Paul'.
git log  
> Displays commit history. --no-merges  
> Excludes merge commits from the log.
```

### **Remote Repository and GitHub**
A remote repository resides on a network server or hosted online.

#### **Add Remote Repo**
```bash
git remote  
> Lists remote repositories. add origin <remote URL>  
> Adds a new remote repository with the given URL.
git push  
> Uploads local commits to the remote repository. -u origin master  
> Pushes the local branch to remote and sets upstream.
```

#### **Work with Remote**
```bash
git remote  
> Lists remote repositories.
git remote  
> Lists remote repositories. -v
git remote  
> Lists remote repositories. show origin
git clone  
> Clones a remote repository to your local machine.
git pull  
> Fetches and merges changes from the remote repository.
```

### **Git Commands Overview**
- `git status  
> Shows the working directory and staging area status.` – Check changes
- `git diff  
> Displays differences between working directory and the last commit.` – Compare with last committed version
- `git add  
> Stages changes for the next commit.` – Stage modified files
- `git commit  
> Records staged changes to the repository.` – Commit changes
- `git push  
> Uploads local commits to the remote repository.` – Push changes to remote repo
- `git log  
> Displays commit history.` – View commit history

### **Forking and Pull Requests**
Fork the repo, make improvements, and create pull requests.

### **.gitignore**
List files/folders to exclude from commits in `.gitignore`.

### **Cloning a Repo**
```bash
git clone  
> Clones a remote repository to your local machine. <remote_repo_link>
```

### **Git Clean**
Clean the working directory.

### **Git Tags**
Tagging versions:
```bash
git tag -a v1.0 -m "My version 1.0"  
> Creates an annotated tag named v1.0 with a message.
git show v1.0  
> Displays information about tag v1.0.
git tag -a v1.2 <commit_no>  
> Tags a past commit with v1.2.
git tag -d <tag_no>  
> Deletes the specified tag locally.
git push  
> Uploads local commits to the remote repository. origin v1.5
git push  
> Uploads local commits to the remote repository. origin --tags
git checkout -b version2 v2.0.0  
> Creates a new branch 'version2' from tag v2.0.0.
```

### **GitHub Project Management**
- Issues, GitHub Actions, and Projects.
- Kanban board tracking.
- Automate workflows with GitHub Actions.
- Secure accounts and manage permissions.
- Monitor repositories for vulnerabilities.