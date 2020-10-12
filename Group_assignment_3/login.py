
# part A, B and C work

#username declaration
username = "Nathan"

#password enter function
def password_enter():
    password = input("What is your password? ") #ask the user for the password
    if password != ("1234"): # if wrong print below
        print("incorrect password")
        retry = input("Do you wish to try again? Enter yes or no in lowercase ") #prompt user for retry
        if "yes" in retry: #check if user said yes or no
            password_enter() #relaunch function
        else:
            exit() #quit
    else:
        print("Welcome", username) #else welcome user

#run the function
password_enter()