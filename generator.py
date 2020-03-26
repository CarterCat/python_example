# generator

# why? a simple way of creating iterators.

# what?  a function that returns an object (iterator)

#        which we can iterate over (one value at a time).

# how? a normal function with `yield` statement

#        instead of a `return` statement.


def g1():
    n = 1
    yield n
    n += 1
    yield n
    n += 1
    yield n


i = g1()

for e in i:
    print(e)

##


def g2():
    for e in range(0, 5):
        yield e


i = g2()

for e in i:
    print(e)


# list comprehension vs generator expression

# list comprehension -> [] -> eager

# generator expression -> () -> lazy

# generator expression is much more memory efficient

l = [1, 2, 3, 4, 5]

r1 = [e * 2 for e in l]  # => a list

r2 = (e * 2 for e in l)  # => a generator

for e in r1:
    print(e)

for e in r2:
    print(e)


##

l = [1, 2, 3, 4, 5]

sum1 = sum([e for e in l])

sum2 = sum(e for e in l)

max1 = max([e for e in l])

max2 = max(e for e in l)

## pipelining generators

with open("sells.log") as file:
    pizza_col = (line[3] for line in file)
    per_hour = (int(x) for x in pizza_col if x != "N/A")
    print("Total pizzas sold = ", sum(per_hour))
