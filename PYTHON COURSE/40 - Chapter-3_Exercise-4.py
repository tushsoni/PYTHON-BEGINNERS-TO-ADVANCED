# ****************************************                        CHAPTER-3_EXERCISE-4                ******************************************** #

# QUESTION 2 OF THREE

# QUESTION 2 :  Ask user to input a number containing more than one digit , example-1256 , calculate 1+2+5+6 and print


# Algorithm use to solve the problem ---- 
# step 1 : ask input in string, i.e. don't change string to int , 
# step 2 : example - "1256"
# step 3 : pick string character one by one and change to int
# step 4 : int(example[0]) + int(example[1])  ....... go upto len(example)


# ************************************************                      ANSWER                    ************************************************** #


n = input("Enter a value : ")            

total=0
i = 0

while i < len(n):
    total += int(n[i])
    i += 1
    print(total)

