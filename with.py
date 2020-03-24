# context management protocol

# __enter__(), __exit__()

# context manager

# runtime context

# context expression -> with


class A:
    def __init__(self):
        self.x = 1
        self.y = 2
        print("init")

    def __enter__(self):
        print("enter")
        return self.x + self.y

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("exit")


# with A() as x:
#     print(x)


class DummyResource:
    def __init__(self, tag):
        self.tag = tag
        print("Resource [%s]" % tag)

    def __enter__(self):
        print("[Enter %s]: Allocate resource." % self.tag)
        return self  # 可以返回不同的对象

    def __exit__(self, exc_type, exc_value, exc_tb):
        print("[Exit %s]: Free resource." % self.tag)
        if exc_tb is None:
            print("[Exit %s]: Exited without exception." % self.tag)
        else:
            print("[Exit %s]: Exited with exception raised." % self.tag)
            return False  # 可以省略，缺省的None也是被看做是False


with DummyResource("Normal"):
    print("[with-body] Run without exceptions.")

# with DummyResource('With-Exception'):
#     print('[with-body] Run with exception.')
#     raise Exception
#     print('[with-body] Run with exception. Failed to finish statement-body!')
