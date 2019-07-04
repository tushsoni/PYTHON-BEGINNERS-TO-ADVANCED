# In python,  STRINGS ARE IMMUTABLE

string = "string"

print(string[2])             # This will print r

# string[2] = "R"            # This will show an error , because once when we created string then we cant change it ,if we change it then it will show an error

new_string = string.replace("r", "R")           #  NOTE : It will create a new string , it don't replace the older string
print(new_string)