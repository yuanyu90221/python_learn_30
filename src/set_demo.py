set_a = {"one", "two", "three"}
set_a.add("four")
print(set_a)

set_a.update(["five","six","seven"])
print(set_a)

set_a.remove("six")
print(set_a)

set_a.discard("six")
set_a.pop()
print(set_a)

# change mutable to immutable
f_set_a = frozenset(set_a)
print(f_set_a)