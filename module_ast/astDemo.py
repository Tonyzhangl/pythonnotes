#coding=utf-8

import ast

expr = """
def add(arg1, arg2):
    return arg1+arg2
print add(4,5)
"""

class CrazyTransformer(ast.NodeTransformer):
    def visit_BinOp(self, node):
        print node.__dict__
        node.op = ast.Mult()
        print node.__dict__
        return node
