# -*- coding: utf-8 -*-
import heapq
import operator
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

protfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, protfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, protfolio, key=operator.itemgetter('price'))

print(cheap)
print(expensive)

heapq.heapify(nums)
heapq.heappop(nums)

# 当要查找的元素个数相对比较小的时候，函数 nlargest() 和 nsmallest() 是很合适的。
# 如果你仅仅想查找唯一的最小或最大(N=1)的元素的话，那么使用min()和max()函数会更快些。
# 类似的，如果N的大小和集合大小接近的时候，通常先排序这个集合然后再使用切片操作会更快点 ( sorted(items)[:N] 或者是 sorted(items)[-N:] )。