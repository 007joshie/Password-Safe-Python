# Password-Safe-Python

## Description 
An lightweight encryption based Password Safe. This was a NCEA level 2 High school project coded in Python 3.4.3. This program features the ability to Add / Change / Remove Apps and their passwords associated. Users must create an account, they will login in to their account with an Email address and a Pincode they have choosen.

## Download
Simply Download the 'Key safe.py', Make sure you are running python version 3 or higher. 

## Add-ons
No Add-ons required!!!
This program works with just the Python Vanilla Libraries :)






# Code:
```
from random import randint
import sys
sys.tracebacklimit=0
import re
def Encrypt(txt,n):
    result = ''
    for i in txt:
        c = ord(i)+n
        if ord(i) != c:
            b = chr(c)
            result += b
    return result

def Decrypt(txt,n):
    decrypt = ''    
    for x in txt:
        c = ord(x)-n
        if ord(x) != c:
            b = chr(c)
            decrypt += b
    return decrypt

def EndProgram(reason="Closing..."):
    from sys import exit
    print(reason)
    exit(0)

def clr():
    print("\n"*50)
    return ''

def create_account():
    import os
    global apps,passwords,pincode,name,username
    clr()
    while True:
        name= input("Please enter your first name: ").capitalize()                                                   # Inputs name
        if len(name) > 15:                                                      # If the name is more than 15 Characters then alert user
            print("Error! Maximum 15 characters allowed!\n")
        if len(name) < 2:                                                      # If the name is more than 15 Characters then alert user
            print("Error! Must have at least 2 characters!\n")
        if not re.match("^[a-z,A-Z]*$", name):                                  # Allows for capitals and lower case but not numbers
            print("Error! Only the letters a-z are allowed!\n")
        if len(name) <15 and len(name) >= 2 and re.match("^[a-z,A-Z]*$", name):                    # If the name input is less than 15 characters and contains no numbers or special characters then break
            clr()
            break
    print("Greetings, "+name+".")
    while True:
        username=str(input("Please enter your new Email address: ")).lower()
        if re.match(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", username):
            if os.path.isfile(Encrypt(re.sub('[0-9]+', '', username),key)+".txt"):
                clr()
                print("This user already exists! Try again!\n")
            else:
                break
        else:
            clr()
            print("Invalid Email address\n")
    while True:
        print("Your new password must:\n\t- Be longer than 8 characters \n\t- Contain at least 1 lowercase letter\n\t- Contain at least 1 uppercase letter\n\t- Contain at least 1 number\n\t- have no spaces")
        pincode= input("Input your password: ")   
        if len(pincode) <= 7 :
            clr()
            print("Must be at least 8 characters\n")
        elif ' ' in pincode:
            clr()
            print("Must not contain spaces!\n")
        elif len(pincode) >= 20:
            clr()
            print("Must be shorter than 20 characters\n")
        elif not re.search("[a-z]",pincode):
            clr()
            print("Must contain lowercase\n")
        elif not re.search("[0-9]",pincode):
            clr()
            print("Must contain a number\n")
        elif not re.search("[A-Z]",pincode):
            clr()
            print("Must contain a least 1 uppercase\n")
        elif len(pincode) > 6 and len(pincode) < 20 and re.search("[A-Za-z0-9]",pincode) and not ' ' in pincode:
            clr()
            break
    emailData=(username.split("@")[1]).split(".")[0].capitalize()
    apps=[str(emailData),'Code Avengers','Python Turtle']
    passwords=[str(pincode),'undefined','undefined']
    exportdata()
    print("-"*60,"\nYour account has been created, "+name+"!","\nYour Login Email:",username,"\nYour Pincode:",pincode,"\nYou have been given 3 default apps: \n\t- "+emailData.capitalize()+"\n\t- Code Avengers\n\t- Python Turtle\nThe default passwords for these are: 'undefined'\nYou can change this in the 'Change an existing password' menu setting\n\nEnjoy!\n"+"-"*60,"\n"*2)
    menu()

def change_pincode():
    global pincode
    while True:
        print("Your new pincode must:\n\t- Be longer than 8 characters\n\t- Contain at least 1 Lowercase letter\n\t- Contain at least 1 Uppercase letter\n\t- Contain at least 1 number\n")
        pincode= input("Input your pincode: \n - ")   
        if len(pincode) <= 7 :
            clr()
            print("Must be at least 8 characters\n")
        if ' ' in pincode:
            clr()
            print("Must not contain spaces!\n")
        if len(pincode) >= 20:
            clr()
            print("Must be shorter than 20 characters\n")
        if not re.search("[a-z]",pincode):
            clr()
            print("Must contain lowercase\n")
        if not re.search("[0-9]",pincode):
            clr()
            print("Must contain a number\n")
        if not re.search("[A-Z]",pincode):
            clr()
            print("Must contain a least 1 uppercase\n")
        if len(pincode) > 6 and len(pincode) < 20 and re.search("[A-Za-z0-9]",pincode) and not ' ' in pincode:
            clr()
            print("Your pincode has been updated, "+name+".\n")
            exportdata()
            menu()
        else:
            clr()
            print("Please make sure your new pincode follows the above rules.")

def delete_account():
    import os
    menu_return("Are you sure you want to delete your account: (Yes or No)")
    if Outcome == True:
        os.remove(Encrypt(re.sub('[0-9]+', '', username),key)+".txt")
        EndProgram("Account terminated")
    else:
        clr()
        print("Returning to menu...")
        menu()

def menu_return(msg="\nWould you like to return to the menu? (Yes or No)"):
    while True:
        global Polar,Outcome
        print(msg)
        Polar=str(input(" - ")).lower()
        if 'y' in Polar:
            Outcome=True
            return Outcome
        if 'n' in Polar:
            Outcome=False
            return Outcome
        else:
            print("Please enter either Yes or No")
            continue


def start_menu():
    clr()
    print("Welcome to Key Safe ...".rjust(30))
    print("Enter the number of the desired function:\n\n",
          "1)  Login With existing Account\n",
          "2)  Create new Account\n",
          "3)  Exit")
    while True:
        choice=""
        try:
            choice=int(input(" - "))
            if choice in range(1,4):
                break
            else:
                print("Please only enter numbers on the menu!")
        except ValueError:
            print("Please only enter numbers on the menu!")
    if choice == 1:
        login()
        return None
    if choice == 2:
        create_account()
    if choice == 3:
        clr()
        EndProgram(str("Thank you! Have a good day!\nClosing..."))


def importdata():
    global apps,passwords,pincode,filename,name
    pincode=Decrypt(filename[1],key)
    name=Decrypt(filename[2],key)
    apps=[]
    passwords=[]
    filename=list(filename)
    for i in range(0,len((filename[3]).split(","))):
        apps.append(Decrypt((filename[3]).split(",")[i],key))
    for i in range(0,len((filename[4]).split(","))):
        passwords.append(Decrypt((filename[4]).split(",")[i],key))

def exportdata():
    filename=open(Encrypt(re.sub('[0-9]+', '', username),key)+".txt","w+")
    filename.write("{}\n{}\n{}\n".format(Encrypt(username,key),Encrypt(pincode,key),Encrypt(name,key)))
    for i in range(0,len(apps)):
        if i == (len(apps)-1):
            ending=""
        else:
            ending=","
        filename.write("{}".format(Encrypt(apps[i],key))+ending)
    filename.write("\n")
    for i in range(0,len(passwords)):
        if i == (len(passwords)-1):
            ending=""
        else:
            ending=","
        filename.write("{}".format(Encrypt(passwords[i],key))+ending)
    filename.close()
    
def find_password():
    global apps,passwords
    while True:
        clr()
        print("Displaying",len(apps),"Apps/Websites")
        print("".ljust(10)+"App:".ljust(22)+"Password:\n")
        for index in range(0,len(apps)):
            print("".ljust(10)+apps[index].ljust(20)+"\t"+"*"*len(passwords[index]))
        choice=str(input("\nType 'All' to display all Apps/websites and their Passwords.\nWhat Website/App would you like to find the password for: ")).capitalize()
        if choice == "All":
            clr()
            print("Displaying all Apps/Websites and their Passwords.")
            print("".ljust(10)+"App:".ljust(22)+"Password:\n")
            for index in range(0,len(apps)):
                print("".ljust(10)+apps[index].ljust(20)+"\t"+passwords[index])
            menu_return()
            if Outcome == True:
                clr()
                menu()
            else:
                continue
        if choice in apps:
            print("".ljust(10)+"App:".ljust(22)+"Password:\n")
            print("".ljust(10)+str(apps[apps.index(choice)]).ljust(22)+str(passwords[apps.index(choice)]))
            menu_return()
            if Outcome == True:
                clr()
                menu()
            else:
                continue
        if not choice in apps:
            clr()
            print("\n"+choice,"does not seem to exist. Would you like to add it? (Yes or No)")
            menu_return("")
            if Outcome == True:
                AddData(str(choice))
                menu_return()
                if Outcome == True:
                    clr()
                    menu()
                else:
                    continue
            else:
                menu_return()
                if Outcome == True:
                    clr()
                    menu()
                else:
                    continue

def change_password():
    global passwords
    choice,new= ""
    clr()
    print("Please enter the number for the password you want to change:")
    print("".ljust(10)+"App:".ljust(22)+"Password:\n")
    for i in range(0,len(apps)):
        print("".ljust(5),"{}".format(i+1)+").",apps[i].ljust(20)+"\t"+"*"*len(passwords[i]))
    print("")
    print("      {}). Cancel".format(i+2))
    while True:
        try:
            choice=int(input(" - "))
            if choice in range(1,len(apps)+1):
                while True:
                    print("\rEnter the new password for", apps[choice-1]+":")
                    new=str(input(" - "))
                    if len(new) >= 4:
                        passwords[choice-1]=new
                        exportdata()
                        clr()
                        print("Password Sucessfully Changed! Returning to Menu...\n")
                        menu()
                    else:
                        print("It is recommended that you new password is longer than 4 characters!")
                        continue
            elif choice == (len(apps)+1):
                clr()
                print("Returning to menu...\n\n")
                menu()
            else:
                print("Please only enter numbers on the menu")

        except ValueError:
            print("Try Again! Please only enter numbers on the menu!")

def remove_app():
    global passwords,apps
    choice=""
    new=""
    clr()
    print("Please state the number for the app you want to remove:")
    print("".ljust(10)+"App:".ljust(22)+"\n")
    for i in range(0,len(apps)):
        print("".ljust(5),"{}".format(i+1)+").",apps[i].ljust(20))
    print("")
    print("      {}). Cancel".format(i+2))
    while True:
        try:
            choice=int(input(" - "))
            if choice in range(1,len(apps)+1):
                del apps[choice-1]
                del passwords[choice-1]
                clr()
                print("App has been removed\nReturning to menu...\n\n")
                menu()
            elif choice == (len(apps)+1):
                clr()
                print("Returning to menu...\n\n")
                menu()
            else:
                print("Please only enter numbers on the menu")

        except ValueError:
            print("Try Again! Please only enter numbers on the menu!")

def AddData(new=""):
    global apps,passwords
    password=''
    if new != "":
        clr()
        while True:
            print("Please enter a password for "+new+":")
            data_password=str(input(" - "))
            if len(data_password) > 4:
                apps.append(new)
                passwords.append(data_password)
                clr()
                print("App/Website Added!\n\tApp:\t\tPassword:\n\n\t"+new+"".ljust(22)+("*"*len(data_password)))
                break
            else:
                clr()
                print("Try Again!\n\nIt is recommended that your password is more than 4 characters!")
    else:
        data_password=''
        clr()
        while True:
            print("Please enter the name of the Website/App:")
            data_name=str(input(" - ")).capitalize()
            if data_name == "Cancel":
                clr()
                menu()
            if len(data_name) > 1:
                apps.append(data_name)
                clr()
                while True:
                    print("Please enter the password for "+data_name+":")
                    data_password= str(input(" - "))
                    if len(data_password) > 4:
                        passwords.append(data_password)
                        break
                    else:
                        print("Try Again!\n\nIt is recommended that your password is more than 4 characters!")
                        continue
                clr()
                print("App/Website Added!\n\tApp:\t\tPassword:\n\n\t"+data_name+"".ljust(10)+("*"*len(data_password)))
                menu_return("Would you like to add another app: (Yes or Nn)")
                if Outcome == True:
                    continue
                else:
                    clr()
                    print("Returning to menu!\n")
                    exportdata() 
                    menu()
            else:
                clr()
                print("Try Again!\n\nInput can not be left empty!")
            
key=int(5)

def login():
    global filename,username,pincode
    attempts= 3
    while attempts > 0:
        try:
            username=str(input("Please enter your existing Email address: ")).lower()
            clr()
            if re.match(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", username):
                filename=open(Encrypt(re.sub('[0-9]+', '', username),key)+".txt","r").read().split()
                if Decrypt(filename[0],key) == username:
                    break
                else:
                    print("\nIncorrect email address")
            else:
                print("Invalid Email address\n")
                attempts-=1
                if attempts == 0:
                    EndProgram(str("\n\n\n\nToo many attempts! The program will now exit."))
                continue
        except FileNotFoundError:
            print("This Email address ("+username+") does not exist!\n")
            attempts-=1
            if attempts == 0:
                EndProgram("Too many attempts! The program will now exit.")
            pass
    attempts= 3
    clr()
    while attempts > 0:
        print("Email Entered: "+username)
        pincode=str(input("Please enter your Pincode: "))
        if Decrypt(filename[1],key) == pincode:
            importdata()
            clr()
            menu()
        else:
            clr()
            print("Incorrent pin!\n")
            attempts-=1
            if attempts == 1:
                    print("\r\rContinuing to enter the incorrect Pincode will cause the program to close.\n")
            if attempts == 0:
                clr()
                EndProgram("Too many attempts! The program will now exit.")

def change_email():
    import os
    global username
    while True:
        new_username=str(input("Please enter your new Email address: ")).lower()
        if re.match(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", new_username):
            if os.path.isfile(Encrypt(re.sub('[0-9]+', '', new_username),key)+".txt"):
                clr()
                print("This user already exists! Try again!\n")
            else:
                os.remove(Encrypt(re.sub('[0-9]+', '', username),key)+".txt")
                username=new_username
                exportdata()
                menu()
        else:
            clr()
            print("Invalid Email address\n")

def change_name():
    global name
    while True:
        try:
            name= input("Please enter the name you want to change to: ").capitalize()                                                   # Inputs name
            if len(name) > 15:                                                      # If the name is more than 15 Characters then alert user
                print("Error! Maximum 15 characters allowed!\n")
            if len(name) < 2:                                                      # If the name is more than 15 Characters then alert user
                print("Error! Must have at least 2 characters!\n")
            if not re.match("^[a-z,A-Z]*$", name):                                  # Allows for capitals and lower case but not numbers
                print("Error! Only the letters a-z are allowed!\n")
            if len(name) <15 and len(name) >= 2 and re.match("^[a-z,A-Z]*$", name):                    # If the name input is less than 15 characters and contains no numbers or special characters then break
                clr()
                break
        except (ValueError):
            print("Please enter a valid first name...\n")
    clr()
    print("Your name has been changed to: "+name+".\n\nReturning to menu...\n")
    menu()
    
def account_options():
    print("Account options for:",name,"\nEnter the number of the desired function:\n\n\t",
          "1)  Change Login Pincode\t(Currently: "+"*"*len(pincode)+")\n\t",
          "2)  View Login Pincode\n\t",
          "3)  Change Login Email address\t(Currently: "+username+")\n\t",
          "4)  Change Display Name\t(Currently: "+name+")\n\t",
          "5)  Delete Account\n\n\t",
          "6)  Return to menu\n")
    while True:
        choice=""
        try:
            choice=int(input(" - "))
            if choice in range(1,7):
                break
            else:
                print("Please only enter numbers on the menu!")
        except ValueError:
            print("Please only enter numbers on the menu!")
    if choice == 1:
        clr()
        change_pincode()
    if choice == 2:
        clr()
        print("\nYour Login Pincode:",pincode,"\n")
        account_options()
    if choice == 3:
        change_email()
    if choice == 4:
        change_name()
    if choice == 5:
        delete_account()
    if choice == 6:
        clr()
        menu()
def menu():
    print("Key Safe".center(60, ' ')+"\n"+"-"*60+"\n")
    print("Logged in user:",name+"\n"+
          "You have",len(apps),"apps\n"
          "Enter the number of the desired function:\n\n",
          "1)  Find the password for an existing Website/App\n",
          "2)  Add new Website/App and new password for it\n",
          "3)  Change an existing password for an existing Website/App\n",
          "4)  Remove an existing App/Website\n",
          "5)  Account Options\n",
          "6)  Exit\n")
    while True:
        choice=""
        try:
            choice=int(input(" - "))
            if choice in range(1,7):
                break
            else:
                print("Please only enter numbers on the menu!")
        except ValueError:
            print("Please only enter numbers on the menu!")
    if choice == 1:
        find_password()
    if choice == 2:
        AddData() 
    if choice == 3:
        change_password()
    if choice == 4:
        if len(apps) == 2:
            clr()
            print("You must have at least 3 apps before you can remove an app.\n")
            menu()
        else:
            remove_app()
    if choice == 5:
        clr()
        account_options()
    if choice == 6:
        clr()
        exportdata()
        EndProgram(str("Thank you,"+name+"! Have a good day!\nClosing..."))
username=str("josh.boag@npbhs.school.nz")
filename=open(Encrypt(re.sub('[0-9]+', '', username),key)+".txt","r").read().split()
#start()
import os
for file in os.listdir():
    if file.endswith(".txt"):
        print(Decrypt(os.path.join("", file),key).replace(')oso',''))

#importdata()
pincode=str("abcD1234")
name=str("Joshua")
apps=['Google','Facebook','Instagram']          
passwords=['Hello','mynameisjeff','undefined']
menu()
#change_password()
```
