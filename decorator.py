# case 1: simple


def d(f):
    def ff():
        print("ff")
        return f()

    return ff


@d
def f():
    return 1


f()

# case 2: function with args


def d(f):
    def ff(a):
        print("ff")
        return f(a)

    return ff


@d
def f(a):
    return a


f(1)

# case 3: decorator with args


def dd(b=1):
    def d(f):
        def ff(a):
            print("ff")
            print("a={}", a)
            print("b={}", b)
            return f(a + b)

        return ff

    return d


@dd(10)
def f(a):
    return a


f(1)


@dd()
def f(a):
    return a


f(1)


# case 4: decorator instance method


def d(f):
    def ff(self):
        print("ff")
        return f(self)

    return ff


class A:
    @d
    def f(self):
        return 1


A().f()

## case 5: decorate instance method with args


def d(f):
    def ff(self, a):
        print("ff")
        return f(self, a)

    return ff


class A:
    @d
    def f(self, a):
        return a


A().f(1)

## case 6: decorate with args for instance method


def dd(b):
    def d(f):
        def ff(self, a):
            print("ff")
            return f(self, a + b)

        return ff

    return d


class A:
    @dd(10)
    def f(self, a):
        return a


A().f(1)
