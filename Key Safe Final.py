from sys import exit                                                                            # Import python defined native exit function
import sys,re,os                                                                                # Import system, read expression, operating system modules                                                              
def startMenu():                                                                                # Defining the 'startMenu()' Function
    global userApps,userPasswords,userPincode,userName,userEmail                                # Declare Global Variables
    clr()                                                                                       # Calls the 'clr()' function, blanks 50 lines.
    sys.tracebacklimit=0                                                                        # Classifies traceback limit 
    print("Welcome to Key Safe".center(40, ' ')+"\n"+"-"*40+"")                                  # Prints program title and information about the program
    print("Enter the number of the desired function:\n\n",                                      # <--
          "1)  Login With existing Account\n",                                                  #    |
          "2)  Create new Account\n",                                                           #    | Prints start menu
          "3)  Information\n",                                                                  #    |
          "4)  Exit\n")                                                                         # <--
    while True:                                                                                 # New Loop
        try:                                                                                    # Do below until except
            userChoice=int(input(" - "))                                                        # User inputs there choice of function, either 1,2 or 3
            if userChoice in range(1,5):                                                        # If choice is either 1,2 or 3 then go below
                break                                                                           # Break out of loop
            else:                                                                               # If a number but not 1,2 or 3 go below
                print("Please only enter numbers on the menu!")                                 # Print "Please only enter numbers on the menu!"
        except ValueError:                                                                      # If a string then go below
            print("Please only enter numbers on the menu!")                                     # Print "Please only enter numbers on the menu!"
    if userChoice == 1:                                                                         # If the user input "1"
        userLogin()                                                                             # Calls user login Function
    if userChoice == 2:                                                                         # If the user input "2"
        clr()                                                                                   # Call 'clr()' Function
        userNameChange()                                                                        # User inputs their name (Function will return)
        print("Greetings, "+userName+".")                                                       # Greet user
        userEmailChange()                                                                       # User inputs their Email Address (Function will return)
        userPincodeChange()                                                                     # User Inputs their login Pincode (Function will return)
        emailData=(userEmail.split("@")[1]).split(".")[0].capitalize()                          # Grabs the provider (josh.boag@Npbhs.com, "Npbhs" in this email)
        userApps=[str(emailData),'Code avengers','Python turtle']                               # Defines 3 Default Apps for the user
        userPasswords=['undefined','undefined','undefined']                                     # Defines 3 Default Passwords for the apps above for the user
        exportData()                                                                            # Exports user data to text file
        print("-"*60,"\nYour account has been created, "+userName+"!","\nYour Login Email:",userEmail,"\nYour Pincode:",userPincode,"\nYou have been given 3 default apps: \n\t- "+emailData.capitalize()+"\n\t- Code Avengers\n\t- Python Turtle\nThe default passwords for these are: 'undefined'\nYou can change this in the 'Change an existing password' menu setting\n\nEnjoy!\n"+"-"*60,"\n"*2) # Prints Welcome statement (Only runs once)
        mainMenu()                                                                              # User is taken to the main menu function
    if userChoice == 3:                                                                         # If the user input 3
        clr()                                                                                   # Clears window
        print("Welcome To Key Safe".center(60," ")+"\n"+"-"*60+"\n"+"\n\tKey Safe is a password storing programme developed\n"+"\tin Python. In this programme I added functionality\n"+"\tto View/Add/Change/Remove Apps and their\n"+"\tpasswords.  I have tried to make this programme\n"+"\teasy to use.\n"+"\n\tIn the numbered Menus, simply type the number of\n"+"\tthe desired function you want to access.\n"+"\n\t- Josh")
        input("\nPress ENTER to continue...")                                                   # After the user has read the information
        startMenu()                                                                             # Repeats the start menu()
    if userChoice == 4:                                                                         # If the user input in 4 in the start menu
        clr()                                                                                   # Clears screen
        endProgram(str("Thank you! Have a good day!\nClosing..."))                              # Calls endProgram Function

