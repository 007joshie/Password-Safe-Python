import re

def clr():
    print("\n"*50)

def change_pincode():
    global pincode
    while True:
        print("Your new pincode must:\n\t- Be longer than 8 characters\n\t- Contain at least 1 Lowercase letter\n\t- Contain at least 1 Uppercase letter\n\t- Contain at least 1 number\n")
        pincode= input("Input your pincode: \n - ")   
        if len(pincode) <= 7 :
            clr()
            print("Must be at least 8 characters\n")
        elif ' ' in pincode:
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
        elif not re.search("[A-Z]",pincode):
            clr()
            print("Must contain a least 1 uppercase\n")
        if len(pincode) > 6 and len(pincode) < 20 and re.search("[A-Za-z0-9]",pincode) and not ' ' in pincode:
            clr()
            print("Your pincode has been updated\n")
            exit(0)
change_pincode()
