# -*- coding: utf-8 -*-
__author__ = 'zhangyunrui'

pieces = u'哈佛的话就好看好看'
largeString = ''
for piece in pieces:
    largeString += piece
    print piece
    print largeString

import operator

largeString = reduce(operator.add, pieces, '')
print largeString


def add(x, y):
    return x + y


print map(lambda x: x ** 2, range(20))
print reduce(add, range(20), 1000)

print type(reduce(lambda x, y: 10 * x + y,
                  map(lambda s: {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s],
                      '123')))
