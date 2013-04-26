#!/usr/bin/env python3
"""Annotations"""

from logilab.astng import builder
from logilab.astng.utils import ASTWalker
from logilab.astng.scoped_nodes import Function

abuilder = builder.ASTNGBuilder()


class PrintFunctions:
    """Print functions"""
    def set_context(self, node, child_node):
        pass

    def visit_function(self, node: Function):
        """Print function definitions"""

        print()
        print(node)
        print(node.args)

        #def get_annotation(annotation : str) -> str:
        #    if annotation:
        #        return ast.dump(annotation)
        #    else:
        #        return "None"
        #annotations = [get_annotation(argument.annotation) for argument in node.args.args]
        #print("%s" % ", ".join(annotations), end=")\n")

class Handler:
    def set_context(self, a, b):
        pass

def main():
    """Hello world"""
    with open("example_module.py") as this_file:
        code = this_file.read()

    p = abuilder.string_build(code)
    handler = PrintFunctions()
    ASTWalker(handler).walk(p)

if __name__ == "__main__":
    main()

