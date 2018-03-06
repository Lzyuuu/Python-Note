# Python sorted()
# sorted()也是一个高阶函数，它可以接收一个比较函数来实现自定义排序，比较函数的定义是，传入两个待比较的元素 x, y，如果 x 应该排在 y 的前面，返回 -1，如果 x 应该排在 y 的后面，返回 1。如果 x 和 y 相等，返回 0。

import functools
sorted_ignore_case = functools.partial(sorted, cmp = (lambda s1, s2: cmp(s1.upper(), s2.upper()))
sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])