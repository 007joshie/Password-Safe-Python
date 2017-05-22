######################################################################################################################
#
#                   Name: Joshua Boag
#                   Class: L2_COS_82A_17
#                   Title: Password Safe Module Testing
#                   Python Version: 3.4.3
#                   File Name: "Export to File 2.0.py"
#                   File Version: 2.0                   
#                   Last Eddited: 08/05/2017
#
#       This is just isolated linear module testing, I wanted to code the basics of my file writing system.\
#       Feel free to change the variables in the User Editor below :)
#
#######################################################################################################################

#----------------------------------------------------------
#                    USER EDITOR                    

userEmail=str("josh.boag@npbhs.school.nz")
userPincode=str("abcD1234")
name=str("Joshua")
userApps=['Google','Facebook','Instagram']          
userPassword=['undefined','undefined','undefined']

#Custom Encryption Key (Must be a number)
key= int(5)

#----------------------------------------------------------
import re
from random import randint
def Encrypt(txt,n):
    global result
    result = ''
    for i in txt:
        c = ord(i)+n
        if ord(i) != c:
            b = chr(c)
            result += b
    return result

def Decrypt(txt,n):
    global decrypt
    decrypt = ''
    for x in txt:
        c = ord(x)-n
        if ord(x) != c:
            b = chr(c)
            decrypt += b
    return decrypt
    
def importdata():
    global Pincode,Email, Apps, Password, Name
    filename=list(open(Encrypt(re.sub('[0-9]+', '', userEmail),key)+".txt","r+"))
    Email= Decrypt(filename[0],key)
    Apps=[]
    Password=[]
    Pincode=Decrypt(filename[1],key)
    Name=Decrypt(filename[2],key)
    for i in range(0,len((filename[3]).split(","))):
        Decrypt((filename[3]).split(",")[i],key)
        Apps.append(decrypt)
    for i in range(0,len((filename[4]).split(","))):
        Decrypt((filename[4]).split(",")[i],key)
        Password.append(decrypt)

def exportdata():
    Encrypt(re.sub('[0-9]+', '', userEmail),key)
    filename=open(result+".txt","w+")
    WriteToFile=str("{}\n").format(Encrypt(userEmail,key))
    filename.write(WriteToFile)
    WriteToFile=str("{}\n").format(Encrypt(userPincode,key))
    filename.write(WriteToFile)
    WriteToFile=str("{}\n").format(Encrypt(name,key))
    filename.write(WriteToFile)
    for i in range(0,len(userApps)):
        if i == (len(userApps)-1):
            ending=""
        else:
            ending=","
        Encrypt(userApps[i],key)
        filename.write("{}".format(result)+ending)
    WriteToFile=str("\n")
    filename.write(WriteToFile)
    for i in range(0,len(userPassword)):
        if i == (len(userPassword)-1):
            ending=""
        else:
            ending=","
        Encrypt(userPassword[i],key)
        filename.write("{}".format(result)+ending)
    filename.close()

exportdata()
print("-"*60,"\n\t\tEXPORT","\n{}\n{}\n{}\n{}\n{}\n".format(userEmail,userPincode,name,userApps,userPassword),"-"*60)
importdata()
print("-"*60,"\n\t\tIMPORT","\n{}\n{}\n{}\n{}\n{}\n".format(Email[:-1],Pincode[:-1],Name[:-1],Apps,Password),"-"*60)
