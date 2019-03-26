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

print(shunt("(a.b)|(c*.d)"))

