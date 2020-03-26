# iterator

# an object that can iterated upon.

# an object that return data, one item at a time.

# build own iterator with iterable protocol

# by impl two special methods `__iter__` and `__next__`

# `iter()` function => call `__iter__()` method -> return iterator

# `next()` function => call `__next__()` method -> return next item

# when reach the end, it will raise `StopIteration`.


# where?

# - for loop

# - comprehension

# - generator

a = [1, 2, 3, 4, 5]

i = iter(a)

a1 = next(i)  # 1

a2 = next(i)  # 2

print(f"a1={a1},a2={a2}")

# for

a = [1, 2, 3, 4, 5]

for e in a:
    print(e)

# impl for

a = [1, 2, 3, 4, 5]

i = iter(a)

while True:
    try:
        e = next(i)
        print(e)
    except StopIteration:
        break

# 1
# 2
# 3
# 4
# 5

# own iterator


class A:
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 * self.n
            self.n += 1
            return result
        else:
            raise StopIteration


a = A(5)
i = iter(a)
for e in i:
    print(e)

# 0
# 2
# 4
# 6
# 8
# 10

##

l = [1,2,3,4,5]

i = iter(l)

for e in i:
    print(e)
    
