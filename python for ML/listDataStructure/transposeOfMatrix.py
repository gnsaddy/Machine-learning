

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
for ele in matrix:
    print(ele)

# transpose without list comprehension

transposed = []
for i in range(4):
    new_lst = []
    for row in matrix:
        new_lst.append(row[i])
    transposed.append(new_lst)

print("Transpose of matrix :-")
for ele in transposed:
    print(ele)

# with list comprehension

transposed1 = [[row[i] for row in matrix] for i in range(4)]
print("Transpose of matrix with list comprehension :-")
for ele in transposed1:
    print(ele)
