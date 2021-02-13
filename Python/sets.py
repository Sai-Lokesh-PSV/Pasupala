# Create an empty set
b = set()

#adding elements to a set
a = input("A number:")
b = input("An another number:")
c = input("An another number:")
b.add(a)
b.add(b)
b.add(c)
print("Here is your set",b)

print(f"the set has {len(b)} elements")