__author__ = 'schneg'

from astroid import builder
from astroid.utils import ASTWalker
from astroid.exceptions import InferenceError
abuilder = builder.AstroidBuilder()

from module_tree import ModuleTree

def infer(node):
    try:
        return list(node.infer())
    except InferenceError:
        return ""

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
    for path, tree in module_tree.modules.items():
        print()
        print("In path %s" % path)
        ASTWalker(PrintArg()).walk(tree)
