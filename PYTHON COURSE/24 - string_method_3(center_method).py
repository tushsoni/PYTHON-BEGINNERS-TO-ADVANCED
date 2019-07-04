#        center method

# center method is used to add things(i.e *,$,@ and etc.) before and after our string
 
# Example :         **Tushar**

# APPROCH TO DO THIS :::: IF WE WANT TO ADD STARS LEFT AND  RIGHT SIDE THEN WE SHOULD WRITE LENGHT OF STRING + HOW MANY ASTRISKS WE HAVE TO ADD 

# LET'S TAKE AN EXAMPLE 

name = "Tushar"

# if we have to make it   **Tushar**              then we should right ::

print(name.center(7, "*"))                            # it will add one star and add on the left side

print(name.center(10, "*"))                           #  10 = length of string (6) + how many astrisks we have to add(4)

print(name.center(10, "$"))

print(name.center(10, "@"))

print(name.center(10, "&"))

print(name.center(10, "!"))

print(name.center(10, "^"))


name = input("Enter your name : ")

print(name.center(len(name) + 8, "*"))