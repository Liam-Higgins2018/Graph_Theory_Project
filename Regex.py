# Thompsons Construction
# Liam Higgins

#Importing reqired functions from supplied python files
from ShuntYard import shunt
from Thompsons_Construction import compile

def followes(state):
    """Return the set of states that can be reached from state following e arrows"""
    # Create a new set, with state as its only member
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
    # the currentState set of states and the nextState set of states
    currentState, nextState = set(), set()
    # Add the initial state to the currentState set
    currentState |= followes(nfa.initial)
    # loop through set of character in the string
    for s in string:
        # Loop through the currentState set of states
        for c in currentState:
            # Check if that state is labelled s
            if c.label == s:
                # Add the edge1 state to the nextState set
                nextState |= followes(c.edge1)
        # Set currentState to nextState, and clear out nextState
        currentState = nextState
        nextState  = set()
    # Check if the accept state is in the set of currentState states
    return (nfa.accept in currentState)