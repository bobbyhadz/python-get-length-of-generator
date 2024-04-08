# Get the length of a Generator in Python

def g():
    yield 1
    yield 2
    yield 3


gen = g()

result = len(list(gen))
print(result)  # 👉️ 3

# ----------------------------------------------------------

# Get the length of an Iterator in Python

my_iterator = iter([1, 2, 3, 4, 5])


result = len(list(my_iterator))

print(result)  # 👉️ 5