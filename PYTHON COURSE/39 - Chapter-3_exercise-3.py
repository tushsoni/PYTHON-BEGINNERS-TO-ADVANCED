# ************************************************                CHAPTER-3_EXERCISE-3           ************************************** #

# QUESTION 1 :              
 
 
# Exercise one of three

# Sum of n natural numbers

# ask a user for natural number(n)

# print total from 1 to n



# ***************************************                            ANSWER                     ********************************************* #

n= input("Enter a number : ")
n = int(n)
total = 0
i = 1

while i <= n:
    total += i                     
    i += 1
    print(total)