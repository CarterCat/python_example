##

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
p.x
p.y
p

##

from collections import defaultdict
dd = defaultdict(lambda: 'foo')
dd['x']
dd


##

from collections import Counter
counter = Counter()
counter['a'] += 1
counter['b'] += 2
counter

##

from collections import deque
dq = deque([1, 2, 3, 4, 5])
dq.pop()
dq.popleft()
dq.append(0)
dq.appendleft(-1)
dq

##

from collections import ChainMap
a = {'a': 1, 'b': 2}
b = {'b': 22, 'c': 33}
c = {'c': 333, 'd': 444}
cm = ChainMap(a, b, c)
cm['c']
cm['d']
cm

