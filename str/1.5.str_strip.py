# -*- coding: utf-8 -*-
__author__ = 'zhangyunrui'

print '++--++报++--++'.lstrip('+++++++++-')
print '++--++报++--++'.lstrip('+++++++++')
print u'++--++报++--++'.lstrip('+++++++++-')
print u'++--++报++--++'.lstrip('+++++++++')
print u'++--++报++--++'.lstrip(u'+++++++++-')
print u'++--++报++--++'.lstrip(u'+++++++++')
print u'++--++报++--++'.lstrip(u'*')
print u'报++--++报++--++报'.lstrip(u'报')
# print u'报++--++报++--++报'.lstrip('报')
print u'报++--++报++--++报'.lstrip('报'.decode('utf-8'))
# print '报++--++报++--++报'.lstrip(u'报')
print '报++--++报++--++报'.lstrip('报')
