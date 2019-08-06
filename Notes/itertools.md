## itertools
我们知道，迭代器的特点是：惰性求值（Lazy evaluation），即只有当迭代至某个值时，它才会被计算，这个特点使得迭代器特别适合于遍历大文件或无限集合等，因为我们不用一次性将它们存储在内存中。<br/>

Python 内置的 itertools 模块包含了一系列用来产生不同类型迭代器的函数或类，这些函数的返回都是一个迭代器，我们可以通过 for 循环来遍历取值，也可以使用 next() 来取值。<br/>

itertools 模块提供的迭代器函数有以下几种类型：<br/>

* 无限迭代器：生成一个无限序列，比如自然数序列 1, 2, 3, 4, ...；
* 有限迭代器：接收一个或多个序列（sequence）作为参数，进行组合、分组和过滤等；
* 组合生成器：序列的排列、组合，求序列的笛卡儿积等；

https://docs.python.org/3/library/itertools.html

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
