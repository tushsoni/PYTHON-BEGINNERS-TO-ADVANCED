name = "                    Tu    shar              "
dots = "......................."

# lstrip()                         -------------------->>>>>>  it deletes all left spaces
# rstrip()                         -------------------->>>>>> it deletes all right spaces
# strip()                          -------------------->>>>>> it delets both left and right spaces
# replace(" ", "")                 -------------------->>>>>> it means it replaces middle spaces

print(name.lstrip() + dots)
print(name.rstrip() + dots)
print(name.strip() + dots)
print(name.replace(" ", "") + dots)