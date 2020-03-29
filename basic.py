bool(0)

True and False

True or False

not True

a = [1, 2, 3]

b = a

a is b

b = a[:]

a is not b

s = "abc"

len(s)

f"aaa{s}bbb"

bool(0)

bool("")

bool([])

bool({})

bool(())

x = 1 if True else 2

a = []

a.append(1)

a.append(2)

a.append(3)

a.pop()

del a[1]

a = [1, 2, 3, 4, 5]

a[1:]

a[:-1]

a[::2]

a[::-1] # reverse

"abc"[::-1] # reverse string

b = a[:]

b is not a

a = [1] * 3

a.remove(1)

a.remove(1)

a.index(1)

a.insert(-1, 9)

a = [1, 2]

b = [3, 4]

c = a + b

a = [1, 2]

b = [3, 4]

a.extend(b)

a = range(1, 6)

1 in a

6 not in a

# tuple

(1,)

(1, 2, 3)

(1, 2) + (3, 4)

(1, 2, *(3, 4), 5)


#

[1, 2, *(3, 4), 5]

[1, 2, *[3, 4], 5]

a, *b, c = 1, 2, 3, 4, 5

a, b = 1, 2

a, b = b, a

d = {"a": 1, "b": 2}

d.keys()

d.values()

d.items()

d.get("x")

d.get("x", "default")

del d["a"]

d.update({"aa": 1})

d = {"a": 1, **{"b": 2, "c": 3}}

s = set([1])

s == {1}

s.add(1)

s1 = {1, 2, 3}

s2 = {2, 3, 4}

s1 & s2

s1 | s2

s1 - s2

s1 ^ s2

s1 > s2

1 in s1


if True:
    1
else:
    2

a = range(1, 10)

for e in a:
    print(e)

for i, e in enumerate(a):
    print(f"{i}-{e}")


i = 0
while i < 5:
    print(i)
    i += 1


try:
    raise (Exception, "err")
except Exception as e:
    print("catch err")
finally:
    print("always do")


with open("file.txt") as f:
    for line in f:
        print(line)

data = {"foo": "bar"}
with open("file1.txt", "w+") as f:
    f.write(str(data))
