# pytests for the libgit library
import libgit
import os
import pytest
# test whether you can use the init command
def test_main():
    pass

def test_init():

    path = os.path.abspath(".")
    print(path)
    git = ".git"
    assert os.path.exists(os.path.join(path, git))
    git = os.path.join(path, git)
    assert os.path.exists(os.path.join(git, "objects"))
    assert os.path.exists(os.path.join(git, "refs/heads"))
    assert os.path.exists(os.path.join(git, "refs/tags"))
    assert os.path.exists(os.path.join(git, "HEAD"))
    assert os.path.exists(os.path.join(git, "config"))
    assert os.path.exists(os.path.join(git, "description"))

# test whether the we can find the git repostiroy from a given path
def test_repo_find():
    path = "/home/ubuntu/pythongitworkingspace"

    assert libgit.repo_find(path) == path

    path = "/home/ubuntu"

def test_invalid_repo_find():
    path = "/home/ubuntu"
    with pytest.raises(Exception) as exp:
        libgit.repo_find(path)
    assert str(exp.value) == "No git repository found"


    
