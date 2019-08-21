# provide a concise way to create lists

# take example,square of number

# without list comprehension 
squares = []
for i in range(10):
    squares.append(i ** 2)
print(squares)

# with list comprehension
squares1 = [i ** 2 for i in range(10)]
print(squares1)

# more examples

lst = [-10, -20, 10, 20, 50]
new_lst = [i * 2 for i in lst]
print(new_lst)

new_lst2 = [i * 2 for i in lst if i >= 0]
print(new_lst2)

# create a list of tuple like [(number,square_of_number)]

new_lst3 = [(i, i ** 2) for i in range(10)]
print(new_lst3)