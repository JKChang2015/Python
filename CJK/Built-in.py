# -*- coding: UTF-8 -*-
# Built-in
# Created by JKChang
# 20/11/2017, 11:19
# Tag:
# Description: Built-in Functions — Python 3.4.7 documentation
# The Python interpreter has a number of functions and types built into it that are always available.

# __import__()	abs()	all()	any()	ascii()	bin()	bool()	bytearray()
# bytes()	callable()	chr()	classmethod()	compile()	complex()	delattr()	dict()
# dir()	divmod()	enumerate()	eval()	exec()	filter()	float()	format()
# frozenset()	getattr()	globals()	hasattr()	hash()	help()	hex()	id()
# input()	int()	isinstance()	issubclass()	iter()	len()	list()	locals()
# map()	max()	memoryview()	min()	next()	object()	oct()	open()
# ord()	pow()	print()	property()	range()	repr()	reversed()	round()
# set()	setattr()	slice()	sorted()	staticmethod()	str()	sum()	super()
# tuple()	type()	vars()	zip()

# --------------------------------------------------------------------------------------------------------------
# abs(x)
# Return the absolute value of a number.  The argument may be an integer or a floating point number.
# If the argument is a complex number, its magnitude is returned.

# a = 1
# b = -1
# c = 1j * 1j
#
# print(abs(a))
# print(abs(b))
# print(abs(c))

# --------------------------------------------------------------------------------------------------------------
# all(iterable)
# Return True if all elements of the iterable are true (or if the iterable is empty). Equivalent to:

# +-----------------------------------------+---------+---------+
# |                                         |   any   |   all   |
# +-----------------------------------------+---------+---------+
# | All Truthy values                       |  True   |  True   |
# +-----------------------------------------+---------+---------+
# | All Falsy values                        |  False  |  False  |
# +-----------------------------------------+---------+---------+
# | One Truthy value (all others are Falsy) |  True   |  False  |
# +-----------------------------------------+---------+---------+
# | One Falsy value (all others are Truthy) |  True   |  False  |
# +-----------------------------------------+---------+---------+
# | Empty Iterable                          |  False  |  True   |
# +-----------------------------------------+---------+---------+

def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

# --------------------------------------------------------------------------------------------------------------
# any(iterable)
# Return True if any element of the iterable is true. If the iterable is empty, return False. Equivalent to:

# +-----------------------------------------+---------+---------+
# |                                         |   any   |   all   |
# +-----------------------------------------+---------+---------+
# | All Truthy values                       |  True   |  True   |
# +-----------------------------------------+---------+---------+
# | All Falsy values                        |  False  |  False  |
# +-----------------------------------------+---------+---------+
# | One Truthy value (all others are Falsy) |  True   |  False  |
# +-----------------------------------------+---------+---------+
# | One Falsy value (all others are Truthy) |  True   |  False  |
# +-----------------------------------------+---------+---------+
# | Empty Iterable                          |  False  |  True   |
# +-----------------------------------------+---------+---------+

def any(iterable):
    for element in iterable:
        if element:
            return True
    return False

# --------------------------------------------------------------------------------------------------------------