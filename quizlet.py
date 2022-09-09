## Script that takes in Strings & puts them inside lists
## Made to create quizlets easier by copying text from docs
## Prints out results on the console, copy between the two borders


term = []
definition = []
status = True

while status:
        ## Insert quizlet terms
        ## inserting end moves to next section
        user_input = input("Insert your term list (enter : end to go next)\n")
        if user_input == "end":
                status = False
        else:
                term.append(user_input);
                

while status == False:
        ## Insert quizlet definitions
        ## Inserting end prints out results
            user_input = input("Insert your def list (enter : end to go next)\n")
            if user_input == "end":
                    status = True
            else:    
                    definition.append(user_input)


                    
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
x = 0
## Recurses through entire list & prints out the terms & definitions
## Formatted like: term,definition
while x < len(definition):
        print("\n")
        print("\n" + term[x] + "," + definition[x] + "\n\n\n")
        x +=1
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\n\n")


## Incase the user accidentally inserts the strings in the wrong order
## There is an option available to flip the lists around
user_input = input("Need to swap the order? (y/n)\n")
if user_input == "y" or user_input == "Y":
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        x = 0
        while x < len(definition):
                print("\n\n" + definition[x] + "," + term[x] + "\n\n\n")
                x +=1
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
else:
        print("\n\nEnd Program\n\n")
        
