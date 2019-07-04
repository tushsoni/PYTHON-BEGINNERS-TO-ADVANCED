# if elif else statement

# EXAMPLE : PRINT ::::

# show ticket pricing
# 0 to 3 (Free)
# 4 to 10 (150)
# 11 to 60 (250)
# above 60 (200)

age = input("Enter your age to know ticket price : ")

age = int(age)

if age == 0 or age < 0:
    print("You cannot watch this movie")



elif 0 < age <=3:
    print("Ticket Price : FREE")

elif 3 < age <=10:
    print("Ticket Price : 150 ")

elif 10 < age <=60:
    print("Ticket Price : 250")

else:
    print("Ticket Price : 200")