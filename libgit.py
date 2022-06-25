import argparse
import configparser
import os
import configparser
from tempfile import TemporaryFile

class GitRepository(object):
    def __init__(self, path):
        self.worktree = path
        self.gitdir = os.path.join(path, ".git")

        #Read configuration file in .git/config
        #sthe config file is an INI file
        self.config = configparser.ConfigParser()
        

#create an empty Git repository
def init(args):
    print(args)
    print("hello there")

    #check if the directory exists
    path = os.path.abspath(".")
    if (args.path):
        path = os.path.abspath(args.path)
        git = os.path.join(path, ".git")
        if(os.path.exists(git)):
            print("path exists")
            print(git)
            return None

    #make the git directory
    try:
        print("making the directory")
        os.makedirs(os.path.join(path, ".git/objects"))
        os.makedirs(os.path.join(path, ".git/refs/tags"))
        os.makedirs(os.path.join(path, ".git/refs/head"))
        os.makedirs(os.path.join(path, ".git/branches"))

    except FileNotFoundError as err:
        print(err)


def main():

    parser = argparse.ArgumentParser(description='reimplementating of git system')
    subparsers = parser.add_subparsers(help='git commands')

    #init
    parser_init = subparsers.add_parser('init', help='create empty git repository')
    parser_init.add_argument('--path', help="the path of the desired directory")
    parser_init.set_defaults(func=init)

    #parse command line and call whatever function was selected
    args = parser.parse_args()
    args.func(args)



    






if __name__=="__main__":
    main()