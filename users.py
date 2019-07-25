import pyperclip

credential_storage = "t.txt"
m_password = input("Enter master password: ")
if m_password == "Masterp":
    account_name = input("Enter account name: ")
    with open(credential_storage, "r") as readFile:
        info = readFile.read()

    if account_name in info:
        pyperclip.copy(info[account_name])
        show_password = input("Enter 'Y' to show the password").upper()
        if show_password == "Y":
            print("Password = ", info[account_name])

        else:
            break