def encrypt(txt):                                                                               # Rotation Encryption function (5 forward alphabetical rotations)
    encrypted = ''                                                                              # Clears string cache
    for i in txt:                                                                               # New loop (len of txt)
        c = ord(i)+5                                                                            # Ord gets the ASCII value for a character and increases its value by 5
        if ord(i) != c:                                                                         # If c is a new character
            b = chr(c)                                                                          # b equals the character of the ASCII value
            encrypted += b                                                                      # Adds each character to the encrypted string
    encrypted=str(encrypted.replace("\\","#"))                                                  # Replaces special characters so that a text file can be created
    encrypted=str(encrypted.replace("|","%"))                                                   # Replaces special characters so that a text file can be created
    return encrypted                                                                            # Returns this string when the function is called

def decrypt(txt):                                                                               # Rotation Decryption function (5 backward alphabetical rotations)
    txt.replace('#','\\')                                                                       # Replaces special characters so that the string can be decrypted
    txt.replace('%','|')                                                                        # Replaces special characters so that the string can be decrypted
    decrypted = ''                                                                              # Clears string cache
    for x in txt:                                                                               # New loop (len of txt)
        c = ord(x)-5                                                                            # Ord gets the ASCII value for a character and decreases its value by 5                                                      
        if ord(x) != c:                                                                         # If c is a new character
            b = chr(c)                                                                          # b equals the character of the ASCII value
            decrypted += b                                                                      # Adds each character to the encrypted string
    return decrypted                                                                            # Returns this string when the function is called

def endProgram(reason="Closing..."):                                                            # EndProgram Function name defined (With default reason)
    global userPincode,userEmail                                                                # Declares Global variables
    print(reason)                                                                               # Prints the reason (Default:"Closing...")
    userPincode=""                                                                              # Clears user data
    userEmail=""                                                                                # Clears user data
    exit(0)                                                                                     # Stops the program from running

def clr():                                                                                      # Defines clr function
    print("\n"*50)                                                                              # Creates a new line 50 times
    return ''                                                                                   # Return to where it was called

def userPincodeChange():                                                                        # Defines Pincode change function
    global userPincode                                                                          # Declares Global Variables
    while True:                                                                                 # New Loop
        print("Your new Pincode must:\n\t- Be longer than 8 characters\n\t- Contain at least 1 Lowercase letter\n\t- Contain at least 1 Uppercase letter\n\t- Contain at least 1 number\n") # Prints pincode Rule statement
        userPincode= input("Input your pincode: \n - ")                                         # User inputs their desire pincode
        if len(userPincode) <= 7 :                                                              # If the length of the picode is 7 or less
            clr()                                                                               # Clears the window
            print("Must be at least 8 characters\n")                                            # Prints error (User will have to input again)
        if ' ' in userPincode:                                                                  # If a space is in user input
            clr()                                                                               # Clears window
            print("Must not contain spaces!\n")                                                 # Prints error (User will have to input again)
        if len(userPincode) >= 20:                                                              # If the user input is greater than 20 charaters
            clr()                                                                               # Clears window
            print("Must be shorter than 20 characters\n")                                       # Prints error (User will have to input again)
        if not re.search("[a-z]",userPincode):                                                  # If there are non lowercase a-z letters then print error and retry
            clr()                                                                               # Clears window
            print("Must contain lowercase\n")                                                   # Prints error (User will have to input again)
        if not re.search("[0-9]",userPincode):                                                  # If the user input does not contain a number then error and retry
            clr()                                                                               # Clears Window
            print("Must contain a number\n")                                                    # Prints error (User will have to input again)
        if not re.search("[A-Z]",userPincode):                                                  # If there are non uppercase A-Z letters then print error and retry
            clr()                                                                               # Clears Window
            print("Must contain a least 1 uppercase\n")                                         # Prints error (user will have to input again)
        if len(userPincode) > 6 and len(userPincode) < 20 and re.search("[A-Za-z0-9]",userPincode) and not ' ' in userPincode: # If the input contains an uppercase and lowercase letter, has a number and no spaces then pass
            clr()                                                                               # Clears Window
            return                                                                              # Returns to where it was called
        else:                                                                                   # else statement incase of some random error that I cant work out ;)
            clr()                                                                               # Clear Window
            print("Please make sure your new pincode follows the rules.")                 # Prints error and the user must retry

