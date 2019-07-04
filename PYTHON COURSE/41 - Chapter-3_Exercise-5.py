# ************************************                     CHAPTER-3_EXERCISE-5            ********************************************* #

# question 3 out of three

# QUESTION 3 :

# Ask a user for name
# Example - Tushar soni
# Print count of each word
# Output :
           # T : 1
           # u : 1
           # s : 1
           # h : 1
           # a : 1
           # r : 1
           # s : 2
           # o : 1
           # n : 1
           # i : 1  


# ***********************************************************                  ANSWER            ********************************************** #


name = input("Enter a name : ")

temp_var = ""
i = 0 
while i < len(name):
    if name[i] not in temp_var:
        temp_var += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i += 1