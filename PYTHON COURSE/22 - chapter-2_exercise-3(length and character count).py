# *************************************                            CHAPTER-2_EXRECISE-3                 *********************************** #

# QUESTION : TAKE TWO COMMA SEPERATED INPUTS FROM USER
# 1) USER'S NAME
# 2) A SINGLE CHARACTER

# OUTPUT : 2 PRINT LINES
# 1) USER'S NAME LENGTH
# 2) COUNT THE CHARACTER THAT USER INPUTED (IT SHOULD BE CASE INSENSITIVE COUNT)


# ***************************************************************             ANSWER                 ****************************************** #

name, single_character = input("Enter the following : name and single character comma seperated : ").split(",")

print(f"your name length is {len(name)} and your character count is {name.count(single_character)}")                         # CASE SENSITIVE

print(f"your name length is {len(name)} and your character count is {name.lower().count(single_character.lower())}")         # CASE INSENSITIVE

print(f"your name length is {len(name)} and your character count is {name.upper().count(single_character.upper())}")          # CASE INSENSITIVE

print(f"your name length is {len(name.strip())} and your character count is {name.strip().lower().count(single_character.strip().lower())}")         # it take cares if spaces

