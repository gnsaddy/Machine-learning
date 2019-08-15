# sum of number present in the list

l1 = [5, 6, 11, 22, 34, 56, 77, 2]

sum = 0
index = 0

while index < len(l1):
    sum += l1[index]
    index = index + 1

print("Sum is: {} ".format(sum))

# product of number present in the list

l2 = [5, 6, 10, 20, 100, 20]

product = 1
i = 0

while i < len(l2):
    product *= l2[i]
    i = i+1

print("Product is: {} ".format(product))

# while with else

l3 = [1, 2, 3, 4, 5, 6, 7]

i = 0

while i < len(l3):
    print(l3[i])
    i = i + 1

else:
    print("No elements is avilable in the list")

# check number is prime or not
num = int(input("Enter number to check prime: "))

isDiv = False
i = 2

while i < num:
    if num % i == 0:
        isDiv = True
        print("{} is divisible by {} ".format(num, i))
    i = i + 1

if isDiv is True:
    print("{} is not prime ".format(num))
else:
    print("{} is prime number ".format(num))


