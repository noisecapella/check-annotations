#!/usr/bin/env python3

import argparse
import os
import os.path

from logilab.astng import builder
from logilab.astng.utils import ASTWalker
from logilab.astng.scoped_nodes import Module

from logilab.astng.as_string import dump

from paths import (
    group,
    make_paths,
)

abuilder = builder.ASTNGBuilder()

class PrintAll:
    def set_context(self, node, child_node):
        pass

    def visit_module(self, node):
        print(node.as_string())

def print_module_code(module_path, tree):
    print("In path %s" % module_path)
    ASTWalker(PrintAll()).walk(tree)

def print_module_tree(module_path, tree):
    print("In path %s" % module_path)
    print(dump(tree))

def check(module_path, tree):
    print("In path %s" % module_path)
    #TODO

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
            tree = abuilder.string_build(code)
            module_path = rel_path.replace("/", ".")
            self.modules[module_path] = tree


def main():
    parser = argparse.ArgumentParser(description='Statically check types for consistency')
    parser.add_argument('path', type=str, help='path to directory containing Python files,'
                                               ' or a path to a single Python file')
    parser.add_argument("--print-code", action='store_true')
    parser.add_argument("--print-tree", action='store_true')
    args = parser.parse_args()

    module_tree = ModuleTree(args.path)
    if args.print_code:
        for module_path, tree in module_tree.modules.items():
            print_module_code(module_path, tree)
    elif args.print_tree:
        for module_path, tree in module_tree.modules.items():
            print_module_tree(module_path, tree)

if __name__ == "__main__":
    main()