__author__ = 'schneg'

from astroid import builder
from astroid.utils import ASTWalker
from astroid.exceptions import InferenceError
abuilder = builder.AstroidBuilder()

from module_tree import ModuleTree

from collections import defaultdict

def infer(node):
    try:
        return list(node.infer())
    except InferenceError:
        return ""

def join_module(a, b):
    if a:
        return a + "." + b
    else:
        return b

class MatchFunc:
    def __init__(self, path, funcs):
        self.path = path
        self.funcs = funcs
        self.imports = {}

    def set_context(self, node, child_node):
        pass
        
    def visit_from(self, node):
        for name in node.names:
            self.imports[name[0]] = node.modname

    def visit_import(self, node):
        for name in node.names:
            self.imports[name[0]] = ""

    def visit_callfunc(self, node):
        """Look for functions with the same name
        Should include imported modules and functions
        referenced from classes

        """
        TODO

class CatchFunc:
    def __init__(self, path, funcs):
        self.path = path
        self.funcs = funcs

    def set_context(self, node, child_node):
        pass

    def visit_function(self, node):
        name = join_module(self.path, node.name)

        self.funcs[(self.path, name)] = node

class PrintArg:
    def set_context(self, node, child_node):
        pass

    def visit_assname(self, node):
        print(node.as_string(), type(node), infer(node))

    def visit_callfunc(self, node):
        print(node.as_string(), type(node), infer(node))

    def visit_default(self, node):
        print(node.as_string(), type(node))


def check(module_tree: ModuleTree):
    # TODO: astroid must keep track of function information somewhere
    # we should use that instead of recording it here

    funcs = {}
    for path, tree in module_tree.modules.items():
        print()
        print("In path %s %s" % (path, tree))
        ASTWalker(CatchFunc(path, funcs)).walk(tree)

    for path, tree in module_tree.modules.items():
        print()
        print("In path %s %s" % (path, tree))
        ASTWalker(MatchFunc(path, funcs)).walk(tree)

