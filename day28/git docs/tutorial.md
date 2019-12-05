# Git Good

## Installing Git

We're going to need to install one more thing. Go to [git-scm](https://git-scm.com/download/win), download, and install. Set your text editor to VS Code (trust me, you don't want it to be VIM, and if you do you already know and will ignore this anyway), and leave everything else on default.

## How to read this

* Variables are indicated with angled brackets. `git commit -m <commit message>` is indicating that you should replace `<commit message>` with your actual commit message
* A common convention is to indicate a command line prompt with a dollar sign. Your actual command line on UCTECH54 will most likely look something like:

    ```
    PS C:\Users\gerst\Desktop\git docs>
    ```

    But that can get really long, so it's typical to indicate the command line as simply:

    ```
    $
    ```
---
## Setup

1. Open VS Code
2. Open the terminal with <kbd>ctrl</kbd> + <kbd>`</kbd>
3. In the terminal, check that Git is installed and accessible with the following command:

    ```
    $ git --version
    ```
    
    You should see something similar to `git version 2.21.0.windows.1`. If not, ask for help
4. Check that your name and email are set up
    
    * To check that your name is set, make sure you see it when you use the following command:
    
        ```
        $ git config --global user.name
        ```
        
        If name is not set, set it with:
        
        ```
        $ git config --global user.name <your name here>
        ```
    * To check that your email is set, make sure you see it when you use the following command:
    
        ```
        $ git config --global user.email
        ```
        
        If email is not set, set it with:
        
        ```
        $ git config --global user.email <email>
        ```
---
## Create a Repository

A repository is a collection of files and folders that make up your project. Although we'll usually work with repositories I create for you through Github Classroom, in this case you're going to start by creating a repository of your own. We'll be working with the command line today, but soon I'll show you some alternate ways of working that may make some of you more comfortable. The first step can be accomplished in a lot of ways, but I'll give you two. **Please choose one of these methods, you don't need to do both!**

### GUI-based

1. Open Windows Explorer
2. Go to the `Documents` folder
3. Create a folder called `hello-world`

### Command Line

1. First, navigate to the Documents folder. You should be able to accomplish this with the following command (assuming you're at `C:\Users\<yourusername>`) right now, but if you get an error I'll help you with it.

    ```
    $ cd documents
    ```

2. Now that your current working directory is the documents folder (command prompt should look like `C:\Users\<username>\documents`), we'll create a folder to be your repository. First, you'll make a new directory called `hello-world`, and then we'll change directories into it.

    ```
    $ mkdir hello-world
    $ cd hello-world
    ```
    Now you should see your command prompt change to something like `C:\Users\<username>\documents\hello-world`. Congratulations, you used the command line to modify files on your computer!

### Setting Up Your VS Code Workspace

Regardless of whether you used the windows GUI or the command line to create your folder, we're going to make your life a whole lot easier by creating a workspace in VS code that uses this folder. In the menu bar, open the `File` menu and choose `Open Folder` (keyboard shortcut is <kbd>ctrl</kbd> + <kbd>k</kbd> <kbd>ctrl</kbd> + <kbd>o</kbd>). Select your `hello-world` folder and you'll see VS Code reload. From this point on, you'll see the files and folders in your repository in the explorer section of the sidebar, and any terminal windows opened will have this folder as the current working directory.

![clean workspace](img/clean&#32;workspace.png)

### Make it Git

Open the terminal with <kbd>ctrl</kbd> + <kbd>`</kbd> and use the following command

```
$ git init
```

You should get a response similar to `Initialized empty Git repository in <your location here>/.git/`. If you got that, you've successfully created a Git repository!

![repo created](img/repo&#32;created.png)
---
## Commit

### Create a File

We're going to create a README file. We don't really have anything particularly meaningful to say yet, so we'll use this as practice for using Markdown. Create a file in the root of your repository called `README.md` and open it in VS Code. In your file, do the following:

* Make a first level header that contains your GitHub username:

    ```
    # <your username here>
    ```
* Link to an image
    
    ```
    ![<title>](<url of your image>)
    ```
* Link to the source of your image
  
    ```
    Create a link with a [<title>](<url>)
    ```

Save your file.

### Check Status, Stage, and Commit

Checking the *status* of your repository is really important, because it shows you what changes have been made, what's been staged, and if you have things you need to commit.

1. Open the terminal <kbd>ctrl</kbd> + <kbd>`</kbd>
2. Make sure your command line shows that you're still in the hello-world directory
3. Check status
   
   ```
   $ git status
   ```

   You should see something like:

    ```
    On branch master

    No commits yet

    Untracked files:
    (use "git add <file>..." to include in what will be committed)

            README.md

    nothing added to commit but untracked files present (use "git add" to track)
    ```

    This means that you've added a file, but it won't be included at your next commit (snapshot/checkpoint) unless you stage it
4. Add your file to stage it
   
    ```
    $ git add README.md
    ```
5. Commit your changes to the repository. The `-m` option allows your to include the commit message in the command instead of having to use VIM to add it. Trust me, you don't want to use VIM.

    ```
    $ git commit -m "Created readme"
    ```

### Make Changes

1. Add another line to README.md and save.
2. Tell git to show you the *diff*erence between the current version and the version in the most recent commit with the following command:

    ```
    $ git diff
    ```

    Your output should be similar to:
    ```
    diff --git a/README.md b/README.md
    index f696c3f..3931929 100644
    --- a/README.md
    +++ b/README.md
    @@ -2,4 +2,6 @@

    ![git commits](https://imgs.xkcd.com/comics/git_commit.png)

    -Webcomic from [XKCD](https://xkcd.com/1296/)
    \ No newline at end of file
    +Webcomic from [XKCD](https://xkcd.com/1296/)
    +
    +Adding something new.
    \ No newline at end of file
    ```
3. Stage and commit your changes. You can do this in one step for files that have already been committed at least once with another *option* you can add to the `git commit` command. The `-a` option will automatically add all files that are already tracked (meaning that they've been committed at least once already). Using the command like this will look like:

    ```
    $ git commit -am "Modified README.md"
    ```
---
## GitHub Setup

Check to see if your GitHub username is already stored in your Git configuration with the first command shown below. If not, add it with the second command. Please note that the username is case sensitive

```
$ git config --global user.username
$ git config --global user.username <UserName>
```
---
## Remote Repository

### Create the Repo

First, we'll create a remote repository to connect to.

1. Log in to [GitHub](http://github.com), click the '+' in the top right corner, and click 'New Repository'
2. Name your new repository the same thing as your local-repository (`hello-world`) and give it a short description.
3. Don't initialize it with a README because we've already created one.
4. Leave everything else on default.
5. Create the repository!

### Connect Local to Remote

1. At the top of the page for your remote repository, you'll see a URL listed for your repo. Copy that URL, making sure you copy the HTTPS version, not the SSH version.
2. Go back to the terminal. We're going to tell Git where the remote repo is stored. We'll name your remote repo `origin`, which is the name typically used. I *think* the first version of the command below will work for you, but I'm not sure because I can't test from your logins. If it doesn't work, use the second one.

    ```
    $ git remote set-url origin <GITHUBURL>
    $ git remote add origin <GITHUBURL>
    ```

### Push

Next you'll send everything you've done to the remote repository. The command to do this is usually `git push`, but in this case because it's the first time you're actually connecting to the remote repository, you'll need to use:

```
$ git push --set-upstream origin master
```

Check to make sure it pushed correctly by viewing your repository on [GitHub](http://github.com).