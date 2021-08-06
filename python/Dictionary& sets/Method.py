b=set()
print(type(b))
# adding values to the empty set

b.add(4)
b.add(5)
b.add(5)
b.add(5)
b.add((4,5,6))
print(b)
print(len(b))
b.remove(4)
print(b)