# pythongit

This projects refernceces the article made by [Thibault Polge](https://wyag.thb.lt/#org947aee7)

Goal: was to better understand the inner workings of git by implementing by own version using python

## Features to Implement

- add
- cat-file
- checkout
- commit
- hash-object
- init
- log
- ls-tree
- merge
- rebase
- rev-parse
- rm
- show-ref
- tag

## Using the program

```
chmod +x pythongit
```

## Commands

### init

Creates a empty .git repository

- subdirectories
  - .git/objects
  - .git/refs/heads
  - .git/refs/tags
  - .git/config
- An initial branch without any commits will be created
- If a path is not specified, the base of the repository is ./.git
- Running init in an existing repository is safe

### add

### tag

## Virtual environment

### Install a virtual environment

```
python3 -m pip install --user virtualenv
```

### Creating a virtual environment

Go to your project's directory then run

```
python3 -m venv .venv
```

venv will create a virtual python installation in the env folder
\*\* the virtual environment needs to be excluded from the virtual control system

### Activating a virtual environment

Before you can start install or using packages in your virtual environment you need to activate it

```
source env/bin/activate
which python
```

### Leaving the virtual environment

simply run

```
deactivate
```
