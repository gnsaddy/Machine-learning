# output formatting in python using print statement

name = "aditya raj"
age = 21
interest = "programming"

print("{} is {} year old and he is interested in {} ".format(name, age, interest))


#we can also pass index number for formatting 

print("{0} is {1} year old and he is interested in {2} ".format(name, age, interest))


#keyword argument to format 

print("Hello {name}, {greeting} ".format(name = "Aditya",greeting="Good Morning"))