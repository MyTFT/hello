#Chris Gintz
#04/07/2026 - 04/09/2026
#CS50 Journey
#This program will ask the user for their name and then greet them.

# Ask the user for their name and store in a variable called yourName.
#yourName = input("What's your name? ")

# Outputs a greeting to the user using their name.
#print ("Hello, " + yourName + "!")

#Edit of a cloned repository in my GitHub account, originally pulled via visual studio
#through the Powershell terminal.

#Opened file in powershell via devenv.exe and made edits to the code, then committed 
#and pushed the changes back to GitHub.
#print ("V.2")

#Test to see add to branch off main to merge later.

#Create new function called hello()



def main():
    yourName = input("What's your name? ")
    #when hello is called, it will take the value of yourName and pass it to the parameter to in the hello function.
    hello(yourName)
    

def hello(to):
    #to is a local variable that is only used within the hello function. 
    #It is a parameter that takes in the value of yourName when the function is called in main.
    print("hello,", to)
main()


#Can chain multiple functions together.
#yourName = input("What's your name? ").strip().title()





