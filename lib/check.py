__author__ = 'schneg'

from astroid import builder
from astroid.utils import ASTWalker
from astroid.exceptions import InferenceError
abuilder = builder.AstroidBuilder()

from collections import defaultdict

def infer(node):
    try:
        return list(node.infer())
    except InferenceError:
        return ""

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


def check(path : str, node):
    # TODO: astroid must keep track of function information somewhere
    # we should use that instead of recording it here

    funcs = {}
    print("In path %s %s" % (path, node))
    ASTWalker(CatchFunc(path, funcs)).walk(node)

    print("In path %s %s" % (path, node))
    ASTWalker(MatchFunc(path, funcs)).walk(node)

