toppings = ['pepperoni', 'cheese', 'ham', 'bacon',
            'mushrooms', 'peppers', 'onions', 'olives']

import itertools
for x in itertools.combinations(toppings, 3):
    print(x)



