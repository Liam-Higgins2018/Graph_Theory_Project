#Liam Higins
#Shunting Yard Algorithm

#"Infix means the string is going to be infix"
def shunt(infix):
  """The shunting yard algorithm for converting infix regular expressions
      to profix."""

  #allowed special characters
  specials = {'*': 50, '.': 40, '|': 30}

  #Pofix regular expression // eventually be the output
  pofix = ""
  #Working string  (push operators in and then take them off)
  stack = ""
    #Loop through the string one charcter at a time
  for c in infix:
    #If an open bracket, push to the stack
    if c == '(':
      stack = stack + c
    #If a closing bracket, pop from the stack, push to output until open bracket
    elif c == ')':
        while stack[-1] != '(':
            pofix, stack = pofix + stack[-1],stack[:-1]
        stack = stack[:-1]
    #If it's an operator, push to stack after popping lower or equal precedence
    #operators from top of stack into output
    elif c in specials:
        while stack and specials.get(c,0) <= specials.get(stack[-1],0):
          pofix, stack = pofix + stack[-1],stack[:-1]
        stack = stack + c
      #Regular characters are pushed immediately to the output
    else:
      pofix = pofix + c

#Pop all remaining operators from stack to output
  while stack:
         pofix, stack = pofix + stack[-1],stack[:-1]
  #Returns postfix regex
  return pofix

#print(shunt("(a.b)|(c*.d)"))



#Represents a state with two arrows, labelled by label
#Use None for a label representing "e" arrows
class state:
  label = None
  edge1 = None
  edge2 = None

#NFA is represented by its initial and accept states
class nfa:
  initial = None
  accept = None

  def __init__(self, initial, accept):
        self.initial = initial
        self.accept = accept

def compile(profix):
  """ compiles a postfix regular expression into an NFA."""

        nfastack = []
  
    for c in profix:
  
        if c == '.':
            #Pop 2 states off the stack
            nfa2 = nfastack.pop()
            nfa1 = nfastack.pop()
            #Connect the first NFA's state to the second initial
            nfa1.accept.edge1 = nfa2.initial
            #Push new NFA's to the stack
            newnfa = nfa(nfa1.initial, nfa2.accept)
            nfastack.append(newnfa)
        elif c == '|':
            #Pop 2 states off the stack
            nfa2 = nfastack.pop()
            nfa1 = nfastack.pop()
            #Create a new initial state,connect it to initial states of NFA1 and NFA2
            initial = state()
            initial.edge1 = nfa1.initial
            initial.edge2 = nfa2.initial
            #Create a new accept state, connecting the two accept states of the two nfa's popped from the stack to the new state
            accept = state()
            nfa1.accept.edge1 = accept
            nfa2.accept.edge2 = accept
            #Push new NFA's to the stack
            newnfa = nfa(initial, accept)
            nfastack.append(newnfa)
        elif c == '*':
            #Pop a single nfa from the stack
            nfa1 = nfastack.pop()
            #Create new initial and accept states
            initial = state()
            accept = state()
            #Join the new initial state to nfa1's initial state and the new accept state
            initial.edge1 = nfa1.initial
            initial.edge2 = accept
            #Join the old accept state to the new accept state and nfa1's initial state
            nfa1.accept.edge1 = nfa1.initial
            nfa2.accept.edge2 = accept
            #Push new nfa to the stack
            newnfa = nfa(initial, accept)
            nfastack.append(newnfa)
        else:
            #Create new initial and accept states
            accept = state()
            initial = state()
            #Join the initial state to the accept state using an arrow labelled c
            initial.label = c
            initial.edge1 = accept
            #Push new nfa to the stack
            newnfa = nfa(initial, accept)
            nfastack.append(newnfa)
    
  #NFA stack should only have a single nfa on it at this point
  return nfastack.pop()

#print(compile("ab.cd.|"))
#print(compile("aa.*"))

def followes(state):
  """Return the set of states from state following e arrows"""
  #Create a new set with state as its only member
  states = set()
  states.add(state)

    #Check if state has arrows labelled e from it 
    if state.label is None:
        #Check if edge1 is a state 
        if state.edge1 is not None:
            #if theres an edge1 follow it
            states |= followes(state.edge1)
            #Check if edge2 is a state
        if state.edge2 is not None:
            #if theres an edge2 follow it
            states |= followes(state.edge2)

    # Return the set of states.
    return states


# A few tests
infixes = ["a.b.c", "a.(b|d).c", "(a.(b.b)*.c"]
strings = ["", "abc", "abbc", "abcc", "abad","abbc"]

for i in infixes:
    for s in strings:
        print(match(i, s), i, s)