def userDelete():                                                                               # New function for when the user wants to delete the account    menuAsk("Are you sure you want to delete your account: (Yes or No)")
    menuAsk("WARNING:  THIS ACTION CANNOT BE UNDONE!\nAre you sure you want to delete this account?\n!") # Warns the user of this action, user must input user or no
    if outcome == True:                                                                         # If the returned value is True 
        os.remove(encrypt(re.sub('[0-9]+', '', userEmail))+".txt")                              # The os module will grab the encrypted file name and remove it from the file
        endProgram("Account terminated")                                                        # Ends the program
    else:                                                                                       # else
        clr()                                                                                   # Clears the window
        print("Action Cancelled!\n\nReturning to menu...")                                      # Print message
        mainMenu()                                                                              # Returns to menu

def menuAsk(msg="\nWould you like to return to the menu? (Yes or No)"):                         # This is a module for asking the user if they would want to go to the main menu. This means I dont have to have as many loops
    while True:                                                                                 # New Loop
        global Polar,outcome                                                                    # Defines global Variables
        print(msg)                                                                              # Prints defined message (Default:"Would you like to return to the menu? (Yes or No)")
        Polar=str(input(" - ")).lower()                                                         # Polar means yes or no. User must input either yes or no
        if 'y' in Polar:                                                                        # If there is a y in the user input
            outcome=True                                                                        #  - Then outcome will be true
            return outcome                                                                      # Returns true
        if 'n' in Polar:                                                                        # If there is a n in the user input
            outcome=False                                                                       #  - Then outcome will be false
            return outcome                                                                      # Returns false
        else:                                                                                   # Else
            print("Please enter either Yes or No")                                              # Prints error message, will require the user to input again                       
            continue                                                                            # Continues to loop again

def importData():                                                                               # Imports encrypted data from text file into decrypted strings which go into corrosponding variables 
    global userApps,userPasswords,userPincode,fileName,userName                                 # Defines Global Variable names
    userPincode=decrypt(fileName[1])                                                            # Declares pincode for the second line in the users file
    userName=decrypt(fileName[2])                                                               # Declares users name for the third line in the users file
    userApps=[]                                                                                 # Defines app list
    userPasswords=[]                                                                            # Defines passwords list
    fileName=list(fileName)                                                                     # converts fileName as a list
    for app in range(0,len((fileName[3]).split(","))):                                          # New loop (length of list in the fourth line)
        userApps.append(decrypt((fileName[3]).split(",")[app]))                                 # Each item in the fourth line is added to the userApps list
    for password in range(0,len((fileName[4]).split(","))):                                     # New loop (length of list in the fifth line)
        userPasswords.append(decrypt((fileName[4]).split(",")[password]))                       # Each item in the fifth line is added to the userPasswords list

def exportData():                                                                               # Exports encrypted strings of user data from the program and puts it neatly into a list
    fileName=open(encrypt(re.sub('[0-9]+', '', userEmail))+".txt","w+")                         # Sets a encrypted file name (removes numbers due to windows not liking special characters) also creates a new file if one doesnt already exist
    fileName.write("{}\n{}\n{}\n".format(encrypt(userEmail),encrypt(userPincode),encrypt(userName))) # Writes encrypted strings for user Email,Pincode and Name and stores each item on new line
    for i in range(0,len(userApps)):                                                            # New loop for each item in userApps list 
        if i == (len(userApps)-1):                                                              # <--
            fileName.write("{}".format(encrypt(userApps[i])))                                   #    |   Places a comma at the end of each item (except the last item) 
        else:                                                                                   #    |   This is for when the strings get imported they are easy for the program to read and seperate
            fileName.write("{}".format(encrypt(userApps[i]))+",")                              # <--
    fileName.write("\n")                                                                        # New line to seperate items
    for i in range(0,len(userPasswords)):                                                       # New loop for each item in userPasswords list
        if i == (len(userPasswords)-1):                                                         # <--
            ending=""                                                                           #    |  Places a comma at the end of each item (except the last item) 
        else:                                                                                   #    |  This is for when the strings get imported they are easy for the program to read and seperate
            ending=","                                                                          #    |
        fileName.write("{}".format(encrypt(userPasswords[i]))+ending)                           # <--
    fileName.close()                                                                            # Closes the file (saves)
    
