# CHECK TWO CONDITIONS AT THE SAME TIME

# and , or    ---------------------->>>>>>>> These two operators are used to check two conditions at the same time


name, age = input("Enter name and age comma seperated : ").split(",")


if name == "Tushar" or int(age) == 21:                    # in this "or" case if any condition is true then it will print "condition is true"
    print("Condition is True")

else:
    print("Condition is false")



if name == "Tushar" and int(age) == 21:                    # For the printing of "condition in true" both condition shoul be true
    print("Condition is True")

else:
    print("Condition is false")