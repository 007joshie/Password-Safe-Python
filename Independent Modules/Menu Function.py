def mainMenu():
    import time
    currentTime = int(time.strftime('%H:%M').split(':')[0])   

    if currentTime < 12 :
         Time="Good morning"
    if currentTime > 12 :
         Time=str('Good afternoon')
    if currentTime > 6 :
         Time=str('Good evening')

    print("Key Safe Main Menu".center(60, ' ')+"\n"+"-"*60+"")                                #
    print("{}, {}.".format(Time,userName)+"\t\t\t"+                                                      #
          "You have",len(userApps),"apps\n"+                                                     #
          "Enter the number of the desired function:\n\n",                                      #
          "1)  Find the password for an existing Website/App\n",                                #
          "2)  Add new Website/App and new password for it\n",                                  #
          "3)  Change an existing password for an existing Website/App\n",                      #
          "4)  Remove an existing App/Website\n",                                               
          "5)  Account Options\n",                                                              
          "6)  Exit\n")                                                                         
    while True:                                                                                                           
        try:                                                                                    
            userChoice=int(input(" - "))                                                        
            if userChoice in range(1,7):                                                        
                break                                                                           
            else:                                                                               
                print("Please only enter numbers on the menu!")                                 
        except ValueError:                                                                      
            print("Please only enter numbers on the menu!")                                     
    if userChoice == 1:                                                                         
        passwordFind()                                                                          
    if userChoice == 2:                                                                         
        addApp()                                                                                
    if userChoice == 3:                                                                         
        passwordChange()                                                                        
    if userChoice == 4:                                                                         
        if len(userApps) == 2:                                                                  
            clr()                                                                               
            print("You must have at least 3 apps before you can remove an app.\n")              
            mainMenu()                                                                          
        else:                                                                                   
            removeApp()                                                                         
    if userChoice == 5:                                                                         
        clr()                                                                                   
        userOptions()                                                                           
    if userChoice == 6:                                                                         
        clr()                                                                                   
        exportData()                                                                            
        endProgram(str("Thank you,"+userName+"! Have a good day!\nClosing..."))
userName="name" #for debug
userApps=["hi"] #for debug
mainMenu()
