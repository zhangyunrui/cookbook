# -*- coding: utf-8 -*-
__author__ = 'zhangyunrui'

import re
# revwords = re.split(r'(\s+)', 'abc def')
# print revwords
# revwords.reverse()
# revwords = ''.join(revwords)
# print revwords


str1 = 'Beautiful, is; better*than\nugly'
# print re.split(r'(\s+)', str1)
# print re.split('\s+', str1)
# print re.split(',', str1)
# print re.split(',|\*', str1)
# print re.split('(,|\*)', str1)

print reversed(str1.split())
