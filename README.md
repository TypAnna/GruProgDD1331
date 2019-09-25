# Grundläggande Programmering DD1331
Repository for the course DD1331 (Fundamentals of Programming in Python) consisting of slides, solved exercises and things that are good to know when starting your programming journey.

# Golden rules to program by :unicorn:
* Draw a (high level) diagram of what your program needs to do.
    - Don't worry about exactly **how** you need to write it (the syntax).
* Use variable names that are easy to understand and makes sense.
* Always leave your code in a state that is easy to come back to.
    - A good rule of thumb is to ensure that one of your classmates should be ables to understand what your code does.
* Divide your program to the most elementary parts and start with them.
    - Ensure that each component works as it should before moving on.
* If a method and what it does cannot be described in a sentence - then it is too long!
* Think about what could go wrong and handle edge cases.

## Reusing code
Reuse code as much as you can, and keep the duplication of code to a minimum. This reduces the amount of bugs, and makes the code easier to read.

Reuse code by writing functions and classes. To use a function from one file in another file, we can import that file/function. Say we we have a file `approximations.py` with the function `approxSin()` in it. We have another file (in the same directory) called, let's say, `drawGraphs.py` in which we want to use `approxSin()`. We can then, in the top of the `drawGraphs.py`-file write `from approximation import approxSin`. We can that use `approxSin()` as we please.

Another option would be to write `import approximation`. To use the `approxSin()` function, we would then instead need to write `approximation.approxSin()` to use the method.

# Steps to follow when you are stuck
1. Insert prints to see what the program actually does.
    - Draw - step by step - what your program does
2. Explain to a friend (or a [rubber duck :duck:](https://en.wikipedia.org/wiki/Rubber_duck_debugging)) what your program does (or should do...) - step by step.
    - You will be amazed by how many bugs/problems can be solved this way!
3. Write tests for your program

# Git & GitHub basics
Git is a version control system which you install locally on your computer. It enables you to manage your projects source code and its history. GitHub is an online tool based around Git which creates a remote repository where you can upload (push) code to, to make it available to others. You can use Git without GitHub, but not GitHub without Git.

## Git commands
In order for git commands to make sense, you need to be in the correct directory (i.e. a git repo). If you are not there, navigate to the correct place using `cd`. Once there, the most common commands you will use are
- `git status`: gives you information about what branch you are on, what (if any) files have been edited, and what files that have been staged (added).
- In order to save your files to the remote repository on GitHub, you need to do the following:
    1. `git add <filename>`: tells git to add the specified file to the batch that is to be commited.
    2. `git commit -m "Information about what has been done" `: records changes to the repository and stores the locally.
    3. `git push origin master`: acutally pushes all the files added to the commit to your remote repository on GitHub.
- `git pull`: fetches the most recent version of your repo
