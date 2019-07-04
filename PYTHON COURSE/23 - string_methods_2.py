# ******************************************************************                STRING METHODS _ PART 2                   ************************************** #

string = "She is a very good dancer and a she is a very talented girl"

# 1) replace() method         ----------------------->>>> it will replace a particular thing with another

print(string.replace(" ", "_"))                                  # it will replace space by underscore
print(string.replace("is", "was"))                               # it will replace all is by was
print(string.replace("is", "was", 1))                            # it will replace first is to was
print(string.replace("is", "was", 2))                            # it will replace both 2 is to was

# 2) find() method            ------------------------>>>> it is used to find a letter

print(string.find("is", 8))                                       # it will search second is position


# It will  tell the position of second "is"

is_pos1 = string.find("is")
is_pos2 = string.find("is", is_pos1 + 1)
print(is_pos2)
