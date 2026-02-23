---
title: Setting up and Managing Python Environments
author: "[Thomas (Tom) C. Gorordo](https://pages.uoregon.edu/tgorordo) - your TA"
date: 2024-10-01
lang: en
...

To help you get started/possibly avoid at least some tech support/give some advice here's a brief note on Python development environments. 

So, welcome to the zoo that is software configuration!

![standards.png](https://imgs.xkcd.com/comics/standards.png)

### POSIX Shells and Environments

It won't come up very often in the course assignments themselves, but for tech support I will generally assume you have access to
a [POSIX](https://en.wikipedia.org/wiki/POSIX) compliant shell (command-line) somewhere on your 
machine. If you're using a Linux or Mac operating system
your default shell is likely [`bash`](https://www.gnu.org/software/bash/) or 
[`zsh`](https://zsh.sourceforge.io/) (or some variant or equivalent thereof accessible through some kind of 'terminal' program), in which case you should be good-to-go. 
If you're on Windows things may be more complicated - 
I'm not very up to speed on the current state of [powershell](https://learn.microsoft.com/en-us/powershell/) -
but I can recommend looking into the [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/), 
or [`git-bash`](https://gitforwindows.org/), and/or [CygWin](https://www.cygwin.com/) 
as ways to get a \*nix-like environment on Windows that I'll be able to help with.

You may also want an editor like [Visual Studio Code](https://code.visualstudio.com/) or [Spyder](https://www.spyder-ide.org/) - though there are many other valid choices for writing/editing your software for this course.
(if you really want to be a shell guru there's always the likes of [neovim](https://neovim.io/);
beware the learning curve.)

You're welcome to set up your technology stack however you'd like, but I can't guarantee I'll be able to debug anything 
or replicate your environment faithfully when testing your assignments if you deviate too far from modern Linux dev standards and/or common software (I can help with MATLAB or Julia as well as Python - this guide just anticipates Python will be the most common language choice, and that MATLAB is more self-contained/explanatory).

### Getting and Using Python

If you don't have it already in some form, you should [download and install Python3](https://www.python.org/downloads/) for your system. 
You'll also, at a minimum, need to be able to [install packages](https://packaging.python.org/en/latest/tutorials/installing-packages/) (<-- READ THIS LINK if you're at all unsure about what is needed. If you have [`pip`](https://pypi.org/project/pip/) you're good to go with respect to this step).
There are some alternative ways of getting/using python (e.g. [`conda`](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html)) - 
but this note will focus on a pretty generic workflow that should be compatible with essentially *any* up-to-date system-level python installation.

Depending on your operating system, it might be more appropriate to use a package manager like 
[`apt`](https://ubuntu.com/server/docs/package-management) (for Debian Linux derivatives like Ubuntu - others for other distros),
[homebrew](https://brew.sh/) (for MacOS), or 
[winget](https://learn.microsoft.com/en-us/windows/package-manager/winget/install?source=recommendations)/[chocolatey](https://chocolatey.org/) (for Windows) 
instead of downloading and running the installer linked above.
Detailed installation instructions will vary a lot by OS, so I won't provide them here - learning how/where to look up system specific ways to do things 
 (and getting familiar with your machine and customizing it to your liking) is an important skill to develop, but you'll mostly have to find favorite resources and methods yourself over time.

### Dependency Management

We'll often want our code to depend on various external libraries rather than implement *everything* from scratch ourselves (even though that is often necessary or useful - there are situations we won't want to reinvent the wheel and where a better solution than we could write in a reasonable amount of time/effort exists). 
The default Python package manager is [`pip`](https://pypi.org/project/pip/) (there are others: [`conda`](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html) 
is quite popular and handles some of the virtual environment features mentioned below - 
there's also [`poetry`](https://python-poetry.org/), or I am personally partial to [`uv`](https://docs.astral.sh/uv/).
Each work a bit differently, so we'll just cover a barebones python workflow here).

Python projects often list their 'dependencies' in a `requirements.txt` with contents like:
```
jupyter
numpy
matplotlib
pandas
scipy
simpy
```

(some of these are dependencies that will come up in the course  - relatively recent versions of each should all work identically well so this list does not specify version numbers [but if you need to lock specific version number down you can do so](https://pip.pypa.io/en/stable/reference/requirements-file-format/)). Given such a file you can install the dependencies for a project into the active environment (usually a venv - see below) via `pip`:

```bash
pip install -r requirements.txt
```

modules can also be installed explicitly by name:

```bash
pip install numpy scipy
```

(Depending on many OS particulars and settings, you may run into permission issues with these commands - let me know if you need help tracking down how to solve them for your particular setup.)

If `pip` is only present in your python installation but not exposed to your commandline you may need to use

```bash
python -m pip <remainder of the pip command goes here...>
```

### Virtual Environments
It can be important to manage dependencies carefully across projects and over time.
For example, suppose you write some code for this course which relies on some specific feature of the current version `numpy1.22` (you might use a particular niche function or rely on a name or shape for some arguments).  
Two or three years from now the latest `numpy` version might change the name(s) or interface of the feature you used - and your code will stop working! 
If you want to run your old code you'll need to use an older version of `numpy`, but that may be difficult if you have some newer project that wants to rely on the newer version of the library. 
While you can ask `pip` to install any version of a library you want at any time (and store a list of required versions in a `requirements.txt`), 
uninstalling and re-installing different versions of libraries all the time is messy and liable to break something (especially if you need to manage multiple libraries this way).

![workflow.png](https://imgs.xkcd.com/comics/workflow.png)

The somewhat standard solution to this kind of problem is a "virtual environment" - rather than rely on our global shell environment to keep track of all our projects somehow (hoping nothing winds up incompatible), 
we'll manage an independent environment for each project.

Simple dependency management via a virtual environment can be done entirely with `python` and `pip` using the [`venv`](https://docs.python.org/3/library/venv.html) module - in your shell, in some directory relevant to your project(s) invoke:

```bash
# use the python venv module 
# to make a new virtual environment stored in the env dir 
python -m venv env 
```

to create a new virtual environment. You can then activate the environment 
(tell your shell it should use the contained version of python and associated libraries) anytime you want to use it by calling:

```bash
source env/bin/activate # run the activation script located in the env dir
```

Your shell will then use a self-contained version of `python` and any libraries you install with `pip` while in this mode.
I recommend using a `venv` of some kind while working on this course - 
at the very least it will give you a place to experiment without mucking up your global python installation.

You can leave the virtual environment at any time by calling `exit`.

### All-together: an example
Suppose you want to run a local [`jupyter`](https://jupyter.org/) notebook for yourself - say, to play around a bit and get some ideas ready for an assignment that will require some [`numpy` functions](https://numpy.org/doc/2.1/reference/index.html#reference) and [`matplotlib`](https://matplotlib.org/stable/api/index.html) plotting - but don't yet have anything set up other than your global python installation.
Here's a basic workflow using the methods described above:

1) Set up a working directory along the lines of
```bash 
# make a directory for the course and "change directory" (cd) into it
mkdir uoph410-510_image-analysis && cd uoph410-510_image-analysis 

# create a virtual environment for the course and activate it 
# in the currently open session with your shell (not persistent)
python -m venv env && source ./env/bin/activate 
```

2) Install the prerequisite packages (in the venv):
```bash
pip install jupyter numpy matplotlib
```
It can be convenient to append these to a `requirements.txt` in case you want to send anyone else your code (you shouldn't send a `venv` directory - they're not portable between systems).
```bash
# create the .txt, ask pip for its requirements, 
# and "pipe" (>>) the text output from pip into the end of the file
touch requirements.txt && pip freeze >> requirements.txt 
```

4) Launch `jupyter notebook` & navigate creating a new `.ipynb` in the browser interface.

5) Voila! Notice that installing a new shell command for interacting with python (`jupyter`) could be managed in the same way as a package providing a library you can use in your code. Both are only enabled locally, and temporarily in the current session without polluting your global environment (you won't have any issues in the future anywhere else on your machine because of any software we just installed).  If you have dependency issues, just shut down the notebook (`CTRL-C` in the running terminal) and repeat (2), adding any packages that are throwing various "not found" errors.

**Note:** `jupyter` is *not* required (nor even really emphasized) in this class - but it can still be a useful tool for quick sanity-checks and pretty-printed tests or document preparation.
Generally this course will prefer you to write your code in a more modular fashion than `jupyter`'s [stateful](https://en.wikipedia.org/wiki/State_(computer_science)) environment encourages, i.e. you should structure and think of your code overall as [module/library development](https://learn.scientific-python.org/development/) rather than each assignment a one-off notebook.
(Though an optional workflow can be to develop your own module, and import it into a notebook for use with particular values). 

## Additional Considerations

The guide above covers just a very basic python environment and workflow. 
For a more featureful development experience you may want to do your own research on (in addition to some of the things scattered above):

- Linters like [ruff](https://docs.astral.sh/ruff/) or [black](https://black.readthedocs.io/en/stable/), which help you ensure your code is written in a consistent style - to help with readability.

- Unit testing with [pytest](https://docs.pytest.org/en/8.0.x/) or [`unittest`](https://docs.python.org/3/library/unittest.html) (along with *many* plugins for each/either). 
  In particular, you might find [ipytest](https://jupyter-tutorial.readthedocs.io/en/stable/notebook/testing/ipytest.html) useful for checking that your code is behaving as you expect 
  while you develop your solutions.

- Type checkers like [mypy](https://www.mypy-lang.org/) or [pyright](https://microsoft.github.io/pyright/#/), while python does not have static typing 
  (the [interpreter](https://en.wikipedia.org/wiki/Interpreter_(computing)) does not know the [type](https://en.wikipedia.org/wiki/Data_type) of an object [before](https://en.wikipedia.org/wiki/Compile_time) [runtime](https://en.wikipedia.org/wiki/Execution_(computing)#Runtime)) - there is some loose tooling available to help you try to structure your code in a type-safe 
  (or at least [duck-typed](https://en.wikipedia.org/wiki/Duck_typing)) - and more likely to be correct - way. These tend to integrate well with testing frameworks mentioned in the last bullet.

- You may want to manage a version-controlled [git](https://git-scm.com/) repository for your work on the course. Git and [Github](https://github.com/) are ubiquitous in modern software development.
  While we won't cover their use in this course, privately managing your work with these tools would be excellent practice.

Good luck, have fun, don't die!


(page [raw pandoc `.md`](setup.md), [github repo](https://github.com/tgorordo/pages.uoregon.edu))
