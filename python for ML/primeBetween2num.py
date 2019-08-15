# prime number between two numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Prime number between {0} to {1} are:" .format(num1, num2))

for num in range(num1, num2 + 1):
    if num > 1:
        isDiv = False
        for index in range(2, num):
            if num % index == 0:
                isDiv = True
        if not isDiv:
            print(num)


# only prime check

num3 = 13

for indexx in range(2,num3):
    if num3 % indexx == 0:
        print(" prime")
        break
    else:
        print("not prime")
        break