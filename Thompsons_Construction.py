#Thompsons Construction
#Liam Higgins

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