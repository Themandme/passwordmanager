from Class import password
#Main menu
def lead():
    print("What would you like? (add/delete/quit)")
    if input() == "add":  
        addpassword()
        repeat()
#Function to add password
def addpassword():
    print("What is the password?")
    input(password)
    print(password)
#Function to ask user about more passrods
def repeat():
    print("Add another passwword? (yes/no)")
    if (input() == "yes"):
        addpassword()
    elif (input() == "no"):
        lead()
    else:
        print("Invalid input")
        repeat()
#Displays database of passwords
def base():
    print (password)
    lead()
lead()