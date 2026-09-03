a = 200
b = 200
print(a is b)

a = 2000
b = 2000
print(a is b)

# Python caches small integers (typically -5 to 256), so 200 may share the same object while 2000 usually does not.