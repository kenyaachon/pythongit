# pytests for the libgit library
import libgit
import os
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




    
