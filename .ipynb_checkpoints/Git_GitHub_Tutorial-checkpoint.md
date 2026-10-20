# Git and GitHub: A Complete Beginner-to-Intermediate Guide

> **Purpose:** These notes explain Git, version control, common
> commands, branches, tags, remote repositories, and a complete workflow
> for uploading a project to GitHub.
>
> **How to use in Jupyter:** Save this file as `Git_GitHub_Tutorial.md`.
> You can open it in JupyterLab, VS Code, or any Markdown editor. To put
> it directly into a notebook, create a **Markdown cell** and paste the
> relevant sections. Code examples should be run in a terminal, Git
> Bash, or a Jupyter cell prefixed with `!` where appropriate.

------------------------------------------------------------------------

## Table of Contents

1.  [What is Git?](#1-what-is-git)
2.  [What are VCS and SCM?](#2-what-are-vcs-and-scm)
3.  [Examples of version control
    systems](#3-examples-of-version-control-systems)
4.  [Why do we need version control?](#4-why-do-we-need-version-control)
5.  [Types of version control
    systems](#5-types-of-version-control-systems)
6.  [Advantages of Git](#6-advantages-of-git)
7.  [How Git works: terminology and
    architecture](#7-how-git-works-terminology-and-architecture)
8.  [Installing and configuring Git](#8-installing-and-configuring-git)
9.  [Creating and cloning
    repositories](#9-creating-and-cloning-repositories)
10. [Understanding repository
    status](#10-understanding-repository-status)
11. [Making changes: add and commit](#11-making-changes-add-and-commit)
12. [Writing good commit messages](#12-writing-good-commit-messages)
13. [Ignoring files with
    `.gitignore`](#13-ignoring-files-with-gitignore)
14. [Viewing commits and changes](#14-viewing-commits-and-changes)
15. [Creating software versions with
    tags](#15-creating-software-versions-with-tags)
16. [Branches and non-linear
    development](#16-branches-and-non-linear-development)
17. [Merging branches](#17-merging-branches)
18. [Working with remote
    repositories](#18-working-with-remote-repositories)
19. [Uploading a new project to
    GitHub](#19-uploading-a-new-project-to-github)
20. [Undoing or correcting changes](#20-undoing-or-correcting-changes)
21. [Common mistakes and
    troubleshooting](#21-common-mistakes-and-troubleshooting)
22. [Git command cheat sheet](#22-git-command-cheat-sheet)
23. [Practice exercises](#23-practice-exercises)

------------------------------------------------------------------------

# 1. What is Git?

**Git is a distributed version control system (DVCS)** used to track
changes to files over time. It is especially popular for software
development, but it can also track documentation, data-processing
scripts, configuration files, and many other text-based files.

Imagine that you are building a machine-learning project. On Monday,
your code works. On Tuesday, you change a preprocessing function and the
model stops working. Without version control, you may have to remember
what changed or maintain copies such as:

-   `model_final.py`
-   `model_final_v2.py`
-   `model_final_really_final.py`

Git provides a more reliable way to record versions and return to
earlier states.

### What can Git do?

-   Record snapshots of a project's tracked files.
-   Show what changed between versions.
-   Help recover earlier versions of files.
-   Let developers work on separate features in branches.
-   Combine work from different developers.
-   Keep a local history and synchronize work with remote repositories
    such as GitHub.

### Is Git the same as GitHub?

No.

  -----------------------------------------------------------------------
  Git                                 GitHub
  ----------------------------------- -----------------------------------
  A version control tool              An online platform for hosting Git
                                      repositories

  Runs locally on your computer       Provides remote hosting and
                                      collaboration features

  Tracks commits, branches, and file  Adds pull requests, issues, code
  changes                             review, access controls, and more

  Can be used without GitHub          Commonly hosts Git repositories
  -----------------------------------------------------------------------

Other hosting platforms also support Git, including GitLab and
Bitbucket.

------------------------------------------------------------------------

# 2. What are VCS and SCM?

## Version Control System (VCS)

A **Version Control System** records changes to files so that users can
inspect, compare, and recover previous versions.

For example, a VCS can help answer:

-   What changed in this file?
-   Who made a particular change?
-   When was it committed?
-   Which change introduced a bug?
-   How can I restore an earlier version?

## Source Code Management (SCM)

**Source Code Management** refers to managing source code and its
changes throughout software development. The term is often used
interchangeably with version control in everyday software-development
discussions.

Strictly speaking, source code management can refer to a broader
development workflow, while version control is the system that records
file history.

## Repository

A **repository**, often shortened to *repo*, is a location where Git
stores project history and version-control information.

A Git repository includes a `.git` directory containing metadata and
Git's object database. A working repository also has the files you edit.

A repository may be:

-   **Local:** stored on your computer.
-   **Remote:** stored on a server or hosting platform such as GitHub.

------------------------------------------------------------------------

# 3. Examples of version control systems

  -----------------------------------------------------------------------
  System                  Type                    Notes
  ----------------------- ----------------------- -----------------------
  Git                     Distributed             Widely used; each clone
                                                  contains local
                                                  repository history

  Apache Subversion (SVN) Centralized             Commonly uses a central
                                                  repository

  CVS                     Centralized             An older version
                                                  control system

  Mercurial               Distributed             Another distributed
                                                  version control system

  Perforce Helix Core     Commonly centralized in Often used for large
                          workflow                codebases and
                                                  game-development assets
  -----------------------------------------------------------------------

Git is especially popular because branching is efficient, local
operations are fast, and developers can work without constantly
contacting a central server.

------------------------------------------------------------------------

# 4. Why do we need version control?

## 4.1 Track changes

Git records commits, allowing you to see how a project evolved.

## 4.2 Recover earlier versions

If a recent change breaks your application, Git history can help you
inspect or restore an earlier version.

## 4.3 Fix bugs

Developers can investigate when a bug appeared and compare the code
before and after a change.

## 4.4 Support non-linear development

A developer can create a branch to experiment with a feature without
immediately changing the main development branch.

## 4.5 Enable collaboration

Multiple people can work on a project, exchange commits, and merge their
work. Conflicting edits sometimes require manual conflict resolution.

## 4.6 Keep a record of decisions

Useful commit messages explain why changes were made and make project
history easier to understand.

## 4.7 Back up and share work

A remote repository can provide another copy of a project's history.
However, a remote repository is not automatically a complete backup of
every uncommitted file on your computer.

------------------------------------------------------------------------

# 5. Types of version control systems

## 5.1 Centralized Version Control System (CVCS)

In a centralized system, a central server stores the main repository,
and users typically check out or update files from it.

**Conceptual structure:**

``` text
             Central Repository
              /      |      \
          User A   User B   User C
```

### Advantages

-   One central place for the repository.
-   Centralized permissions and administration can be straightforward.
-   A familiar model for organizations that prefer a single source of
    truth.

### Disadvantages

-   Some operations depend on network access to the server.
-   A central server outage can interrupt many workflows.
-   The central repository can become a critical point of failure unless
    it is backed up and replicated.

## 5.2 Distributed Version Control System (DVCS)

In a distributed system such as Git, each clone has its own repository
database and local history. Users can make commits locally and
synchronize with others later.

**Conceptual structure:**

``` text
       Remote Repository (for example, GitHub)
                 /                 \
        Local Repository A    Local Repository B
              |                     |
          Developer A           Developer B
```

### Advantages

-   Most everyday version-control operations work offline.
-   Local commits and history inspection are fast.
-   Developers can work independently.
-   Branching and merging are central parts of the workflow.
-   A clone contains substantial repository history, though it may be
    shallow or otherwise limited depending on how it was created.

### Important clarification

Distributed does not mean that every copy automatically contains every
uncommitted change or every possible branch. Only committed work that
has been transferred is available in another repository.

------------------------------------------------------------------------

# 6. Advantages of Git

## 6.1 Version control

Every commit records a version of the tracked project state. You can
compare versions and inspect how the project changed.

## 6.2 Bug fixing

Branches let you investigate or fix a bug separately from ongoing
feature work. History can help identify the commit that introduced a
problem.

## 6.3 Non-linear development

Different features can be developed on separate branches and combined
later.

## 6.4 Collaborative development

Developers can exchange work through remote repositories, review
changes, and resolve conflicts.

## 6.5 Local and offline work

You can create commits, inspect local history, and use many Git commands
without an internet connection.

## 6.6 Traceability

Commit authorship metadata, timestamps, messages, and diffs help teams
understand the history of a project. These details are useful records,
although they are not proof that every recorded claim is authentic.

------------------------------------------------------------------------

# 7. How Git works: terminology and architecture

## 7.1 The three main areas

A useful beginner model has three areas:

1.  **Working directory:** The files you currently see and edit.
2.  **Staging area (index):** The changes selected for the next commit.
3.  **Local repository:** The committed history stored by Git.

``` text
Edit files
   |
   v
Working Directory
   |
   | git add
   v
Staging Area
   |
   | git commit
   v
Local Repository
   |
   | git push
   v
Remote Repository (for example, GitHub)
```

`git add` does not upload files to GitHub. It stages changes for a
future local commit. `git commit` records the staged snapshot locally.
`git push` transfers eligible commits to a remote repository.

### Example

Suppose you edit `app.py`.

``` bash
git status
git add app.py
git status
git commit -m "Add input validation"
git status
```

-   Before `git add`, the modification is usually listed as unstaged.
-   After `git add`, it is staged.
-   After a successful commit, that staged version is recorded in
    history.

If you edit `app.py` again after staging it, the new edit is not
automatically included in the already staged snapshot. Run
`git add app.py` again to stage the newer version.

## 7.2 Important terminology

### Repository

The Git database and history for a project.

### Commit

A recorded snapshot of the staged project state, with metadata and
references to its parent commit or commits.

### Branch

A movable reference to a line of development. A branch lets you work on
a feature, experiment, or fix independently.

### `main`

A commonly used name for the primary branch. It is not a special branch
name required by Git; repositories can use other names.

### `origin`

A conventional name for the default remote created by `git clone`. It is
only a name, not a special kind of repository.

### `HEAD`

Usually identifies the currently checked-out commit or branch. In a
normal attached state, `HEAD` points to the current branch, and that
branch points to a commit.

### `HEAD^`

Usually means the first parent of `HEAD`.

### `HEAD~4`

Means the fourth first-parent ancestor of `HEAD`, if that many ancestors
exist. It does **not** mean the "great-great grandparent" in every
context; the number specifies how many first-parent steps to go back.

### Working tree

The checked-out files and directories that you can inspect and edit.

### Remote-tracking branch

A local reference that records the last fetched state of a branch on a
remote, such as `origin/main`. It updates when you fetch or perform an
operation that fetches.

### Merge conflict

A situation where Git cannot automatically reconcile competing changes.
A developer must edit the affected files and complete the merge.

------------------------------------------------------------------------

# 8. Installing and configuring Git

## 8.1 Installation

Download Git from the official website:

-   Git website: https://git-scm.com/

Follow the installer instructions for your operating system. On Windows,
Git Bash is a convenient terminal for Git commands.

Verify the installation:

``` bash
git --version
```

If Git is installed, the command prints the installed version.

## 8.2 Configure your name and email

Git records author and committer information in commits.

``` bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Replace the example values with your preferred identity.

`--global` applies the setting to your user account on that computer. A
repository-specific setting can override it:

``` bash
git config user.name "Project Author"
git config user.email "project-author@example.com"
```

Inspect settings:

``` bash
git config --list
git config user.name
git config user.email
```

**Privacy note:** The configured name and email can be visible in commit
history shared with others. If you prefer not to expose a personal email
on a public repository, consider using the email privacy features
provided by your Git hosting service.

------------------------------------------------------------------------

# 9. Creating and cloning repositories

## 9.1 Initialize a new repository

Create a project folder and initialize Git:

``` bash
mkdir my-project
cd my-project
git init
```

Or initialize a named directory:

``` bash
git init my-project
```

`git init` creates the repository metadata. It does not automatically
create a commit or upload anything.

Check the result:

``` bash
git status
```

## 9.2 Clone an existing repository

`git clone` downloads a repository and creates a local working copy.

``` bash
git clone <repository-url>
```

Example:

``` bash
git clone https://github.com/campusx-official/streamlit-basics.git
cd streamlit-basics
```

Cloning normally creates a remote named `origin` and checks out the
repository's default branch.

### `git init` versus `git clone`

  -----------------------------------------------------------------------
  Command                             Purpose
  ----------------------------------- -----------------------------------
  `git init`                          Start a new Git repository in a
                                      directory

  `git clone <url>`                   Copy an existing remote repository
                                      into a new local directory
  -----------------------------------------------------------------------

Use `git init` when starting from your own local files. Use `git clone`
when you want to work on an existing repository.

------------------------------------------------------------------------

# 10. Understanding repository status

Run:

``` bash
git status
```

Git reports the state of the working directory and staging area.

Common categories include:

-   **Untracked:** A file Git is not tracking yet.
-   **Modified:** A tracked file has changes that have not necessarily
    been staged.
-   **Changes to be committed:** Staged changes waiting for a commit.
-   **Unmodified:** A tracked file matches the checked-out committed
    version.
-   **Conflicts:** Some files need conflict resolution during a merge or
    related operation.

Example workflow:

``` bash
echo "print('Hello, Git!')" > app.py
git status
git add app.py
git status
git commit -m "Add starter application"
git status
```

In Jupyter, shell commands can often be run by prefixing them with `!`,
for example:

``` python
!git status
```

For a series of Git operations, a terminal is often easier to use.

------------------------------------------------------------------------

# 11. Making changes: add and commit

## 11.1 Stage a specific file

``` bash
git add app.py
```

This stages the current content of `app.py`.

Stage multiple files:

``` bash
git add app.py README.md
```

## 11.2 Stage all changes under the current directory

``` bash
git add .
```

This stages eligible changes under the current directory, subject to
Git's ignore rules. Review `git status` before committing to ensure you
are not staging secrets, generated files, or unrelated work.

Other useful forms include:

``` bash
git add -A
git add -p
```

-   `git add -A` stages additions, modifications, and deletions
    throughout the working tree.
-   `git add -p` lets you interactively select portions of changes to
    stage.

## 11.3 Commit staged changes

``` bash
git commit -m "Add input validation"
```

A commit records the staged changes in local history.

The `-m` option supplies the commit message.

## 11.4 The shortcut `git commit -am`

``` bash
git commit -am "Fix input validation"
```

This stages modifications and deletions to **already tracked** files and
commits them. It does **not** automatically stage new untracked files.

For a new file, use:

``` bash
git add new_file.py
git commit -m "Add new file"
```

## 11.5 When should you commit?

A good commit usually represents one coherent, understandable change.

Good moments to commit include:

-   A small bug fix is complete.
-   A feature reaches a meaningful checkpoint.
-   A refactor is complete and tested.
-   Documentation for a feature is updated.
-   A working change is ready for review.

Avoid combining unrelated work in one large commit. Smaller, focused
commits are usually easier to review and troubleshoot.

### Example

``` bash
git status
git add app.py tests/
git commit -m "Validate uploaded file type"
```

Before committing, consider running relevant tests and reviewing the
staged changes:

``` bash
git diff --cached
```

------------------------------------------------------------------------

# 12. Writing good commit messages

A commit message should explain the purpose of the change.

### Examples

Good:

``` text
Add input validation
Fix empty-file handling
Update installation instructions
Handle missing values in preprocessing
```

Less useful:

``` text
Changes
Update
Final
Fix
Stuff
```

## A practical rule of thumb

-   Keep the subject short and specific.
-   Explain **what** changed and, when useful, **why**.
-   Prefer one focused purpose per commit.
-   Use a body for extra context if the change is not self-explanatory.
-   Follow the conventions used by your team or project.

Example:

``` bash
git commit -m "Handle missing values in preprocessing"
```

For a longer message, open the configured editor:

``` bash
git commit
```

A commit message does not have to describe every line. Its job is to
help someone understand the intent of the change.

------------------------------------------------------------------------

# 13. Ignoring files with `.gitignore`

A `.gitignore` file lists files and directories that Git should
generally ignore when they are untracked.

Create a file named `.gitignore` in the project root.

Example:

``` gitignore
# Log directory
logs/

# Files ending in .notes
*.notes

# Python cache directories and bytecode
__pycache__/
*.py[cod]

# Virtual environment
.venv/

# Local environment variables and secrets
.env

# Database files
*.db

# IDE settings
.idea/
```

## What do these patterns mean?

  -----------------------------------------------------------------------
  Pattern                             Meaning
  ----------------------------------- -----------------------------------
  `logs/`                             Ignore directories named `logs` at
                                      the relevant location; a root
                                      pattern can target the root-level
                                      directory

  `*.notes`                           Ignore files whose names end in
                                      `.notes`

  `__pycache__/`                      Ignore Python cache directories

  `.env`                              Ignore files named `.env` matching
                                      the pattern's scope

  `*.db`                              Ignore files ending in `.db`

  `.idea/`                            Ignore directories named `.idea` at
                                      the relevant location
  -----------------------------------------------------------------------

Git ignore rules support wildcards and other pattern syntax. The exact
scope depends on where the `.gitignore` file is located and whether a
pattern starts with `/` or contains a path.

### Important: `.gitignore` does not untrack an existing file

If a file has already been committed, adding it to `.gitignore` will not
remove it from Git history or stop Git from tracking it.

To stop tracking a file while keeping it on your computer:

``` bash
git rm --cached data.db
git commit -m "Stop tracking local database"
```

For a directory, a recursive removal from the index may be appropriate:

``` bash
git rm -r --cached some_directory/
```

Review the command before running it. `--cached` removes paths from
Git's index, not from the working directory.

### Check why a file is ignored

``` bash
git check-ignore -v data.db
```

### Security warning

Do not commit passwords, API keys, private tokens, or credentials.
Ignoring a secret file helps prevent accidental future additions, but it
does not erase a secret that was already committed or pushed. If a
secret has been exposed, revoke or rotate it first and follow the
repository's cleanup process.

------------------------------------------------------------------------

# 14. Viewing commits and changes

## 14.1 View commit history

``` bash
git log
```

This shows commits with details such as the commit ID, author, date, and
message.

A compact view:

``` bash
git log --oneline
```

A more descriptive compact view:

``` bash
git log --oneline --decorate --graph --all
```

This can show branch references and a graph of the history.

## 14.2 View a commit

``` bash
git show
```

Show a particular commit:

``` bash
git show <commit-id>
```

`git show` displays information about an object, commonly a commit and
its changes.

## 14.3 View unstaged changes

``` bash
git diff
```

This compares the working tree with the staging area for tracked files.

## 14.4 View staged changes

``` bash
git diff --cached
```

This compares the staging area with the current commit (`HEAD`).

## 14.5 Compare two commits

``` bash
git diff <commit1-id> <commit2-id>
```

This shows the differences between the two commit snapshots.

You can also compare a particular file:

``` bash
git diff <commit1-id> <commit2-id> -- app.py
```

## 14.6 View commit statistics

``` bash
git log --stat
```

Show statistics and detect renames where possible:

``` bash
git log --stat -M
```

The `-M` option enables rename detection for history display. Rename
detection is based on similarity; Git does not store a separate
permanent "rename object."

## 14.7 Follow a file through renames

``` bash
git log --follow -- app.py
```

This attempts to follow the history of a file across renames. `--follow`
is designed for a single file path.

## 14.8 Inspect another repository's commits

If you have cloned someone else's repository, enter that repository and
run:

``` bash
git log --oneline --all --decorate --graph
git show <commit-id>
git diff <commit1-id> <commit2-id>
```

These commands inspect history available in your local clone. If the
remote has newer commits, fetch them first:

``` bash
git fetch origin
```

------------------------------------------------------------------------

# 15. Creating software versions with tags

A **tag** is a reference used to mark a specific commit, often for a
release.

A common version format is **MAJOR.MINOR.PATCH**, for example `2.4.1`.

-   **MAJOR:** Incompatible or breaking changes.
-   **MINOR:** New functionality that is generally backward-compatible.
-   **PATCH:** Backward-compatible bug fixes.

This is a common semantic-versioning convention. A project may follow a
different versioning policy, so follow its release rules.

## 15.1 Create a lightweight tag

``` bash
git tag v1.0.0
```

This marks the current commit with a lightweight tag.

## 15.2 Create an annotated tag

``` bash
git tag -a v1.0.0 -m "Release version 1.0.0"
```

Annotated tags include tag metadata and a message. They are commonly
preferred for releases.

## 15.3 List tags

``` bash
git tag
```

List tags matching a pattern:

``` bash
git tag -l "v1.*"
```

## 15.4 Tag an earlier commit

``` bash
git tag -a v0.9.0 <commit-id> -m "Release version 0.9.0"
```

Replace `<commit-id>` with the intended commit ID.

## 15.5 Inspect a tag

``` bash
git show v1.0.0
```

## 15.6 Delete a local tag

``` bash
git tag -d v1.0.0
```

## 15.7 Push tags to a remote

``` bash
git push origin v1.0.0
```

Push all local tags:

``` bash
git push origin --tags
```

Be cautious with `--tags` if your repository contains tags that should
not yet be published.

## 15.8 Move a tag

Moving an existing tag changes which commit the tag identifies. This can
confuse other users if the tag has already been published. Avoid moving
published release tags unless the project has a clear policy for doing
so.

For a local tag:

``` bash
git tag -f v1.0.0 <new-commit-id>
```

To update a tag on a remote, you must also update the remote reference.
Because this can overwrite a published reference, coordinate with
collaborators and use an explicit, carefully reviewed push operation.
Prefer creating a new release tag when possible.

------------------------------------------------------------------------

# 16. Branches and non-linear development

A branch is a lightweight reference to a commit. Branches make it
possible to develop features or fixes separately.

For example:

``` text
main:       A---B---C
                 \
feature:          D---E
```

The feature branch can move forward without immediately changing `main`.

## 16.1 List local branches

``` bash
git branch
```

List remote-tracking branches:

``` bash
git branch -r
```

List local and remote-tracking branches:

``` bash
git branch -a
```

## 16.2 Create a branch

``` bash
git branch feature-login
```

This creates the branch but does not switch to it.

## 16.3 Switch to an existing branch

Modern command:

``` bash
git switch feature-login
```

Traditional command:

``` bash
git checkout feature-login
```

## 16.4 Create and switch in one command

Modern command:

``` bash
git switch -c feature-login
```

Traditional command:

``` bash
git checkout -b feature-login
```

## 16.5 Delete a merged branch

``` bash
git branch -d feature-login
```

Git normally refuses to delete a branch with unmerged work that it
considers at risk of being lost.

## 16.6 Force-delete a branch

``` bash
git branch -D feature-login
```

This deletes the local branch reference even if Git considers it
unmerged. It does not automatically erase every commit that was
reachable only through that branch forever, but the work may become
difficult to find and could eventually be garbage-collected. Use it
carefully.

## 16.7 A typical feature workflow

``` bash
git switch main
git pull --ff-only origin main
git switch -c feature-login

# Edit files and test the feature.
git status
git add .
git commit -m "Add login form"

git switch main
git merge feature-login
```

This example assumes you are allowed to merge directly into `main` and
that the branches can be merged cleanly. In a team, you may instead push
the feature branch and open a pull request.

------------------------------------------------------------------------

# 17. Merging branches

A **merge** combines changes from one branch into the branch you
currently have checked out.

## 17.1 Merge one branch into another

Suppose branch `a` contains work you want to merge into branch `b`.

``` bash
git switch b
git merge a
```

The target branch is the one you check out before running `git merge`.

Equivalent older syntax:

``` bash
git checkout b
git merge a
```

## 17.2 What happens during a merge?

Depending on the history, Git may:

-   Perform a **fast-forward**: move the target branch reference forward
    without creating a merge commit.
-   Create a **merge commit**: record the combination of two lines of
    development.
-   Report a **merge conflict**: ask you to resolve competing changes.

## 17.3 Resolve a merge conflict

1.  Run the merge and read Git's output.
2.  Run `git status` to identify conflicted files.
3.  Open each conflicted file and resolve the conflict markers.
4.  Test the result.
5.  Stage the resolved files.
6.  Complete the merge commit if Git requires one.

Example:

``` bash
git status
# Edit conflicted files to resolve the conflict.
git add app.py
git commit
```

Do not blindly delete conflict markers without checking which code
should remain.

## 17.4 Squash merge

``` bash
git switch main
git merge --squash feature-login
git commit -m "Add login feature"
```

A squash merge combines the changes from the source branch into the
staging area as one combined change, rather than preserving all of that
branch's commits as individual commits in the target branch's history.
You then create the commit yourself.

The source branch is not automatically deleted.

------------------------------------------------------------------------

# 18. Working with remote repositories

A **remote** is a named connection to another Git repository. The other
repository might be hosted on GitHub, a company server, or another
computer.

## 18.1 List remotes

``` bash
git remote
```

Show remote names and URLs:

``` bash
git remote -v
```

A cloned repository commonly has a remote named `origin`.

## 18.2 Add a remote

``` bash
git remote add origin <repository-url>
```

Example:

``` bash
git remote add origin https://github.com/your-username/example.git
```

If `origin` already exists, Git will report an error. Inspect existing
remotes before changing them.

## 18.3 Rename a remote

``` bash
git remote rename old-name new-name
```

## 18.4 Remove a remote connection

``` bash
git remote remove origin
```

This removes the local remote configuration; it does not delete the
hosted repository.

## 18.5 Fetch changes

``` bash
git fetch origin
```

Fetch downloads new commits and updates remote-tracking references. It
does **not** automatically merge those changes into your current branch.

Fetch a particular branch:

``` bash
git fetch origin main
```

After fetching, inspect what arrived:

``` bash
git log --oneline --decorate --all
git diff main origin/main
```

The comparison assumes the relevant local and remote-tracking branches
exist.

## 18.6 Pull changes

``` bash
git pull
```

`git pull` fetches from a remote and integrates changes into the current
branch according to the configured tracking relationship and pull
strategy. Depending on configuration and history, integration may use a
merge or rebase.

An explicit form is:

``` bash
git pull origin main
```

Use this when you intend to integrate the remote `main` branch into your
currently checked-out branch.

## 18.7 Pull with rebase

``` bash
git pull --rebase origin main
```

This fetches remote changes and replays your local, unpushed commits on
top of the fetched branch. It often creates a linear-looking history.

Rebasing rewrites commit IDs for the commits being replayed. Avoid
rebasing commits that others already depend on unless your team
understands and agrees to that workflow.

## 18.8 Push changes

``` bash
git push origin main
```

This sends eligible local commits from the current local `main` branch
to the remote branch named `main`.

A common first-push command is:

``` bash
git push -u origin main
```

The `-u` option sets the upstream tracking relationship, making future
`git push` and `git pull` commands more convenient.

Push a feature branch:

``` bash
git push -u origin feature-login
```

### The four essential synchronization commands

  -----------------------------------------------------------------------
  Command                             Main purpose
  ----------------------------------- -----------------------------------
  `git fetch`                         Download remote updates without
                                      integrating them into the current
                                      branch

  `git pull`                          Fetch and integrate remote updates

  `git pull --rebase`                 Fetch and replay local commits on
                                      top of the fetched history

  `git push`                          Upload local commits to a remote
                                      repository
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# 19. Uploading a new project to GitHub

This section walks through the complete workflow.

## 19.1 Example project structure

Imagine your project looks like this:

``` text
Project/
├── static/
├── .idea/
├── logs/
├── app.py
├── data.db
├── requirements.txt
└── .gitignore
```

A possible `.gitignore` is:

``` gitignore
logs/
*.db
.idea/
__pycache__/
*.py[cod]
.venv/
.env
```

These patterns help prevent local logs, databases, IDE settings, Python
bytecode, virtual environments, and environment files from being added
as untracked files.

**Important:** Do not ignore files blindly. Some databases or data files
may be essential project assets. Decide which files belong in the
repository. Never commit secrets.

## 19.2 Create an empty repository on GitHub

1.  Sign in to GitHub.
2.  Create a new repository.
3.  Choose a repository name, such as `example`.
4.  Choose the visibility you want.
5.  If you already have a local project and intend to push it, creating
    the remote repository without a README, license, or `.gitignore` can
    avoid an unnecessary initial-history conflict.
6.  Create the repository and copy its Git URL.

Official site: https://github.com/

A repository URL may look like:

``` text
https://github.com/your-username/example.git
```

Replace the example URL with the URL of your own repository.

## 19.3 Open a terminal in the project directory

``` bash
cd path/to/Project
```

Make sure you are in the correct directory:

``` bash
pwd
```

On Windows Command Prompt, `cd` and `dir` are common alternatives for
checking the location and contents.

## 19.4 Initialize Git

``` bash
git init
```

This creates a local repository if one does not already exist.

## 19.5 Review and stage files

``` bash
git status
git add .
git status
```

Inspect the status carefully. Confirm that secrets, local databases,
logs, virtual environments, and other unwanted files are not staged.

For a closer review:

``` bash
git diff --cached
```

## 19.6 Make the first commit

``` bash
git commit -m "Initial commit"
```

If Git reports that your identity is not configured, set `user.name` and
`user.email` as explained earlier, then retry.

## 19.7 Name the branch `main`

``` bash
git branch -M main
```

This renames the current branch to `main`. It is commonly used when
preparing a new repository for its first push.

## 19.8 Connect the remote repository

``` bash
git remote add origin https://github.com/your-username/example.git
```

Use the actual URL copied from GitHub.

Check it:

``` bash
git remote -v
```

If `origin` already exists, inspect it first. If it points to the wrong
repository, update the URL deliberately rather than adding a duplicate
remote:

``` bash
git remote set-url origin <correct-repository-url>
```

## 19.9 Push the branch

``` bash
git push -u origin main
```

Git may ask you to authenticate. Follow the authentication flow
supported by your Git installation and hosting provider. For HTTPS, a
regular account password is generally not the method used for Git
operations; a supported credential manager, browser-based sign-in, or
token may be required. SSH is another option.

After a successful push, refresh the GitHub repository page to view the
committed files.

## 19.10 Complete command sequence

For a new local project and a newly created, empty GitHub repository:

``` bash
cd path/to/Project
git init
git status
git add .
git status
git diff --cached
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/your-username/example.git
git push -u origin main
```

Replace the directory and repository URL with your actual values.

### What does each command do?

  -----------------------------------------------------------------------
  Command                             Explanation
  ----------------------------------- -----------------------------------
  `git init`                          Initializes the local repository

  `git status`                        Shows untracked, modified, staged,
                                      and other relevant states

  `git add .`                         Stages eligible changes under the
                                      current directory

  `git diff --cached`                 Reviews the staged changes

  `git commit -m "Initial commit"`    Records the staged snapshot locally

  `git branch -M main`                Renames the current branch to
                                      `main`

  `git remote add origin <url>`       Adds a named remote connection

  `git push -u origin main`           Pushes the branch and sets its
                                      upstream
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# 20. Undoing or correcting changes

Git provides several ways to undo work. Choose based on whether the
change is unstaged, staged, committed, or already pushed.

## 20.1 Rename or move a file

``` bash
git mv old_name.py new_name.py
```

This moves or renames the file and stages the change. Git detects
renames by comparing file content; it does not store a special rename
operation as an independent object.

## 20.2 Delete a tracked file

``` bash
git rm old_file.py
```

This removes the file from the working tree and stages its removal.

## 20.3 Stop tracking a file but keep it locally

``` bash
git rm --cached data.db
```

This removes the file from the staging index while leaving the working
copy in place. Commit the change to record the removal from the
repository's tracked state.

## 20.4 Unstage a file

``` bash
git restore --staged app.py
```

This removes the staged version from the index while preserving the
working-tree changes.

## 20.5 Discard unstaged edits

``` bash
git restore app.py
```

**Warning:** This discards unstaged changes to the specified file. Make
sure you do not need them.

## 20.6 Undo a commit by creating a new commit

``` bash
git revert <commit-id>
```

This creates a new commit that reverses the changes introduced by the
target commit, where possible. It is often appropriate for changes that
have already been shared with others.

## 20.7 Reset a branch to an earlier commit

``` bash
git reset --soft <commit-id>
git reset --mixed <commit-id>
git reset --hard <commit-id>
```

-   `--soft`: moves the current branch reference; changes from the
    removed commits remain staged.
-   `--mixed` (the default): moves the branch and resets the index;
    changes remain in the working tree.
-   `--hard`: resets the branch, index, and working tree. **Uncommitted
    work can be lost.**

Reset changes history for the current branch. Be especially careful when
the commits have already been pushed or shared. Prefer `git revert` for
many shared-history corrections.

------------------------------------------------------------------------

# 21. Common mistakes and troubleshooting

## Mistake 1: `git commit` says there is nothing to commit

Possible reason: changes have not been staged, or the working tree is
already clean.

Check:

``` bash
git status
git add <file>
git commit -m "Describe the change"
```

## Mistake 2: A new file was not included by `git commit -am`

`-am` does not stage untracked files.

Fix:

``` bash
git add new_file.py
git commit -m "Add new file"
```

## Mistake 3: A file is still tracked even though it is in `.gitignore`

`.gitignore` does not automatically untrack committed files.

Fix, if the intention is to stop tracking it while keeping the local
file:

``` bash
git rm --cached <file>
git commit -m "Stop tracking local file"
```

## Mistake 4: `fatal: remote origin already exists`

Inspect the current remote:

``` bash
git remote -v
```

If you need to change the URL:

``` bash
git remote set-url origin <correct-url>
```

## Mistake 5: Push is rejected because the remote contains commits you do not have

First inspect your status and history. If the remote has a README or
another initial commit, you may need to fetch and integrate its history.

For example, when appropriate:

``` bash
git fetch origin
git log --oneline --graph --decorate --all
```

Then decide whether to merge or rebase. Do not blindly force-push,
particularly to a shared branch.

## Mistake 6: Merge conflict

``` bash
git status
```

Edit the conflicted files, resolve the content, stage them, and complete
the merge. If you want to cancel a merge that is still in progress,
`git merge --abort` may help:

``` bash
git merge --abort
```

## Mistake 7: Accidentally committed a secret

1.  Revoke or rotate the exposed key or credential immediately.
2.  Remove it from the current code and prevent future accidental
    additions.
3.  If necessary, follow your hosting provider's process for removing it
    from history.
4.  Remember that collaborators, clones, logs, or caches may still
    contain the exposed value.

Simply deleting the file in a later commit does not erase it from
earlier history.

## Mistake 8: Authentication failure when pushing

Check that the remote URL is correct and that you have permission to
push. Use the authentication method supported by your Git hosting
provider, such as a credential manager, browser sign-in, access token,
or SSH key.

------------------------------------------------------------------------

# 22. Git command cheat sheet

## Setup

``` bash
git --version
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --list
```

## Create or copy a repository

``` bash
git init
git init <directory>
git clone <url>
```

## Check and stage changes

``` bash
git status
git add <file>
git add .
git add -A
git add -p
```

## Commit

``` bash
git commit -m "Describe the change"
git commit -am "Describe tracked-file changes"
```

## Inspect history and changes

``` bash
git log
git log --oneline
git log --oneline --graph --decorate --all
git show <commit-id>
git diff
git diff --cached
git diff <commit1-id> <commit2-id>
git log --stat -M
git log --follow -- <file>
```

## Branches

``` bash
git branch
git branch -r
git branch -a
git branch <branch-name>
git switch <branch-name>
git switch -c <branch-name>
git branch -d <branch-name>
git branch -D <branch-name>
```

## Merge

``` bash
git switch main
git merge <branch-name>
git merge --squash <branch-name>
```

## Tags

``` bash
git tag
git tag <tag-name>
git tag -a v1.0.0 -m "Release version 1.0.0"
git show v1.0.0
git tag -d <tag-name>
git push origin v1.0.0
```

## Remotes and synchronization

``` bash
git remote
git remote -v
git remote add origin <url>
git remote set-url origin <url>
git remote remove origin
git fetch origin
git pull
git pull --rebase origin main
git push origin main
git push -u origin main
```

## Undo or correct changes

``` bash
git restore <file>
git restore --staged <file>
git revert <commit-id>
git reset --soft <commit-id>
git reset --mixed <commit-id>
git reset --hard <commit-id>
git rm <file>
git rm --cached <file>
git mv <old-path> <new-path>
```

------------------------------------------------------------------------

# 23. Practice exercises

Try the exercises in a temporary practice directory. Avoid experimenting
with destructive commands in an important project.

## Exercise 1: Create your first repository

1.  Create a directory called `git-practice`.
2.  Initialize Git.
3.  Create a file called `README.md`.
4.  Stage and commit the file.
5.  View the commit history.

Useful commands:

``` bash
mkdir git-practice
cd git-practice
git init
echo "# Git Practice" > README.md
git status
git add README.md
git commit -m "Add project README"
git log --oneline
```

## Exercise 2: Understand staging

1.  Create `app.py`.
2.  Stage it.
3.  Modify it again after staging.
4.  Run `git status` and `git diff`.
5.  Stage the latest version and inspect `git diff --cached`.
6.  Commit.

Goal: understand that the staging area and working tree can contain
different versions of the same file.

## Exercise 3: Add a `.gitignore`

1.  Create a `logs` directory.
2.  Create a file ending in `.notes`.
3.  Add `logs/` and `*.notes` to `.gitignore`.
4.  Run `git status`.

Goal: observe which untracked files Git ignores.

## Exercise 4: Use branches

1.  Create a branch named `feature-readme`.
2.  Switch to it.
3.  Edit `README.md`.
4.  Commit the change.
5.  Switch back to `main`.
6.  Merge the feature branch.

Goal: understand isolated work and integration.

## Exercise 5: Inspect history

Run these commands and explain what each one shows:

``` bash
git log --oneline
git show HEAD
git diff
git diff --cached
```

## Exercise 6: Create a release tag

1.  Create an annotated tag named `v1.0.0`.
2.  Inspect it.
3.  List all tags.

``` bash
git tag -a v1.0.0 -m "Release version 1.0.0"
git show v1.0.0
git tag
```

## Exercise 7: Push to GitHub

1.  Create an empty repository on GitHub.
2.  Add it as `origin`.
3.  Push your `main` branch.
4.  Make another local commit and push again.
5.  Check that the new commit appears on GitHub.

------------------------------------------------------------------------

# Final mental model

Remember these core ideas:

-   **Git** tracks project history.
-   **GitHub** hosts repositories and provides collaboration tools.
-   **Working directory** is where you edit files.
-   **Staging area** selects what goes into the next commit.
-   **Commit** records a local snapshot.
-   **Branch** lets you develop a line of work separately.
-   **Merge** combines work from branches.
-   **Tag** marks a specific commit, often for a release.
-   **Remote** is a named connection to another repository.
-   **Fetch** downloads remote history without automatically integrating
    it into your current branch.
-   **Pull** fetches and integrates remote changes.
-   **Push** uploads eligible commits.
-   **`.gitignore`** helps prevent specified untracked files from being
    added, but does not untrack files already committed.

A useful everyday cycle is:

``` text
Edit → git status → git add → git diff --cached
     → git commit → git pull/fetch as needed → git push
```

The exact order depends on whether you are working alone, collaborating,
or starting from an existing remote repository. Check `git status`
frequently, review staged changes before committing, and be cautious
with commands that rewrite history or discard work.

**Happy learning!**
