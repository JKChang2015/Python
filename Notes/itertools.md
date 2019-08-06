## itertools
我们知道，迭代器的特点是：惰性求值（Lazy evaluation），即只有当迭代至某个值时，它才会被计算，这个特点使得迭代器特别适合于遍历大文件或无限集合等，因为我们不用一次性将它们存储在内存中。<br/>

https://docs.python.org/3/library/itertools.html

* [1.Merging and Splitting Iterators](#1)
    * [1.1 chain()](#1.1)
    * [1. 2 chain.from_iterable()](#1.2)
* [2.Coverting Inputs](#2)
* [3.Producing New Values](#3)
* [4.Filtering](#4)
* [5.Grouping Data](#5)
* [6.Combining Inputs](#6)

``` python
import itertools
print('\n'.join(itertools.__dict__))
```
output:

```
__name__
__doc__
__package__
__loader__
__spec__
tee
accumulate
combinations
combinations_with_replacement
cycle
dropwhile
takewhile
islice
starmap
chain
compress
filterfalse
count
zip_longest
permutations
product
repeat
groupby
_grouper
_tee
_tee_dataobject
```
----

<h3 id="1">1.Merging and Splitting Iterators</h3>

<h6 id="1.1">1. 1 chain 链式迭代</h6>

```python
chain(iterable1, iterable2, iterable3, ...)
```
chain 接收多个可迭代对象作为参数，将它们『连接』起来，作为一个新的迭代器返回。 迭代器按照顺序一一运行.

```python
from itertools import chain

for item in chain([1,2,3],['a','b','c']):
    print(item, end = ' ')
```
```
1 2 3 a b c
```

<h6 id="1.2">1. 2 chain.from_iterable</h6>

```python
chain.from_iterable(iterable)
```
如果要组合的迭代不是全部事先声明的，或者需要延迟评估（evaluated ），可以使用chain.from_iterable（）来构造链.

```python
from itertools import chain
def make_interable_to_chain():
    yield[1,2,3]
    yield['a','b','c']

for i in chain.from_iterable(make_interable_to_chain()):
    print(i,end=' ')
```
```
1 2 3 a b c
```
