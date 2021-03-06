## itertools
我们知道，迭代器的特点是：惰性求值（Lazy evaluation），即只有当迭代至某个值时，它才会被计算，这个特点使得迭代器特别适合于遍历大文件或无限集合等，因为我们不用一次性将它们存储在内存中。<br/>

https://docs.python.org/3/library/itertools.html

* [1.Merging and Splitting Iterators](#1)
    * [1.1 chain()](#1.1)
    * [1.2 chain.from_iterable()](#1.2)
    * [1.3 zip() and zip_longest()](#1.3)
    * [1.4 islice()](#1.4)
    * [1.5 tee()](#1.5)
* [2.Coverting Inputs](#2)
    * [2. 1 map() and starmap()](#2.1)
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
<br><br>
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
<br><br>
<h6 id="1.3">1. 3 zip() and zip_longest()</h6>

```python
zip(*iterables)
```
zip是python内置函数，返回一个迭代器，它将几个迭代器的元素组合成***元组***. 返回值是一个可以迭代的对象，每次遍历产生一个值。

```python
for i in zip([1,2,3],['a','b','c']):
    print(i)
```
```
(1, 'a')
(2, 'b')
(3, 'c')
```
当第一个输入迭代器耗尽时，zip（）停止。
```python
for i in zip([1,2,3,4,5],['a','b']):
    print(i)
```
```
(1, 'a')
(2, 'b')
```

<br>
如果想要处理所有数据（以长迭代器为准），使用zip_longest():

```python
itertools.zip_longest(*iterables, fillvalue=None)
```

默认情况下，zip_longest（）将任何缺失值替换为None。 使用fillvalue参数来使用不同的替代值。

```python
from itertools import zip_longest
for i in zip_longest([1,2,3,4,5],['a','b','c']):
    print(i)
```
```
(1, 'a')
(2, 'b')
(3, 'c')
(4, None)
(5, None)
```

<br><br>
<h6 id="1.4">1. 4 islice</h6>

``` python
itertools.islice(iterable, stop)

itertools.islice(iterable, start, stop[, step])
```
islice()函数返回一个迭代器，通过**索引**从输入迭代器中挑选结果输出

```python
from itertools import islice

for i in islice(range(10),5):
    print(i,end= ' ')
    
for i in islice(range(10),5,10):
    print(i,end= ' ')

for i in islice(range(100), 0,100,10):
    print(i,end= ' ')
```
```
0 1 2 3 4 
5 6 7 8 9 
0 10 20 30 40 50 60 70 80 90 
```
<br><br>
<h6 id="1.5">1. 5 tee</h6>

``` python
itertools.tee(iterable, n=2)
```
tee() 函数根据单个原始输入返回几个独立的迭代器。当复制到输出迭代后，原来的迭代器会被视为“消耗”掉。
```python
from itertools import tee,islice,count

r = islice(count(),5)
i1,i2 = tee(r)
print('i1:', list(i1))
print('i2:', list(i2))
print('r:',list(r))
```
```
i1: [0, 1, 2, 3, 4]
i2: [0, 1, 2, 3, 4]
r: []
```
----


----

<h3 id="2">2.Coverting Inputs</h3>

<h6 id="2.1">2. 1 map and starmap</h6>

```python
map(function_to_apply, list_of_inputs)
```


```python
from itertools import chain

for item in chain([1,2,3],['a','b','c']):
    print(item, end = ' ')
```
```
1 2 3 a b c
```

