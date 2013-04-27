import argparse
import os
import os.path

def make_paths(path) -> list:
    """returns a collection of python file paths"""

    if os.path.isfile(path):
        yield path
    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".py"):
                    yield os.path.join(root, file)
    else:
        raise Exception("%s is not a directory or a file" % path)

def main():
    parser = argparse.ArgumentParser(description='Statically check types for consistency')
    parser.add_argument('path', type=str, help='path to directory containing Python files,'
                                               ' or a path to a single Python file')
    args = parser.parse_args()

    paths = make_paths(args.path)
    print(list(paths))

if __name__ == "__main__":
    main()