# Instructions on how to use the program

To run the program the user must navigate to the program location on their computer. The user then must enter “python menu.py” command to run the program. On execution the user will be displayed several options to which they can choose from.

-	Option 1:	The user enters ‘1’ into the console when prompted to from the menu. From here a series of infix notation regular expressions will be compared against a series of strings. The output will be printed out to the console which will display the infix regular expression, the string the regular expression was compared to and ‘True’ or ‘False’ depending whether the regular expression could pass through the string. Example (a.b.c*, abcc would return True, and a+ , b would	return False).

-	Option 2:	The user enters ‘2’ into the console when prompted to from the menu. The user will then be prompted to enter their own custom infix regular expression. The user will then be prompted to enter their custom string		that they wish to compare against their regular expression. The output 	will display the regular expression, the string and ‘True’ or ‘False’	depending whether the regular expression can pass through the string.	Example (a. , aaa would return true).

-	 Option 3:	The user enters ‘3’ into the console when prompted to from the menu. When this option is selected the user will exit the menu and the	program, after being displayed a message saying “Goodbye!!” to the user.

-	Other:	If the user enters anything outside of the options that user is prompted for an error message will be displayed to the user saying “Error	Invalid Input”. The user will then be given the opportunity to enter the correct input again.


# Architecture of the program

I decided to incorporate what I have learned from previous modules and apply them to this project. I split each python function in its own class as we were thought in Object Oriented Programming (OOP) to increase code efficiency. 

 - Menu Class	 This is the class that is going to be called first when the project is first ran. It will display the user interface to the console prompting the user for input to various options.
 
- Regex Class	 This class is responsible for matching the string with the regular expression and Returning the set of states that can be accessed from the state by following the e arrows

- ShuntYard Class 	This class is responsible for converting the infix regular expression into the postfix notation. It will loop through the regular expression one character at a time. If an open bracket ’(’ is encountered it will push the character to the stack, and if a ‘)’ is encountered it will pop the character from the stack. It also pushed operators to the stack after popping lower or equal precedence operators from the top of the stack.

- Thompsons_Construction Class	This class is responsible for pushing a postfix regular expression into an NFA, whenever an operator is encountered the appropriate nfa will be exectudted.
