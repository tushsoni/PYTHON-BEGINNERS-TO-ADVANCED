# Make a program in which take two numbers from user and add it

number_one = input("Enter first number : ")       # Suppose we give 4
number_two = input("Enter second number : ")      # Suppose we give 5

Total = number_one + number_two
print("Total is " + Total)                       # OUTPUT : Total is 45 ,,,, This is because it take input as string

# Specifying the integer before input


number_one = int(input("Enter first number : "))     
number_two = int(input("Enter second number : "))      

Total = number_one + number_two
print("Total is " + str(Total))


# Let's use Float, int and str 

number1 = str(4)
number2 = float("44")
number3 = int("33")

print(number2 + number3)         # We can add Float and int , but the final output comes in Float

#print(number1 + number2)         # We can't add string and int

#print(number1 + number3)          # We can't add str and int
