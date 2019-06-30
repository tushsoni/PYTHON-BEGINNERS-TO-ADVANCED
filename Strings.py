# Strigs are collection of characters inside single or double quotes

first_name = "TUSHAR  "
last_name = "SONI"

#********** Concatenations is a way to join the srtings with each other ************#

# we use plus(+) for concatenation

full_name = first_name + last_name

print(full_name)

# We can't add a number with a string  (print(first_name + 3)        -------------->>>>>>>>>>>  ERROR !!!!!!!!!!!!!!!!))       , we can only add a string with string
# we can do Two thing to add a number with string i.e. 1) put number in double quotes         2) put str(number you want to add)

print(full_name + "3")                    # METHOD 1

print(full_name + str(3))                 # Method 2

# We can use multiply(*) sign and it will print that much string , that we wrote in multiply part.

print(full_name * 4)
print(first_name * 3)
