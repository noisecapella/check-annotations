__author__ = 'schneg'

import os

from paths import make_paths, group

from logilab.astng import builder
from logilab.astng.utils import ASTWalker
abuilder = builder.ASTNGBuilder()

class ModuleTree:
    def __init__(self, root):
        self.modules = {}

        if os.path.isfile(root):
            basedir, _ = os.path.split(root)
            basedir = os.path.abspath(basedir)
            paths = [os.path.abspath(root)]
        elif os.path.isdir(root):
            basedir = os.path.abspath(root)
            paths = make_paths(root)

        relative_paths = group(basedir, paths)

        for abs_path, rel_path in relative_paths.items():
            with open(abs_path) as f:
                code = f.read()
            module_path = rel_path.replace("/", ".").replace("-", "_")
            if module_path.endswith(".py"):
                module_path = module_path[:-len(".py")]

            tree = abuilder.string_build(code, modname=module_path)
            self.modules[module_path] = tree
