import argparse

def init():
    print("hello there")
def main():
    
    parser = argparse.ArgumentParser(description='reimplementating of git')
    parser.add_argument( dest="init", help="initalize the git repostitory")

    args = parser.parse_args()

    if args.init: init()

if __name__=="__main__":
    main()