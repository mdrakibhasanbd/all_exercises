a = ["1", 1, "1", 2]
a = list(set(a))
print(a)

from collections import OrderedDict
a = ["1", 1, "1", 2]
a = list(OrderedDict.fromkeys(a))
print(a)

