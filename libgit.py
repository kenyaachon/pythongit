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
        os.makedirs(os.path.join(path, ".git/refs/heads"))
        os.makedirs(os.path.join(path, ".git/branches"))

    except FileNotFoundError as err:
        print(err)

    # .git/description
    with open(os.path.join(path, ".git/description"), 'w') as fp:
        fp.write("Unnamed repository: edit this file 'description' to name the repository.\n")

    # .git/HEAD
    with open(os.path.join(path, ".git/HEAD"), 'w') as fp:
        fp.write("ref: refs/heads/masters\n")

    # config file
    with open(os.path.join(path, ".git/config"), 'w') as fp:
        config = configparser.ConfigParser()
        config.add_section('core')
        config.set('core', 'repositoryformatversion', '0')
        config.set('core', 'filemode', 'false')
        config.set('core', 'bare', 'false')
        config.write(fp)



def repo_find(path):
    path = os.path.realpath(path)
    if os.path.isdir(os.path.join(path, ".git")):
        return os.path.join(path, ".git")
    else:
        raise Exception("No git repository found")
   
    
    return ""
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