def passwordFind():                                                                             # Function for find the password in a list
    global userApps,userPasswords                                                               # Declares global variabes
    while True:                                                                                 # New loop
        clr()                                                                                   # Clears window
        print("Displaying",len(userApps),"Apps/Websites")                                       # Prints the ammount of apps there are in the userApps list
        print("".ljust(10)+"App:".ljust(22)+"Password:\n")                                      # Prints the title for the App and Password columns
        for index in range(0,len(userApps)):                                                    # New loop For the ammount of apps in userApps
            print("".ljust(10)+userApps[index].ljust(20)+"\t"+"*"*len(userPasswords[index]))    # Prints app and hidden password
        userChoice=str(input("\nType 'All' to display all Apps/websites and their Passwords.\nWhat Website/App would you like to find the password for: ")).capitalize()# New user input
        if userChoice == "All":                                                                 # If the user inputs "All"
            clr()                                                                               # Clears window
            print("Displaying all Apps/Websites and their Passwords.")                          # Prints statement
            print("".ljust(10)+"App:".ljust(22)+"Password:\n")                                  # Prints header of columns
            for index in range(0,len(userApps)):                                                # New loop For the ammount of apps in userApps
                print("".ljust(10)+userApps[index].ljust(20)+"\t"+userPasswords[index])         # Prints all apps and shown passwords
            menuAsk()                                                                           # Calls menuAsk() Function
            if outcome == True:                                                                 # If returned True
                clr()                                                                           #  - Clears window
                mainMenu()                                                                      #  - Returns to main menu
            else:                                                                               # Else
                continue                                                                        # Goes to top of function
        if userChoice in userApps:                                                              # If the user input is within the userApps list
            clr()                                                                               # Clears window
            print("".ljust(10)+"App:".ljust(22)+"Password:\n")                                  # Prints Header column
            print("".ljust(10)+str(userApps[userApps.index(userChoice)]).ljust(22)+str(userPasswords[userApps.index(userChoice)])) # Prints that specific app and password the user asked for
            menuAsk()                                                                           # Calls menuAsk() Function
            if outcome == True:                                                                 # If the user input yes in menuAsk() equals true
                clr()                                                                           # Clears window
                mainMenu()                                                                      # Goes to the main menu
            else:                                                                               # Else
                continue                                                                        # Goes to the top of the function and repeats input
        if not userChoice in userApps:                                                          # <---
            clr()                                                                               #     |
            print("\n"+userChoice,"does not seem to exist. Would you like to add it? (Yes or No)") #  |
            menuAsk("")                                                                         #     |
            if outcome == True:                                                                 #     | If the user input an app that was not in userApps then
                addApp(str(userChoice))                                                         #     | they get the option to add it to the userApps list.
                menuAsk()                                                                       #     | If decide they want to add it then they go to a seperate 
                if outcome == True:                                                             #     | function.
                    clr()                                                                       #     | If they do not want to add it then they have a
                    mainMenu()                                                                  #     | choice if they want to go the menu or not
                else:                                                                           #     | The entire function will run again if they do not want
                    continue                                                                    #     | to go to the main menu.
            else:                                                                               #     |
                menuAsk()                                                                       #     |
                if outcome == True:                                                             #     |
                    clr()                                                                       #     |
                    mainMenu()                                                                  #     |                              
                else:                                                                           #     |
                    continue                                                                    # <---

