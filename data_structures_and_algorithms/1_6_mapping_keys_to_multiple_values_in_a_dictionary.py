# -*- coding: utf-8 -*-
from collections import defaultdict

dl = defaultdict(list)
dl['a'].append(1)
dl['a'].append(2)
dl['b'].append(4)

ds = defaultdict(set)
ds['a'].add(1)
ds['a'].add(2)
ds['a'].add(4)

# defaultdict 会自动为将要访问的键(就算目前字典中并不存在这样的键)创建映射实体。
# 如果你并不需要这样的特性，你可以在一个普通的字典上使用 setdefault() 方法来代替

dd = {}
dd.setdefault('a', []).append(1)
dd.setdefault('a', []).append(2)
dd.setdefault('b', []).append(4)