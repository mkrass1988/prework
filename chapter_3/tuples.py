buffet_food = ("salad", "pasta", "pizza", "soup", "drinks")

print("The food at the buffet on Monday is:")
for food in buffet_food:
    print(food)

# buffet_food[0]="ice cream"
buffet_food = ("salad", "pasta", "pizza", "ice cream", "pie")

print("\nThe new buffet food on Tuesday is:")
for food in buffet_food:
    print(food.title())