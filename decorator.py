# decorator

# use for: log, cache, assert, etc...


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

# case 6: decorate with args for instance method


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


# logger

import logging

def use_logging(func):

    def wrapper(*args, **kwargs):
        logging.warn("%s is running" % func.__name__)
        return func(*args, **kwargs)
    return wrapper

@use_logging
def foo():
    print("i am foo")

foo()


## 

def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warn("%s is running" % func.__name__)
            elif level == "info":
                logging.info("%s is running" % func.__name__)
            return func(*args)
        return wrapper

    return decorator

@use_logging(level="warn")
def foo(name='foo'):
    print("i am %s" % name)

foo()


##


def error_log(logger):
    def wrapper(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger.error(f"{args[0].__class__.__name__}:{func.__name__}(error={e})", exc_info=True)
        return wrapper
    return wrapper


# # example
# import logging 

# logger = logging.getLogger("auction.%s" % __name__)

# class A:
#     @error_log(logger)
#     def foo(self, a,b):
#         1/0
#         return a+b

# A().foo(1,2)



