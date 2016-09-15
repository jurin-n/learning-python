class MyClass(object):
        pass

m = MyClass()

print(type(m))
print(type(MyClass))
print(type(12))
print(type(type))
print(type.__bases__)
print(type.__str__ is object.__str__)
print(type.__str__)
print(object.__str__)