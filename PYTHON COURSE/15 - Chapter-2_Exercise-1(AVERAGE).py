# ***************************************** CHAPTER 2 - EXRERCISE-1 ***************************************#

# QUESTIONS : ASK USER TO INPUT 3 NUMBERS AND YOU HAVE TO PRINT AVERAGE OF THREE NUMBERS USING STRING FORMATTING.     
#  BONUS : TRY TO TAKE ALL THREE COMMA SEPERATED INPUTS IN ONE LINE

#***********************************************                ANSWER                    *************************************************************#

number_one = int(input("Enter first number : "))     
number_two = int(input("Enter second number : "))
number_three = int(input("Enter third number : "))


print(f"Average of your three numbers is {(number_one + number_two + number_three)/3}")

# If we wan to take input in one line

num1, num2, num3 = input("Enter three numbers comma seperated : ").split(",")

print(f"Average of your three numbers is {(int(num1) + int(num2) + int(num3)) / 3}")