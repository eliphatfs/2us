# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 14:29:53 2020

@author: eliphat
"""
import __
import functools


assert sum(map(__ + 1, range(1000))) == sum(map(lambda x: x + 1, range(1000)))
assert set(map(__[0], {1: 2, 4: 6}.items())) == {1, 4}
assert tuple(map(__.is_in([1, 2]), [3, 1, 5, 0, 2])) == (False, True, False, False, True)
assert functools.reduce(__ + __, range(1000)) == sum(range(1000))
