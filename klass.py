
class A:
    def instance_method(self, a, b):
        return a + b
    @classmethod
    def class_method(cls, a, b):
        return a + b
    @staticmethod
    def static_method(a, b):
        return a + b



A().instance_method(1, 2)

A.class_method(1, 2)

A.static_method(1, 2)