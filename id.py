x = [1, 2, 3]
print(id(x))
print(id([1, 2, 3]))
y = x
x[0] = 0
print(y)
print(id(y))
print(y is x)