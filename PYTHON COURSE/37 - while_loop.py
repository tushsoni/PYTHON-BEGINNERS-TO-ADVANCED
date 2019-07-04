# LOOP     --------------- >>>>>>>>>>>                1) while loop
#                                                     2) for loop


# 1) while loop

i = 1                                                  # we initialise the value of i =1

while i<=10:                                           # Now it will check that i is < = 10 or not and the answer is yes because we initialises the value of i =1
    print(f"Hello world {i}")                          # It will print hello world one time
    i = i + 1                                          # Now it will ad i + 1 that means 1+1=2 , Now i value becomes 2 and the loop will execute again untilll the condition becomes false



i = input("Enter the value : ")
i =int(i)

while i<=55:
    print(f"Your hello world {i}")
    i = i + 1

else:
    print("Out of range(Condition false)")