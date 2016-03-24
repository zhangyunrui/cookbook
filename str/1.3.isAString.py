# -*- coding: utf-8 -*-
__author__ = 'zhangyunrui'


def isAString(anobj):
    print isinstance(anobj, basestring)
    return isinstance(anobj, basestring)


def isExactlyAString(anobj):
    print type(anobj) is type('')
    return type(anobj) is type('')


def isStringLike(anobj):
    try:
        anobj.lower() + '' + anobj
    except:
        print False
        return False
    else:
        print True
        return True



if __name__ == '__main__':
    pass
    isAString(u'报')
    isExactlyAString(u'报')
    isExactlyAString('报')
    isStringLike(u'报')
