my_dict = {'Lena': 1999, 'Dima' : 2001, 'Alina': 2000 }
print('Dict:', my_dict)
print('Existing value:', my_dict.get('Dima'))
print('Not existing value:', my_dict.get('Mars'))
my_dict.update({'Misha' : 2001, 'Sasha' : 1998})
print('Deleted value:', my_dict.pop('Lena'))
print('Modified dictionary:', my_dict)
my_set = {25.3, 'карта', 25.3, 9, 'карта', 9, 9}
print('Set:', my_set)
my_set.add('флаг')
my_set.add((56, 4, 78))
my_set.discard(25.3)
print('Modified set:', my_set)