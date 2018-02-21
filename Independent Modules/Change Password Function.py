apps=['App1','App2','App3']
password=['undefined','undefined','undefined']
input_1=input("name of app")
if input_1 in apps:
    num=apps.index(input_1)
else:
    print("Not found")

input_2=input("change password")
password[num]=input_2
print(apps)
print(password)
