# greet.py
import sys

def greet(name):
    print(f"Hello, {name}!\nWelcome to DevOps learning.\nAuthor - Sandeep Siyadri")

if __name__ == "__main__":
    args = sys.argv[1:]
    if args:
        greet(args[0])
    else:
        greet("There")