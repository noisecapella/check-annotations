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

def convertible(from_type, to_type):
    if from_type == to_type:
        return True
    if ((from_type == int and to_type == float) or
        (from_type == float and to_type == int)):
        return True
    if from_type == str or to_type == str:
        return False
    try:
        if issubclass(from_type, to_type) or issubclass(to_type, from_type):
            return True
    except TypeError:
        pass
    # TODO: this is pretty arbitrary where this line is drawn
    return False

def collision_in(infer_list):
    already_found = []
    for item in infer_list:
        item_type = item.pytype()
        if not already_found:
            already_found.append(item_type)
        else:
            for other_type in already_found:
                if not convertible(item_type, other_type):
                    raise Exception("Found type %s which conflicts with type %s" % (item_type, other_type))
            if item_type not in already_found:
                already_found.append(item_type)

    return False

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
        
        if collision_in(node.infer()):
            raise Exception("Collision: %s" % node.infer)



def check(path : str, node):
    print("In path %s %s" % (path, node))
    ASTWalker(MatchFunc(path)).walk(node)

