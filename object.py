import json


class Foo(object):
    a = 1

    def __init__(self, b, c):
        self.b = b
        self.c = c


foo = Foo(2, 3)
foo_dict = foo.__dict__
foo_json = json.dumps(foo_dict)

print(foo)
print(foo_dict)
print(foo_json)
