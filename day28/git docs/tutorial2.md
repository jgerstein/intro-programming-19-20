# Git Part 2

## Cloning

Last class, you created a repository locally (on your own computer), and then pushed it to GitHub. This time, we'll do the opposite. When you accepted the GitHub Classroom assignment, it created a remote repository. Now you need to **clone** it to create your local repository.

1. Go to your repository on [GitHub](http://github.com).
2. Copy the URL for your repository. This is not identical to the URL in the address bar. You can get the URL by clicking the "Clone or Download" button in the top right and copying the HTTPS (not SSH!) URL.
3. Open VS Code if you haven't already, and open the terminal with <kbd>ctrl</kbd> + <kbd>`</kbd>
4. Whatever directory is showing in your command prompt is where the repository will be copied. I strongly recommend either the "Documents" folder or the "GitHub" folder. Navigate to one of those. If you need help, I can help you.
    * To navigate up a level:
        ```
        $ cd ..
        ```
    * To navigate into a folder inside your current one:
        ```
        $ cd <foldername>
        ```
    * To see what folders are inside your current one:
        ```
        $ ls
        ```
    * To be really lazy and not have to think about this, find the folder using Windows Explorer (which is not IE!), right click on the address in the address bar, and choose "Copy address as text". You can now paste that in as the folder you want to navigate to and it will navigate directly there
5. Clone your repository:
    ```
    $ git clone <URLforyourrepo>
    ```
6. In VS Code, open the folder for your repo so your command line automatically opens in the right directory and so you can see your files easily.
---
## Python

Follow the directions in README.md for your repository to run your code. Don't forget that you'll need to install Pygame - directions are in the README. We'll look together at how the code works.
---
## Branching

Branching will let you work on additional features or fixes without affecting whatever stable code you have in master. 

Some common commands:

* `git branch` will show you what branches you have
* `git checkout <branch>` lets you change which branch is active
* `git checkout -b <branch>` adds an option that lets you create a branch and immediately switch to it
* `git push --set-upstream origin <branch>` creates the branch in your remote repository, links it to your local one, and pushes to it. This is necessary the first time you push if you create the branch locally, but not if you create it remotely.

When you switch branches, the files on your computer will actually change to reflect the state of whatever branch you currently have active. When you create a branch, it splits off from whatever branch is currently active. This means that you can branch off of branches other than master.

1. Create a branch called change-pic and make it your active branch
    ```
    $ git checkout -b change-pic
    ```
2. Find a new image you want to replace `ball.png` with, and put it in the image folder. For your own sanity, I recommend a short name for the file.
3. Modify your code to replace `ball.png` with your image.
4. Run your code to test it
5. When it works, stage and commit your changes. Remember that `git status` can show you the current status of your repository, `git add <filename>` can add a file to what will be staged, and `git commit -m "<commit message>"` will create a commit
6. Push to origin with:
    ```
    $ git push --set-upstream origin change-pic
    ```