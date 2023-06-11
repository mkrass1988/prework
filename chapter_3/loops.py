types_of_fruits = ["apples", "bananas", "mangos", "kiwis"]

# letter_to_check = input("what letter should we check?")

# for fruit in types_of_fruits:
#     if fruit[0] == letter_to_check:
#         print(fruit.title() + " " + "are good for you" + ".\n")
#     elif fruit[0] != letter_to_check:
#         print("no fruits have that letter")

# length = len(types_of_fruits)

# for i in range(len(types_of_fruits)):
#     print(types_of_fruits[i])
favorite_fruit = []
for item in types_of_fruits:
    if item[0] in ["a", "b"]:
        favorite_fruit.append(item)
    else:
        continue

other_fruit = [item for item in types_of_fruits if item[0] in ["a", "b"]]

print(favorite_fruit)
print(other_fruit)
