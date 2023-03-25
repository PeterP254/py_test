shopping_list=['Rice', 'chipoo', 'ndengu', 'kamande']
shopping_copy=shopping_list[:]
print(f"Three items from the middle of the list are:. {shopping_copy[:2]}")
print(shopping_list)
print(shopping_copy)
shopping_list.append('ndondoo')
shopping_copy.append('Chapoo')
print('My favourite shopping list is;\n')
for shop in shopping_list:
 #print('my favourite shopping list is;\n')
 print(shop.title())
for shop in shopping_copy:
 print(f"A dog would make a great pet,{shop}")  
print(shopping_list)
print(shopping_copy)
print('These are my best meals combined')
additions=[]
for count in range(1,100,2):
  additions.append(count**2)
print(additions)
print(additions[13:23])
print(additions[47:50])
print('check')

print(min(additions))
print(max(additions))
print(sum(additions))
print(len(additions))
# define function for addition
def add(x, y):
   return x + y



