my_dict = {"a": "1",
           "b": "2",
           "c": "3"}


reverse_dict = {value: key for key, value in my_dict.items()}


print(reverse_dict)    