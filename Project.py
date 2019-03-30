# Thompsons Construction
# Liam Higgins

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

# Represents a state with two arrows labelles by label
# Use None for a label represenring "e" arrows
class state:
    label, edge1, edge2 = None, None, None
# An NFA is a represented by its initial and accept states
class nfa:
    initial, accept = None, None

    def __init__(self, initial, accept):
        self.initial = initial
        self.accept = accept 

def compile(profix):
    """Compiles a postfix regular expression into a NFA"""
    nfastack = []

    for c in profix:
        if c == '.':
            # pop two NFA's off the stack
            nfa2, nfa1 = nfastack.pop(), nfastack.pop()
            # Connect first NFA's accept state to the second's initial.
            nfa1.accept.edge1 = nfa2.initial
            # Push NFA to the stack
            nfastack.append(nfa(nfa1.initial, nfa2.accept))
        elif c == '|':
            # pop two NFA's off the stack
            nfa2, nfa1 = nfastack.pop(), nfastack.pop()
            # Create a new initial state, connect it to initial states
            # of the two NFA's popped from the stack.
            initial = state()
            initial.edge1, initial.edge2 = nfa1.initial,nfa2.initial
            # Create a new accept state, connecting the new accept states
            # of the thwo NFA's popped from the stack, to the new state.
            accept = state()
            nfa1.accept.edge1, nfa2.accept.edge1 = accept, accept
            # Push new NFA to the stack
            newnfa = nfa(initial, accept)
            nfastack.append(newnfa)
        elif c == '+':
            # pop two NFA's off the stack
            nfa2, nfa1 = nfastack.pop(), nfastack.pop()
            # Create a new initial state, connect it to initial states
            # of the two NFA's popped from the stack.
            initial = state()
            initial.edge1 = nfa1.initial
            # Create a new accept state
            accept = state()
            #Connect the first edge of nfa1's accept back to nfa1's initial
            nfa1.accept.edge1 = nfa1.initial
            #Connect the second edge of nfa1 to the initial state of nfa2
            nfa1.accept.edge2 = nfa2.initial
            #Connect nfa2 to the accept state
            nfa2.initial.edge1 = accept
            # Push new NFA to the stack
            newnfa = nfa(initial, accept)
            nfastack.append(newnfa)
        elif c == '?':
            #Pop a single NFA from the stack
            nfa1 = nfastack.pop()
            #Create an initial and accept state
            initial, accept = state(), state()
            #Join the initial state to the nfa1's initial
            #and to the accept state
            initial.edge1 = nfa1.initial
            initial.edge2 = accept
            #Connect nfa1's accept state to the accept state
            nfa1.accept.edge1 = accept
            #Pushes the new nfa to the stack
            newnfa = nfa(initial, accept)
            nfastack.append(newnfa)
        elif c == '^':
            #Pop a single NFA from the stack
            nfa1 = nfastack.pop()
            #Create the initial and accept state
            initial, accept = state(),state()
            #Join the initial state to the nfa1's initial
            initial.edge1 = nfa1.initial
            #Connect the nfa1's accept state to the accept state
            nfa1.accept.edge1 = accept
            #Pushes the new nfa to the stack
            newnfa = nfa(initial, accept)
            nfastack.append(newnfa)
        elif c == '$':
            #Pop two NFA's from the stack
            nfa1, nfa2 = nfastack.pop(), nfastack.pop()
            #Creates an initial state
            initial = state()
            #Let's nfa1's initial state be the accept state
            accept = nfa1.initial
            #Connects the initial state to the initial state of nfa2
            initial.edge1 = nfa2.initial
            #Connects the nfa2's accept state to the initial state of nfa1
            nfa2.accept.edge1 = nfa1.initial
            #Connects the accept state of nfa1 back to the initial state of nfa1
            nfa1.accept.edge1 = nfa1.initial
            #Connects the accept state of nfa1 to the initial state of nfa2
            nfa1.accempt.edge2 = nfa2.initial
            #Pushes the nes nfa to the stack
            newnfa = nfa(initial, accept)
            nfastack.append(newnfa)
        elif c == '*':
            # Pop a single NFA from the stack
            nfa1 = nfastack.pop()
            # Creat new initial and accept states
            initial, accept = state(), state()
            # Join the new initial state to nfa1's
            # initial state and the new accept state
            initial.edge1 = nfa1.initial
            initial.edge2 = accept
            # Join the old accept state to the new accept
            # state and nfa1's initial state
            nfa1.accept.edge1 = nfa1.initial
            nfa1.accept.edge2 = accept
            # Push new NFA to the stack
            newnfa = nfa(initial, accept)
            nfastack.append(newnfa)
        else: 
            # Create new initial and accept states
            accept, initial  = state(), state()
            # Join the initial state and the accept state
            # using an arrow labelled c.
            initial.label = c
            initial.edge1 = accept
            #Push new NFA to the stack
            newnfa = nfa(initial, accept)
            nfastack.append(newnfa)
    # nfastack should only have a single nfa on it at this point
    return nfastack.pop()


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

options = int(input("\nPlease enter:\n 1) To read a sample test of regular expressions and strings\n 2) To input custom user regular expressions and strigs\n\n"))

if options == 1:
    #Sample Regular Expressions and Strings
    infixes = ["a.b.c*", "a.(b|d).c*", "(a.(b|d))*", "a.(b.b)*.c"]
    strings = ["", "abc", "abbc", "abcc", "abad", "abbbc"]


    for i in infixes:
        for s in strings:
            print(match(i, s), i, s)

elif options == 2:
    userInfix = input("Please enter your regular expression in the infix notation: ")
    userString = input("Please enter a string to compare against your infix notation: ")
    print(match(userInfix, userString), userInfix, userString)
