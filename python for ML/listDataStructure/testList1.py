# list is a data structure in python

lst1 = [1, 2, 3, 4]
print(lst1)
lst2 = [1, 'a', 2, 'b']
print(lst2)
# list of list
lst3 = [[1, 2, 3, 4], ['a', 'b', 'c', 'd']]
print(lst3)
# list nesting
print(lst3[0][1])
print("List methods :-")
print("length of list:- ", len(lst2))
lst1.append('abc')
print("append abc into list:- ", " appended at last position ", lst1)
lst2.insert(2, "xyz")
print("insert at position 2 in lst2 ", lst2)
lst2.remove(2)
print("remove 2 from lst2 ", lst2)

lst1.reverse()
print(lst1)



