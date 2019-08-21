# the easiest way to sort a list is with the sorted(list) method
# it takes a list and retun a new list with with those list element in sorted order
# by default the order is ascending order
# the original list is not changed.

num = [3, 2, 4, 1, 6, 5, 8, 7, 9, 0]
sorted_list = sorted(num)
print(sorted_list)

# for sorting in descending order

sorted_list_des = sorted(num, reverse=True)
print(sorted_list_des)

# sort function


