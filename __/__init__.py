# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 12:59:11 2020

@author: eliphat
"""
import sys
import operator
import functools
from types import ModuleType


class LambdaProxyModule(ModuleType):
    def __getattr__(self, name):
        return lambda x: getattr(x, name)

    def __call__(self, *args, **kwargs):
        return lambda x: x(*args, **kwargs)

    def __getitem__(self, key):
        return operator.itemgetter(key)

    def is_in(self, it):
        return functools.partial(operator.contains, it)

    def contains(self, other):
        if self is other:
            return lambda x, y: y in x
        return lambda x: other in x

    def __lt__(self, other):
        if self is other:
            return operator.__lt__
        return lambda x: x < other

    def __le__(self, other):
        if self is other:
            return operator.__le__
        return lambda x: x <= other

    def __eq__(self, other):
        if self is other:
            return operator.__eq__
        return lambda x: x == other

    def __ne__(self, other):
        if self is other:
            return operator.__ne__
        return lambda x: x != other

    def __gt__(self, other):
        if self is other:
            return operator.__gt__
        return lambda x: x > other

    def __ge__(self, other):
        if self is other:
            return operator.__ge__
        return lambda x: x >= other

    def __add__(self, other):
        if self is other:
            return operator.__add__
        return lambda x: x + other

    def __sub__(self, other):
        if self is other:
            return operator.__sub__
        return lambda x: x - other

    def __mul__(self, other):
        if self is other:
            return operator.__mul__
        return lambda x: x * other

    def __matmul__(self, other):
        if self is other:
            return operator.__matmul__
        return lambda x: x @ other

    def __truediv__(self, other):
        if self is other:
            return operator.__truediv__
        return lambda x: x / other

    def __floordiv__(self, other):
        if self is other:
            return operator.__floordiv__
        return lambda x: x // other

    def __mod__(self, other):
        if self is other:
            return operator.__mod__
        return lambda x: x % other

    def __pow__(self, other):
        if self is other:
            return operator.__pow__
        return lambda x: x ** other

    def __lshift__(self, other):
        if self is other:
            return operator.__lshift__
        return lambda x: x << other

    def __rshift__(self, other):
        if self is other:
            return operator.__rshift__
        return lambda x: x >> other

    def __and__(self, other):
        if self is other:
            return operator.__and__
        return lambda x: x & other

    def __xor__(self, other):
        if self is other:
            return operator.__xor__
        return lambda x: x ^ other

    def __or__(self, other):
        if self is other:
            return operator.__or__
        return lambda x: x | other

    def __radd__(self, other):
        if self is other:
            return lambda x, y: y + x
        return lambda x: other + x

    def __rsub__(self, other):
        if self is other:
            return lambda x, y: y - x
        return lambda x: other - x

    def __rmul__(self, other):
        if self is other:
            return lambda x, y: y * x
        return lambda x: other * x

    def __rmatmul__(self, other):
        if self is other:
            return lambda x, y: y @ x
        return lambda x: other @ x

    def __rtruediv__(self, other):
        if self is other:
            return lambda x, y: y / x
        return lambda x: other / x

    def __rfloordiv__(self, other):
        if self is other:
            return lambda x, y: y // x
        return lambda x: other // x

    def __rmod__(self, other):
        if self is other:
            return lambda x, y: y % x
        return lambda x: other % x

    def __rpow__(self, other):
        if self is other:
            return lambda x, y: y ** x
        return lambda x: other ** x

    def __rlshift__(self, other):
        if self is other:
            return lambda x, y: y << x
        return lambda x: other << x

    def __rrshift__(self, other):
        if self is other:
            return lambda x, y: y >> x
        return lambda x: other >> x

    def __rand__(self, other):
        if self is other:
            return lambda x, y: y & x
        return lambda x: other & x

    def __rxor__(self, other):
        if self is other:
            return lambda x, y: y ^ x
        return lambda x: other ^ x

    def __ror__(self, other):
        if self is other:
            return lambda x, y: y | x
        return lambda x: other | x


sys.modules[__name__].__class__ = LambdaProxyModule
