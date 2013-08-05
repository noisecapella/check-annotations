#!/usr/bin/env python3

import argparse
import os
import os.path

from astroid.manager import AstroidManager
from astroid.utils import ASTWalker

from astroid.as_string import dump

from lib.check import check

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

    path = args.path
    manager = AstroidManager()
    node = manager.ast_from_file(path)
    
    if args.print_code:
        print_module_code(args.path, node)
    elif args.print_tree:
        print_module_tree(args.path, node)
    elif args.check:
        check(args.path, node)
    else:
        raise Exception("One option must be selected")

if __name__ == "__main__":
    main()
