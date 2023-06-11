sandwich_orders = ['pastrami', 'salami', 'capicola', 'meatball', 
                   'pastrami', 'pb and j'
                   ]
finished_orders = []

# active = True

while sandwich_orders:
    finished_order = sandwich_orders.pop()
    if finished_order == 'pastrami':
        continue
    finished_orders.append(finished_order)

print("Unfortunately we are out of Pastrami but we did finish these orders:")
for i in finished_orders:
    print(i)


#print(finished_orders)