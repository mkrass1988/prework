my_dictionary = {
    'key':'value',
    1:"food",
    2:"butter",
    "hello" : "goodbye",
    3.6:"cheese curds"
}

my_dictionary['math'] = 'calculus'

print(my_dictionary)

# for key, value in my_dictionary.items():
#     print(f"The key is: {key}")
#     print(f"The value is: {value}")

for key in my_dictionary.keys():
    print(key)

for value in my_dictionary.values():
    print(value)