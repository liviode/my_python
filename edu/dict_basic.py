my_dict = {'livio': ['asian', 'steak', 'pizza', 'french', 'servelat'],
           'toni': ['asian', 'cheese', 'servelat', 'pizza', 'pasta']}

my_dict['elena'] = ['pizza', 'pasta', 'servelat', 'hamburger']

print('my_list:', my_dict)
print('len:', len(my_dict))

common_food = None

for person, food_list in my_dict.items():
    if common_food == None:
        common_food = set(food_list)
    else:
        common_food = common_food.intersection(set(food_list))

print('common_food:', common_food)
