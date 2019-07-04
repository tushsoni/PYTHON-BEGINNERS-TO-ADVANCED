# ************************************************                 CHAPTER-3_EXERCISE-2 (WATCH COCO)        ************************************ #

# QUESTION : Ask user's name and age, if use,s name start with ('a' or 'A') and age is above 10 then Print 'You can watch movie' , Else print 'Sorry, you can't watch movie'


# **********************************************************                    ANSWER                      ************************************ #

name, age = input("Enter name and age with comma seperated : ").split(",")

age = int(age)

if (name[0] == 'a' or name[0] == 'A') and age >= 10:
    print("You can watch coco")

else:
    print("Sorry you can't watch coco")