def passwordChange():                                                                           # The function if the user wants to change a password for an existing app
    global userPasswords                                                                        # Declare Global variables
    clr()                                                                                       # Clears the Window
    print("Please enter the number for the password you want to change:")                       # Prints instruction
    print("".ljust(10)+"App:".ljust(22)+"Password:\n")                                          # Prints column header
    for i in range(0,len(userApps)):                                                            # Starts new loop, for the ammount of items in userApps list
        print("".ljust(5),"{}".format(i+1)+").",userApps[i].ljust(20)+"\t"+"*"*len(userPasswords[i])) # Prints every app with a number list
    print("\n      {}). Cancel".format(i+2))                                                    # Prints a cancel button if the user does not wish to delete an app
    while True:                                                                                 # New loop
        try:                                                                                    # Try unless exception
            userChoice=int(input(" - "))                                                        # User inputs a number on the menu
            if userChoice in range(1,len(userApps)+1):                                          # If the number is on the menu
                while True:                                                                     # New loop
                    print("\rEnter the new password for", userApps[userChoice-1]+":")           # <--
                    newChoice=str(input(" - "))                                                 #    |  
                    if len(newChoice) >= 4:                                                     #    |   
                        userPasswords[userChoice-1]=newChoice                                   #    |  User inputs a new password for the app
                        exportData()                                                            #    |  
                        clr()                                                                   #    |
                        print("Password Sucessfully Changed! Returning to Menu...\n")           #    |
                        mainMenu()                                                              #    |
                    else:                                                                       #    |
                        print("It is recommended that you new password is longer than 4 characters!") #
                        continue                                                                # <--
            if userChoice == (len(userApps)+1):                                                 # If the user input is equal to Cancel
                clr()                                                                           # Clears Window
                print("Returning to menu...\n\n")                                               # Print Message
                mainMenu()                                                                      # Returns to menu
            else:                                                                               # Else
                print("Please only enter numbers on the menu")                                  # Print error message
        except ValueError:                                                                      # If the user input is a string rather than an Int
            print("Try Again! Please only enter numbers on the menu!")                          # Print Error message

def removeApp():                                                                                # Remove app
    global userPasswords,userApps                                                               # Declares global Variables
    clr()                                                                                       # Clears window
    print("Please state the number for the app you want to remove:")                            # Print instructions
    print("".ljust(10)+"App:".ljust(22)+"\n")                                                   # Print header columns
    for i in range(0,len(userApps)):                                                            # New Loop for each item in userApps list
        print("".ljust(5),"{}".format(i+1)+").",userApps[i].ljust(20))                          # Print all apps
    print("\n      {}). Cancel".format(i+2))                                                    # Print the cancel button
    while True:                                                                                 # New loop
        try:                                                                                    # Try unless exception
            userChoice=int(input(" - "))                                                        # User inputs a number on the list
            if userChoice in range(1,len(userApps)+1):                                          # If the user inputted a number that was on the list
                del userApps[userChoice-1]                                                      # Deletes that particular app
                del userPasswords[userChoice-1]                                                 # Deletes that particular password
                clr()                                                                           # Clears window
                print("App & Password Removed!\nReturning to menu...\n\n")                      # Prints our message
                mainMenu()                                                                      # Goes to main menu
            if userChoice == (len(userApps)+1):                                                 # If the user inputted the number to cancel
                clr()                                                                           # Clear window
                print("Returning to menu...\n\n")                                               # Prints message
                mainMenu()                                                                      # Goes to main menu
            else:                                                                               # Else
                print("Please only enter numbers on the menu")                                  # Prints error message
        except ValueError:                                                                      # If the input was a string
            print("Try Again! Please only enter numbers on the menu!")                          # Print error message

def addApp(new=""):                                                                             # Add app
    global userApps,userPasswords                                                               #
    if new != "":                                                                               # <----------
        clr()                                                                                   #            |  
        while True:                                                                             #            |
            print("Please enter a password for "+new+":")                                       #            | If the user adds a new app from findPassword()
            dataPassword=str(input(" - "))                                                      #            | the user inputs a password without having to
            if len(dataPassword) > 4:                                                           #            | retype the app name again
                userApps.append(new)                                                            #            |
                userPasswords.append(dataPassword)                                              #            |
                clr()                                                                           #            |
                print("App/Website Added!\n\tApp:\t\tPassword:\n\n\t"+new+"".ljust(22)+("*"*len(dataPassword))) #
                break                                                                           #            |
            else:                                                                               #            |
                clr()                                                                           #            |
                print("Try Again!\n\nIt is recommended that your password is more than 4 characters!")  #<---
    else:                                                                                       # else
        clr()                                                                                   # clears window
        while True:                                                                             # New loop
            print("Please enter the name of the Website/App:")                                  # Prints instruction
            userInput=str(input(" - ")).capitalize()                                            # User inputs the name of the app they want to add
            if userInput == "Cancel":                                                           # If the user inputted cancel 
                clr()                                                                           # Clears the screen
                mainMenu()                                                                      # Goes to menu
            if len(userInput) > 1:                                                              # If the app name is greater then the length of 1
                userApps.append(userInput)                                                      # Add app to list
                clr()                                                                           # Clear window
                while True:                                                                     # New loop
                    print("Please enter the password for "+userInput+":")                       # Print instructions
                    userChoice= str(input(" - "))                                               # User inputs the password for their app
                    if len(userChoice) > 4:                                                     # If the password lengh is greater than 4 characters
                        userPasswords.append(userChoice)                                        # Add the password to the password list
                        break                                                                   # Break out of loop
                    else:                                                                       # Else
                        print("Try Again!\n\nIt is recommended that your password is more than 4 characters!") # Print error
                        continue                                                                # Continue
                clr()                                                                           # Clears window
                print("App/Website Added!\n\tApp:\t\tPassword:\n\n\t"+userInput+"".ljust(10)+("*"*len(userChoice))) # Prints added apps abd passwords
                menuAsk("Would you like to add another app: (Yes or No)")                       # Ask the user if they want to add another app
                if outcome == True:                                                             # If they want to add a new app then this function will loop
                    continue                                                                    # Loop function
                else:                                                                           # Else
                    clr()                                                                       # Clears window
                    print("Returning to menu!\n")                                               # Prints message
                    exportData()                                                                # Exports user data to file
                    mainMenu()                                                                  # Goes to main Menu
            else:                                                                               # Else
                clr()                                                                           # Clears window
                print("Try Again!\n\nInput can not be left empty!")                             # Prints error message

