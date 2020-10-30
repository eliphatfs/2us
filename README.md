# __ (Double Underscores)
Glueing functionals by `import __` for python!

## Install
The package is written in pure python, with no dependencies other than the Python language. Just do:

```sh
pip install __
```

Requires Python 3.5 or higher.

## Why this?
Python is a great language for creating convenient wrappers around native code and implementing simple, human-friendly functions.
In python, a bunch of builtin higher-order methods (which means that they accept functions as arguments) such as `map`, `filter` are available.
They enable streamed data processing on containers that focus on the processing itself,
in contrast with *noisy code* on traditional command-based languages that is heavily involved in loops.

However, you may occasionally run into the situatiion where you find that there is no standard library functions to implement in-line unpacking of tuples,
adding all numbers in a list by a constant shift, so you will have to write:
```python
map(lambda x: x + 1, some_list)
map(lambda x: x[0], some_list)
```
which seems rather dumb due to the inconvenient definition of lambda functions in python.

## Using __
Start using the package by importing `__`:
```python
import __
```
And then `__` can be used to create convenient functions that are identical to those written with `lambda`. Examples:
```python
assert sum(map(__ + 1, range(1000))) == sum(map(lambda x: x + 1, range(1000)))
assert set(map(__[0], {1: 2, 4: 6}.items())) == {1, 4}
assert functools.reduce(__ + __, range(1000)) == sum(range(1000))
```
Currently there is a drawback: python do not support overriding `__contains__` returning non-boolean values, so the `in` condition should be handled separately.
```python
assert tuple(map(__.is_in([1, 2]), [3, 1, 5, 0, 2])) == (False, True, False, False, True)
assert list(map(__.contains('1'), '13')) == [True, False]
```
