from random import randint
def Encrypt(txt,n):
    global result
    result = '' 
    for i in txt:
        c = ord(i)+n
        if ord(i) != c:
            b = chr(c)
            result += b
    print(result)

def Decrypt(txt,n):
    global decrypt
    decrypt = ''
    for x in txt:
        c = ord(x)-n
        if ord(x) != c:
            b = chr(c)
            decrypt += b
    print(decrypt)

message= input("Type Your secret message: ")
key=int(input("Type Key: "))
Encrypt(message,key)
Decrypt(result,key)
