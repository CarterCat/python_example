class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")


class A:
    class Aaa(Exception):
        pass

    def f(self):
        raise A.Aaa()


try:
    a = A()
    a.f()
except A.Aaa as e:
    print("catch")
