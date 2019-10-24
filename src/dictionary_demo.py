our_dictionary = {"name":"Json", "height":"6'0", "location":"lost"}

print(our_dictionary["name"])

our_dictionary["name"] = "Micheal"
print(our_dictionary)

our_dictionary["eye color"] = "blue"
print(our_dictionary)
# pop specific property
our_dictionary.pop("eye color")
print(our_dictionary)