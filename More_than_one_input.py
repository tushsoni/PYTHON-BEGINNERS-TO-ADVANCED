name = input("Enter your Name : ")
age = input("Enter your age : ")

print("your name is " + name)
print("your age is " + age)

# SPLIT IS STRING METHOD

name, age = input("Enter your name  and age  : ").split()

print(name)
print(age)

# If we want to use comma(,) or anthing else in input then we have to write it on split also , LETS SEE AN EXAMPLE

name, age = input("Enter your name  and age  : ").split(",")

print(name)
print(age)


