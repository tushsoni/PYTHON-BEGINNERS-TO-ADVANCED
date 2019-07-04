#  ***************************************              CHAPTER-3_EXERCISE-1             *************************************#\

# QUESTION : MAKE A VARIABLE LIKE winning_number and assign any number to it , ask user to guess a number , if user guessed correctly then print "YOU WIN !!!!" 
# if user did'nt guessed correctly then :
#  1) if user guessed lower than actual number then print "too low"
#  2) if user guessed higher than actual number then print "too high"

# bonus : : : google "how to generate random number using python" to generate random number
               #winning number



# ******************************************************                    ANSWER               ******************************************************* #


winning_number = 13

guessed_number = int(input("Enter a number between 1 to 20 : "))



if winning_number == guessed_number:
    print("You win the game")

else:                                              # It is called as NESTED IF-ELSE (it contain if in else that's why)
    if guessed_number < winning_number:
        print("too low")

    if guessed_number > winning_number: 
        print("too high")

