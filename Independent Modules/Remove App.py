apps=["Google","Gmail","Drive","Docs","Sheets"]
passwords=["Yoshie","Gmail","Drive","Docs","Sheets"]

def clr():
    print("\n"*50)

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
                print("App has been removed\n")
                print("".ljust(10)+"App:".ljust(22)+"\n")
                for i in range(0,len(apps)):
                    print("".ljust(5),"{}".format(i+1)+").",apps[i].ljust(20))
                return
            elif choice == (len(apps)+1):
                return
            else:
                print("Please only enter numbers on the menu")

        except ValueError:
            print("Try Again! Please only enter numbers on the menu!")

remove_app()
