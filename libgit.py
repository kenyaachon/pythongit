import argparse
import configparser
import os
import configparser

class GitRepository(object):
    def __init__(self, path):
        self.worktree = path
        self.gitdir = os.path.join(path, ".git")

        #Read configuration file in .git/config
        #sthe config file is an INI file
        self.config = configparser.ConfigParser()

    def repo_file(self, path, mkdir=False):
        
        if self.repo_dir(*path[:-1], mkdir=mkdir):
            return self.repo_path()

    def repo_dir(self, *path, mkdir=False):
        path = self.repo_file(*path)


        #check if the path is a directory


        #check if I need to make a directory

    def repo_default_config(self):
        pass

    def repo_path(self, *path):
        return os.path.join(self.gitdir, *path)


def repo_create(path):
    pass
        

#create an empty Git repository
def init():
    print("hello")
    print("hello there")


def main():
    
    parser = argparse.ArgumentParser(description='reimplementating of git system')
    
    parser.add_argument("command", nargs='+')
    args = parser.parse_args()
    print(args)

    if args.command[0] == 'init': init()
    






if __name__=="__main__":
    main()