# multiples_of_three = []
# for number in range(3,31,3):
#     multiples_of_three.append(number)
# print(multiples_of_three)

my_favorite_pizza = ["cheese", "pepporoni", "bacon"]
your_favorite_pizza = my_favorite_pizza[:]

my_favorite_pizza.append("white")
your_favorite_pizza.append("spinach")

print("My favorite pizzas are:")
for pizza in my_favorite_pizza:
    print(pizza.title())

print("Your favorite pizzas are:")
print(your_favorite_pizza)
