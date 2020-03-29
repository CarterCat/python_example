# closure

# why?

# 1 avoid use global variable

# 2 data hiding -> encapsulation

# 3 decorator

##


def f(msg):
    def ff():
        print(msg)

    ff()


f("foo")

##


def f(msg):
    def ff():
        print(msg)

    return ff


ff = f("foo")
ff()

##


def f(a):
    def ff(b):
        print(a + b)

    return ff


add1 = f(1)
add2 = f(2)

add1(4)
add2(4)

add1.__closure__[0].cell_contents

add2.__closure__[0].cell_contents
