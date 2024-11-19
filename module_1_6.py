my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print(my_dict)
print(my_dict.get('Vasya'))
print(my_dict.get('Misha'))
my_dict.update({'Misha' : 2003, 'Katya': 1980})
a = my_dict.pop('Egor')
print(a)
print(my_dict)

my_set = {1, 5, 7, 5, 5, True, False, False, 'No', 'Yes', 'Yes'}
print(my_set)
my_set.add('Idk')
my_set.add(4)
my_set.discard(5)
print(my_set)