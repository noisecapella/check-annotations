__author__ = 'schneg'

import os.path

from types import GeneratorType

def make_paths(path: str) -> GeneratorType:
    """returns a collection of python file paths which exist in a directory.
    If 'path' is just that file, just that file is returned"""

    if os.path.isfile(path):
        yield os.path.abspath(path)
    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".py"):
                    yield os.path.abspath(os.path.join(root, file))
    else:
        raise Exception("%s is not a directory or a file" % path)

def group(basedir: str, paths: GeneratorType) -> dict:
    """returns a relative path (relative to basedir) for each path in paths"""
    ret = {}

    basedir = os.path.abspath(basedir)
    if basedir.endswith("/"):
        basedir = basedir[:-1]

    for path in paths:
        path = os.path.abspath(path)
        commonprefix = os.path.commonprefix([path, basedir])
        if basedir != commonprefix:
            raise Exception("Expected commonprefix = %s, but basedir was %s" % (commonprefix, basedir))
        suffix = path[len(commonprefix):]
        if suffix.startswith("/"):
            suffix = suffix[len("/"):]
        ret[path] = suffix
    return ret