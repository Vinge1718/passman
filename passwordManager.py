import random
import json

info = {}
info_storage = "t.txt"
s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
len_password = int(input("Enter the desired length of your password: "))

password = "".join(random.sample(s, len_password))
print(password)

answer0 = input("would you like to keep this password or create your own? answer with a (Y/N)").upper()
if answer0 == "Y":
    account_name = input("Enter account name: ")
    info[account_name] = password
    with open(info_storage, "w") as file:
        file.write(json.dumps(info))

elif answer0 == "N":
    account_name = input("Enter account name:")
    info[account_name] = input("Enter your own desired password: ")
    with open(info_storage, "w") as file:
        file.write(json.dumps(info))
         

else:
    print("Okay")