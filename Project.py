# Thompsons Construction
# Liam Higgins

#Importing reqired functions from supplied python files
from ShuntYard import shunt
from Thompsons_Construction import compile

def followes(state):
    """Return the set of states that can be reached from state following e arrows"""
    # Create a new se, with state as its only member
    states = set()
    states.add(state)
    # Check id state has arrows labelled e from it
    if state.label is None:
        # Check if edge1 is a state
        if state.edge1 is not None:
            # if theres an edge1, follow it
            states |= followes(state.edge1)
        # Check if edge2 is a state 
        if state.edge2 is not None:
            # If there's an edge2, follow it
            states |= followes(state.edge2)
    # Return the set of states
    return states


def match(infix, string):
    """Matches string to infix regular expression"""
    # shunt and compile the regular expression
    postfix = shunt(infix)
    nfa = compile(postfix)
    # the current set of states and the next set of states
    current, next = set(), set()
    # Add the initial state to the current set
    current |= followes(nfa.initial)
    # loop through set of character in the string
    for s in string:
        # Loop through the current set of states
        for c in current:
            # Check if that state is labelled s
            if c.label == s:
                # Add the edge1 state to the next set
                next |= followes(c.edge1)
        # Set current to next, and clear out next
        current = next
        next  = set()
    # Check if the accept state is in the set of current states
    return (nfa.accept in current)
# A few tests

options = int(input("\nPlease enter:\n 1) To read a sample test of regular expressions and strings\n " +
                        "2) To input custom user regular expressions and strigs\n 3) To exit the code\n\n"))

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
        
    options = int(input("\nPlease enter:\n 1) To read a sample test of regular expressions and strings\n 2) To input custom user regular expressions and strigs\n 3) To exit the code\n\n"))

