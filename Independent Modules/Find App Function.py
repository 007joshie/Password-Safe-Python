apps=["Google","Gmail","Drive","Docs","Sheets"]
passwords=["password1","Gmail","Drive","Docs","Sheets"]

def clr():
    print("\n"*50)

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
            return
        if choice in apps:
            print("".ljust(10)+"App:".ljust(22)+"Password:\n")
            print("".ljust(10)+str(apps[apps.index(choice)]).ljust(22)+str(passwords[apps.index(choice)]))
            return
        if not choice in apps:
            clr()
            print("\n"+choice,"does not seem to exist.")
            return
find_password()
