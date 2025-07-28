import sys
a=10
a=10
b=a

print(sys.getrefcount(a))

print(a is b)


a = [1, 2, 3]
print(sys.getrefcount(a))  # Example: 2 (a + internal call)

b = a
print(sys.getrefcount(a))  # Example: 3 (a, b, and internal call)

del a
print(sys.getrefcount(b))  # Example: 2 (b + internal call)


print(type(sys))  # Should be <class 'module'>

