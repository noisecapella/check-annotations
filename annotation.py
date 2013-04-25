#!/usr/bin/env python3
"""Annotations"""


def func(num1: int,
         num2: int) -> int or None:
    """Add two numbers"""
    return num1 + num2

import ast


class PrintFunctions(ast.NodeVisitor):
    """Print functions"""
    def visit_FunctionDef(self, node: ast.FunctionDef):
        """Print function definitions"""

        print()
        for subnode in node.body:
            PrintFunctions().visit(subnode)

        print("def %s(" % node.name, end="")

        def get_annotation(annotation : str) -> str:
            if annotation:
                return ast.dump(annotation)
            else:
                return "None"
        annotations = [get_annotation(argument.annotation) for argument in node.args.args]
        print("%s" % ", ".join(annotations), end=")\n")


def main():
    """Hello world"""
    with open("example_module.py") as this_file:
        code = this_file.read()

    p = ast.parse(code)
    PrintFunctions().visit(p)

if __name__ == "__main__":
    main()

