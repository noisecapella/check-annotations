__author__ = 'schneg'

from astroid import builder
from astroid.utils import ASTWalker
from astroid.exceptions import InferenceError
from astroid.inference import InferenceContext, CallContext
abuilder = builder.AstroidBuilder()

from collections import defaultdict

def infer(node):
    try:
        return list(node.infer())
    except InferenceError:
        return ""

class MatchFunc:
    def __init__(self, path):
        self.path = path

    def set_context(self, node, child_node):
        pass
        
    def visit_assname(self, node):
        """Look for functions with the same name
        Should include imported modules and functions
        referenced from classes

        """
        
        #context = CallContext(node.args, node.starargs, node.kwargs)
        print("%s %s" % (node.name, list(node.infer())))

    def visit_callfunc(self, node):
        node_func = node.func
        infer = list(node_func.infer())
        print("Callfunc: %s %s %s" % (node.func, node, infer))



def check(path : str, node):
    print("In path %s %s" % (path, node))
    ASTWalker(MatchFunc(path)).walk(node)

