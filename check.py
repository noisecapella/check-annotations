__author__ = 'schneg'

from logilab.astng import builder
from logilab.astng.utils import ASTWalker
abuilder = builder.ASTNGBuilder()

from module_tree import ModuleTree

class PrintArg:
    def set_context(self, node, child_node):
        pass

    def visit_default(self, node):
        print(node.as_string())

def check(module_tree: ModuleTree):
    for path, tree in module_tree.modules.items():
        ASTWalker(PrintArg()).walk(tree)