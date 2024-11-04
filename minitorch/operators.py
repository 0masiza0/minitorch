"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

def mul(x: float, y: float) -> float:
    #print(x, y, x * y)
    return x * y
    
def id(x: float) -> float:
    return x
    
def add(x: float, y: float) -> float:
    return x + y
    
def neg(x: float) -> float:
    return float(-x)
    
def lt(x: float, y: float) -> float:
    return 1. if x < y else 0.
    
def eq(x: float, y: float) -> float:
    return 1. if x == y else 0.
    
def max(x: float, y: float) -> float:
    return x if x > y else y
    
def is_close(x: float, y: float, tol=1e-2) -> float:
    return 1. if abs(x - y) < tol else 0.

def sigmoid(x: float) -> float:
    if x > 0.:
        return 1. / (1. + math.exp(-x))
    else:
        return math.exp(x) / (1. + math.exp(x))
    
def relu(x: float) -> float:
    return 0. if x < 0. else x
    
def log(x: float) -> float:
    return math.log(x + 1)
    
def exp(x: float) -> float:
    return math.exp(x)
    
def log_back(x: float, y: float) -> float:
    return y / x

def inv(x: float) -> float:
    return 1. / x
    
def inv_back(x: float, y: float) -> float:
    return -y / (x * x)
    
def relu_back(x: float, y: float) -> float:
    return 0. if x < 0. else y

# Mathematical functions:
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists

def map(iterable, f):# -> Iterable[float]:
    return [f(x) for x in iterable]

def zipWith(iterable1, iterable2, f):
    return [f(iterable1[i], iterable2[i]) for i in range(len(iterable1))] 
    
def reduce(iterable, f, start):
    result = start
    for x in iterable:
        result = f(result, x)
    return result

def negList(iterable):
    return map(iterable, neg)
    
def addLists(iterable1, iterable2):
    return zipWith(iterable1, iterable2, add)
    
def sum(iterable):
    return reduce(iterable, add, 0)
    
def prod(iterable):
    return reduce(iterable, mul, 1)
# TODO: Implement for Task 0.3.
