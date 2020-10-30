# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 13:40:24 2020

@author: eliphat
"""


model = """
    def {0}(self, other):
        if self is other:
            return operator.{0}
        return lambda x: x {1} other
"""
r_model = """
    def {0}(self, other):
        if self is other:
            return lambda x, y: y {1} x
        return lambda x: other {1} x
"""
ops = {
    "__lt__": "<",
    "__le__": "<=",
    "__eq__": "==",
    "__ne__": "!=",
    "__gt__": ">",
    "__ge__": ">=",
    "__add__": "+",
    "__sub__": "-",
    "__mul__": "*",
    "__matmul__": "@",
    "__truediv__": "/",
    "__floordiv__": "//",
    "__mod__": "%",
    "__pow__": "**",
    "__lshift__": "<<",
    "__rshift__": ">>",
    "__and__": "&",
    "__xor__": "^",
    "__or__": "|"
}
rops = {
    "__contains__": "in",
    "__radd__": "+",
    "__rsub__": "-",
    "__rmul__": "*",
    "__rmatmul__": "@",
    "__rtruediv__": "/",
    "__rfloordiv__": "//",
    "__rmod__": "%",
    "__rpow__": "**",
    "__rlshift__": "<<",
    "__rrshift__": ">>",
    "__rand__": "&",
    "__rxor__": "^",
    "__ror__": "|"
}
s = ''
for n0, n1 in ops.items():
    s += model.format(n0, n1)
for n0, n1 in rops.items():
    s += r_model.format(n0, n1)
print(s)
