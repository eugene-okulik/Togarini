my_dict = {
    "tuple": (1, 2, 3, 'text', 3.32, True),
    "list": [1, 2.34, 5, 'dict', 3.334, None],
    "dict": {"one": 1, "two": "2", "three": False, "four": 4.4, "five": None},
    "set": {None, "False", 3, 4, 5, 6, 7, 8, 9, 10}
}

my_dict["tuple"][-1]
my_dict["list"].append(4.4)
my_dict["list"].remove(2.34)
my_dict["dict"][("i am a tuple",)] = 5
my_dict["dict"].pop("four")
my_dict["set"].add(11)
my_dict["set"].remove(7)

print(my_dict)
