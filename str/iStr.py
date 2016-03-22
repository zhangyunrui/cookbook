# -*- coding: utf-8 -*-
__author__ = 'zhangyunrui'


class iStr(str):
    def __init__(self, *args):
        self._lowered = str.lower(self)

    def __repr__(self):
        return '%s(%s)' % (type(self).__name__, str.__repr__(self))

    def __hash__(self):
        return hash(self._lowered)

    def lower(self):
        return self._lowered

    def _make_case_insensitive(name):
        str_meth = getattr(str, name)

        def x(self, other, *args):
            try:
                other = other.lower()
            except (TypeError, AttributeError, ValueError):
                pass
            return str_meth(self._lowered, other, *args)

        setattr(iStr, name, x)

    for name in 'eq lt le gt ne cmp contains'.split():
        _make_case_insensitive('__%s__' % name)

    for name in 'count endwith find index rfind rindex startwith'.split():
        _make_case_insensitive(name)

    del _make_case_insensitive