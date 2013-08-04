#!/usr/bin/env python3

import argparse
import os
import os.path

from astroid import builder
from astroid.utils import ASTWalker

from astroid.as_string import dump

from check import check

from module_tree import ModuleTree

abuilder = builder.AstroidBuilder()

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

def main():
    parser = argparse.ArgumentParser(description='Statically check types for consistency')
    parser.add_argument('path', type=str, help='path to directory containing Python files,'
                                               ' or a path to a single Python file')
    parser.add_argument("--print-code", action='store_true')
    parser.add_argument("--print-tree", action='store_true')
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    module_tree = ModuleTree(args.path)
    if args.print_code:
        for module_path, tree in module_tree.modules.items():
            print_module_code(module_path, tree)
    elif args.print_tree:
        for module_path, tree in module_tree.modules.items():
            print_module_tree(module_path, tree)
    elif args.check:
        check(module_tree)
    else:
        raise Exception("One option must be selected")

if __name__ == "__main__":
    main()
