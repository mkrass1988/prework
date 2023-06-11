def make_pizza():
    size = input('What size pizza would you like to order?: \n')
    toppings = []

    

    while True:
        topping = input('What would you like on your pizza?:\n(press q when finished)')
        if topping == 'q':
            break
        else:
            toppings.append(topping)

    if toppings:
        print('I have made you a ' + str(size) + ' inch pizza with:')
        for topping in toppings:
            print(topping)
        print(' on it.')
    else:
        print('I have made you a ' + str(size) + ' inch cheese pizza')



