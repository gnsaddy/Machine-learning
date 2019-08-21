
# del method is used to remove item based on index position, it will not return anyting 'none'

lst1 = [1, 'a', 'b', 2, 3, 4]
del lst1[2]
print(lst1)

# pop method is also used to delete element from list based on index position but it return the value of deleted element

lst2 = [1, 2, 3, 4, 5, 6]
deletedEle = lst2.pop(3)
print(deletedEle)
