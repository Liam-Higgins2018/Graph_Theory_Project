#Shuntin Yard Algorithm
#Liam Higgins

#Shunting Yard Algorithm in the ShuntingYard.py file
def shunt(infix):
    """The Shunting Yard Algorithm for converting infix regular expressions 
    to postfix."""
    # special characters for regular expressions and their precidence
    specials = {'*': 50, '+': 50, '?': 50, '.': 45, '^' : 40, '$': 40, '|': 30}
    # will eventually be the output
    pofix = ""
    # operator stack
    stack = ""
    # loop throuh the string a character at a time
    for c in infix:
        # If an open bracket, push to the stack
        if c== '(':
            stack = stack + c
        # If a closing bracket, pop from the stack, push to output until open bracket
        elif c == ')':
            while stack[-1] != '(':
                pofix  = pofix + stack[-1]
                stack = stack[:-1]
            stack = stack[:-1]
        # If it's an operator, push to the stack after popping lower or equal precedence
        # operators from top of stack into output
        elif c in specials:
            while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
                pofix  = pofix + stack[-1]
                stack = stack[:-1]
            stack = stack + c
        # Regular characters are pushed immediately to the output
        else:
            pofix = pofix + c
    # Pop all remaining operators from the stack to output
    while stack:
        pofix  = pofix + stack[-1]
        stack = stack[:-1]
    # Return postfix regex
    return pofix