def userLogin():                                                                                # This is the login Fucntion for my program
    global fileName,userEmail,userPincode                                                       # Declares global variables
    attempts= 3                                                                                 # The ammount of attempts the user can get is 3
    while attempts > 0:                                                                         # While the user still has attempts left
        try:                                                                                    # Try unless exception
            userEmail=str(input("Please enter your existing Email address: ")).lower()          # User inputs existing email address
            clr()                                                                               # Clears window
            if re.match(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", userEmail):        # If the Email passes an email checker
                fileName=open(encrypt(re.sub('[0-9]+', '', userEmail))+".txt","r").read().split()# attemps to open the email (Remove numbers due to encryption)
                if decrypt(fileName[0]) == userEmail:                                           # Verifies the input by checking it against the email in the file
                    break                                                                       # If they are the same then break
                else:                                                                           # Break
                    print("\nIncorrect email address")                                          # Else
            else:                                                                               # Print error and the user will have to input again
                print("Invalid Email address\n")                                                # Print error message and the user will have to input again
                attempts-=1                                                                     # Decreases the attempts variable by 1
                if attempts == 0:                                                               # If attempts = 0
                    endProgram(str("\n"*3+"Too many attempts! The program will now exit."))     # The program will print a message and close 
                continue                                                                        # Continues
        except FileNotFoundError:                                                               # If the file does not exist then the user will have to try again
            print("This Email address ("+userEmail+") does not exist!\n")                       # Prints error message
            attempts-=1                                                                         # Decreases the attempts variable by 1
            if attempts == 0:                                                                   # If attempts = 0
                endProgram("Too many attempts! The program will now exit.")                     # The program will print a message and close
            pass                                                                                # Loops function
    attempts= 3                                                                                 # Resets the attempts value back to 3
    clr()                                                                                       # Clears Window
    while attempts > 0:                                                                         # While attempts is greater than 0 
        print("Email Entered: "+userEmail)                                                      # Prints email
        userPincode=str(input("Please enter your Pincode: "))                                   # User must input a pincode
        if decrypt(fileName[1]) == userPincode:                                                 # If the pincode entered matches the pincode in the file
            importData()                                                                        # Import the text file
            clr()                                                                               # Clear window
            mainMenu()                                                                          # Prints main menu
        else:                                                                                   # Else
            clr()                                                                               # Clears window 
            print("Incorrent pin!\n")                                                           # Print error message
            attempts-=1                                                                         # Attempts value gets decreased by 1
            if attempts == 1:                                                                   # If attempts = 1 then the following message will be printed
                    print("\r\rContinuing to enter the incorrect Pincode will cause the program to close.\n") # Prints "Continuing to enter the incorrect Pincode will cause the program to close."
            if attempts == 0:                                                                   # If there are no attempts left
                clr()                                                                           # Clears window
                endProgram("Too many attempts! The program will now exit.")                     # Ends program with printed message

def userEmailChange():                                                                          # If the user wants to change their login email address then they can do it here :)
    global userEmail                                                                            # Declares global variables
    while True:                                                                                 # New Loop
        newEmail=str(input("Please enter your new Email address: ")).lower()                    # User inputs their email address
        if re.match(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", newEmail):             # Check email for no special characters
            if os.path.isfile(encrypt(re.sub('[0-9]+', '', newEmail))+".txt"):                  # Check if the user already exists so there will be no duplicates
                clr()                                                                           # Calls 'clr()' function                                               
                print("This user already exists! Try again!\n")                                 # Alerts the user that this user already exists, the user must input a different email
            else:                                                                               # If the user does not already exist..
                try:                                                                            # Try unless exception
                    if len(userPincode) > 7:                                                    # <---
                        os.remove(encrypt(re.sub('[0-9]+', '', userEmail))+".txt")              #     |
                        userEmail= newEmail                                                     #     |
                        exportData()                                                            #     |
                        clr()                                                                   #     | This function gets called twice at different times. I needed to make a way so that
                        print("Your login email is now:",userEmail,"\n")                        #     | it would not return to the wrong place. I came up with a system which checks the pincode
                        mainMenu()                                                              #     | if the pincode already exists then this is an existing account
                    else:                                                                       #     | Otherwise the pincode would not be defined in the create account function (Because creating a pincode is the next step) 
                        userEmail= newEmail                                                     #     |
                        return                                                                  #     |
                except NameError:                                                               #     |
                    userEmail= newEmail                                                         #     |
                    return                                                                      # <---
        else:                                                                                   # Else (Because input does not contain '@' or special characters are inserted which are not allowed)
            clr()                                                                               # Calls 'clr()' function
            print("Invalid Email Address!\n")                                                   # Prints "Invalid Email Address", user must input again
    
def userNameChange():                                                                           # Name change or define function
    global userName                                                                             # Declares global variables
    while True:                                                                                 # New loop
        userName= input("Please enter your first name: ").capitalize()                          # User Inputs first name, saved as name with capitalize
        if len(userName) > 15:                                                                  # If the name is more than 15 Characters then alert user
            clr()                                                                               # Clears Window
            print("Error! Maximum 15 characters allowed!\n")                                    # Print "Error! Maximum 15 characters allowed!"         
            continue                                                                            # User must input another name (Retry)
        if len(userName) < 2:                                                                   # If the name is more than 15 Characters then alert user
            clr()                                                                               # Clears Window 
            print("Error! Must have at least 2 characters!\n")                                  # Print "Error! Must have at least 2 characters!"
            continue                                                                            # User must input another name
        if not re.match("^[a-z,A-Z]*$", userName):                                              # Allows for capitals and lower case but not numbers
            clr()                                                                               # Clears Window
            print("Error! Only the letters a-z are allowed!\n")                                 # Print "Error! Only the letters a-z are allowed!
            continue                                                                            # The user must input another name
        if len(userName) <15 and len(userName) >= 2 and re.match("^[a-z,A-Z]*$", userName):     # If the name input is less than 15 characters and contains no numbers or special characters then break
            clr()                                                                               # Calls 'clr()' function
            break                                                                               # Breaks out of loop
        else:                                                                                   # Else
            print("Please enter a valid first name...\n")                                       # Prints error message
            continue                                                                            # The user must input another name 
    return                                                                                      # Returns to where it was called
    
def userOptions():                                                                              # User options function
    print("Account options for:",userName,"\nEnter the number of the desired function:\n\n\t",  # <---
          "1)  Change Login Pincode\t(Currently: "+"*"*len(userPincode)+")\n\t",                #     |  
          "2)  View Login Pincode\n\t",                                                         #     |
          "3)  Change Login Email address\t(Currently: "+userEmail+")\n\t",                     #     | Prints Menu items
          "4)  Change Display Name\t(Currently: "+userName+")\n\t",                             #     |
          "5)  Delete Account\n\n\t",                                                           #     |
          "6)  Return to menu\n")                                                               # <---
    while True:                                                                                 # New Loop
        try:                                                                                    # Try unless exception
            userChoice=int(input(" - "))                                                        # User inputs a number on the list
            if userChoice in range(1,7):                                                        # If the number is either 1,2,3,4,5 or 6 (Not 7)
                break                                                                           # Break out of loop
            else:                                                                               # Else
                print("Please only enter numbers on the menu!")                                 # Print error message
        except ValueError:                                                                      # If the user inputted a string instead of an integer
            print("Please only enter numbers on the menu!")                                     # Print error message
    if userChoice == 1:                                                                         # If userChoice = 1
        clr()                                                                                   # Clears window
        userPincodeChange()                                                                     # Calls the pincode change function
        print("Your pincode has been updated to:",userPincode)                                  # Prints a message that the pincode has been changed
        exportData()                                                                            # Data is exported
        userOptions()                                                                           # Returns to top of function
    if userChoice == 2:                                                                         # If userChoice = 2
        clr()                                                                                   # Clears window
        print("\nYour Login Pincode:",userPincode,"\n")                                         # Prints the login pincode
        userOptions()                                                                           # Returns to top of function
    if userChoice == 3:                                                                         # If userChoice = 3
        userEmailChange()                                                                       # Goes to the email change function
        print("Your email has been changed to:",userEmail)                                      # Prints out a message saying that email has been updated
    if userChoice == 4:                                                                         # If userChoice = 4
        userNameChange()                                                                        # Calls the name change function
        print("Your name has been changed to: "+userName+".\n\nReturning to menu...\n")         # Prints out saying that the name has been changed
        mainMenu()                                                                              # Goes to main menu
    if userChoice == 5:                                                                         # If userChoice = 5
        userDelete()                                                                            # Goes to the user delete function
    if userChoice == 6:                                                                         # If userChoice = 6
        clr()                                                                                   # Clears window
        mainMenu()                                                                              # Goes to main menu
        
def mainMenu():                                                                                 # Main menu function
    print("Key Safe Main Menu".center(60, ' ')+"\n"+"-"*60+"\n")                                # <---
    print("Logged in user:",userName+"\n"+                                                      #     | 
          "You have",len(userApps),"apps\n"                                                     #     | 
          "Enter the number of the desired function:\n\n",                                      #     |  Prints out the main menu options
          "1)  Find the password for an existing Website/App\n",                                #     | 
          "2)  Add new Website/App and new password for it\n",                                  #     | 
          "3)  Change an existing password for an existing Website/App\n",                      #     | 
          "4)  Remove an existing App/Website\n",                                               #     | 
          "5)  Account Options\n",                                                              #     | 
          "6)  Exit\n")                                                                         # <---
    while True:                                                                                 # New loop                         
        try:                                                                                    # Try unless exception
            userChoice=int(input(" - "))                                                        # User inputs their choice of menu option
            if userChoice in range(1,7):                                                        # If the input is either 1,2,3,4,5 or 6 (Not 7)
                break                                                                           # Breaks out of loop
            else:                                                                               # Else
                print("Please only enter numbers on the menu!")                                 # Prints out Error message
        except ValueError:                                                                      # If the user inputted a string instead of a number
            print("Please only enter numbers on the menu!")                                     # Print error message
    if userChoice == 1:                                                                         # If userChoice = 1
        passwordFind()                                                                          # Calls the password find function
    if userChoice == 2:                                                                         # If userChoice = 2
        addApp()                                                                                # Calls the add app function
    if userChoice == 3:                                                                         # If userChoice = 3
        passwordChange()                                                                        # Calls the change password app
    if userChoice == 4:                                                                         # If userChoice = 4
        if len(userApps) == 2:                                                                  # If the ammount of apps in userApps is 2 then the user cannot delete any more apps
            clr()                                                                               # Clears window
            print("You must have at least 3 apps before you can remove an app.\n")              # Print Error message
            mainMenu()                                                                          # Calls the main menu function
        else:                                                                                   # Else
            removeApp()                                                                         # calls the remove app function
    if userChoice == 5:                                                                         # If userChoice = 5
        clr()                                                                                   # Clears window
        userOptions()                                                                           # Calls the user options function
    if userChoice == 6:                                                                         # If userChoice = 6
        clr()                                                                                   # Clears window
        exportData()                                                                            # Exports user data
        endProgram(str("Thank you,"+userName+"! Have a Good Day!\nClosing..."))                 # Ends program with a heartfull farewell message :'(

startMenu()                                                                                     # Starts the program

