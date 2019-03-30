#Main Menu
#Liam Higgins

#Importing reqired functions from supplied python files
from Regex import match, followes

def Menu():
    """Main Menu of Project"""
#Displays Options to the user and takes in their input
options = int(input("\nPlease enter:\n 1) To read a sample test of regular expressions and strings\n " +
                        "2) To input custom user regular expressions and strigs\n 3) To exit the program\n\n"))

#Loops through statements prompting the user until they Quit out of the menu 
while True:
    if options == 1:
        #Sample Regular Expressions and Strings
        infixes = ["a.b.c*", "a.(b|d).c*", "(a.(b|d))*", "a.(b.b)*.c"]
        strings = ["", "abc", "abbc", "abcc", "abad", "abbbc"]

        for i in infixes:
            for s in strings:
                print(match(i, s), i, s)

    elif options == 2:
        #Custom user infix and string
        userInfix = input("Please enter your regular expression in the infix notation: ")
        userString = input("Please enter a string to compare against your infix notation: ")
        print(match(userInfix, userString), userInfix, userString)
    
    elif options == 3:
        print("Goodbye!!\n")
        break

    else:
        #User Validation 
        print("Error Invalid Input\n")
        
    options = int(input("\nPlease enter:\n 1) To read a sample test of regular expressions and strings\n " +
                        "2) To input custom user regular expressions and strigs\n 3) To exit the program\n\n"))

