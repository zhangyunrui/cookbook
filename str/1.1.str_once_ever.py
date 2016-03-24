# -*- coding: utf-8 -*-
__author__ = 'zhangyunrui'

str1 = 'abcd'
str2 = 'cdef'
print ''.join(set(str1) & set(str2))


print u'\u62a5'
print '\xe6\x8a\xa5'
print '\xe6\x8a\xa5'.decode('utf-8')
print str('报')
print unicode(u'报')
print str('报').decode('utf-8')
print '报'.decode('utf-8')
print '报'