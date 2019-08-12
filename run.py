#!/usr/bin/env python3.6

from user import User
import pickle
from credential import Credential
import random

def create_user(first_name, last_name, email, password):
    '''
    Function to create a new user
    '''
    new_user = User(first_name, last_name, email, password)
    return new_user

def create_credential(site_name, user_name, password):
    '''
    function to create a new credential
    '''
    new_credential = Credential(site_name, user_name, password)
    return new_credential

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def save_credential(credential):
    '''
    Function to save credential
    '''
    credential.save_credential()

def delete_user(user):
    '''
    function to delete user
    '''
    user.delete_user()

def find_user(email):
    '''
    Function that finds a user by email and returns the user
    '''
    return User.find_by_email(email)

def find_credential(site):
    '''
    function that finds the credentials for logging into a site
    '''
    return Credential.find_by_site_name(site)

def check_if_user_exists(email):
    '''
    Function that checks for the existence of a user and returns a boolean
    '''
    return User.user_exists(email)

def check_if_credential_exists(site):
    '''
    Functions that checks the existence of a credential and returns a boolean
    '''
    return Credential.credential_exists(site)

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.all_users()

def main():
    credentials_list = []
    users_list = []
    while True:
        registered_status = input("Welcome to the password locker. Do you have a registered account? (Y/N) ").upper()
        if registered_status == "N":
            print("Enter your details to create a user account:")

            print("First Name: ")
            f_name = input()

            print("Last Name")
            l_name = input()

            print("Email")
            email = input()

            print("Password")
            passcode = input()

            save_user(create_user(f_name, l_name, email, passcode))
            print("\n")
            print(f"New User {f_name} {l_name} created")
            print("\n")

            with open("userdetails.obj", "ab") as new_rawData:
                user_object  = create_user(f_name, l_name, email, passcode)
                users_list.append(user_object)
                save_user(user_object)
                pickle.dump(users_list, new_rawData)
                
            print("Use these short codes : sc - save already existing credentials, cc - create credentials for a new account, fc -find credentials for an account, ex -exit the password locker ")
            short_code = input().lower()
            if short_code == "sc":
                site_name = input("Enter the name of the site: ")
                account_user_name = input("Enter account name: ")
                password1 = input("Enter account name: ")

                with open("user_credentials.txt", "ab") as credential_rawData:
                    user_credential = Credential(site_name, account_user_name, password1)
                    save_credential(user_credential)
                    credentials_list.append(user_credential)
                    pickle.dump(credentials_list, credential_rawData)

            elif short_code == "cc":
                s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
                len_password = int(input("Enter the desired length of your password: "))
                password0 = "".join(random.sample(s, len_password))
                print(password0)
                answer0 = input("would you like to keep this password or create your own? answer with a (Y/N)").upper()
                if answer0 == "Y":
                    site_name0 = input("Enter the name of the site: ")
                    account_user_name0 = input("Enter account name: ")
                    password10 = password0
                    with open("user_credentials.txt", "ab") as credential_rawData0:
                        user_credential0 = Credential(site_name0, account_user_name0, password10)
                        save_credential(user_credential0)
                        credentials_list.append(user_credential0)
                        pickle.dump(credentials_list, credential_rawData0)

                elif answer0 == "N":
                    site_name2 = input("Enter the name of the site: ")
                    account_user_name2 = input("Enter account name: ")
                    password2 = input("Enter your preffered password: ")
                    with open("user_credentials.txt", "ab") as credential_rawData2:
                        user_credential2 = Credential(site_name2, account_user_name2, password2)
                        save_credential(user_credential2)
                        credentials_list.append(user_credential2)
                        pickle.dump(credentials_list, credential_rawData2)
                else:
                    print("Operation Cancled Please enter a valid entry as requested")

            elif short_code == "fc":
                print("Enter the site name whose credentials you want to search for")
                search_site = input()
                if check_if_credential_exists(search_site):
                    sort_Credential = find_credential(search_site)
                    print(f"{sort_Credential.user_name} \n {sort_Credential.password}")

            elif short_code == "ex":
                print("Bye .......")
                break

        elif registered_status == "Y":
            user_email = input("Enter your email address: ")
            user_password = input("Enter your password: ")
            with open("userdetails.txt", "ab") as read_rawData:
                user_list2 = pickle.load(read_rawData)
                for users in user_list2:
                    if (users.email == user_email) and (users.password == user_password):
                        print("Successfully logged in \n Use these short codes : sc - save already existing credentials, cc - create credentials for a new account, fc -find credentials for an account, ex -exit the password locker ")
                        short_code = input().lower()
                        if short_code == "sc":
                            site_name = input("Enter the name of the site: ")
                            account_user_name = input("Enter account name: ")
                            password1 = input("Enter account name: ")
            
                            with open("user_credentials.txt", "ab") as credential_rawData:
                                user_credential = Credential(site_name, account_user_name, password1)
                                save_credential(user_credential)
                                credentials_list.append(user_credential)
                                pickle.dump(credentials_list, credential_rawData)
            
                        elif short_code == "cc":
                            s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
                            len_password = int(input("Enter the desired length of your password: "))
                            password0 = "".join(random.sample(s, len_password))
                            print(password0)
                            answer0 = input("would you like to keep this password or create your own? answer with a (Y/N)").upper()
                            if answer0 == "Y":
                                site_name0 = input("Enter the name of the site: ")
                                account_user_name0 = input("Enter account name: ")
                                password10 = password0
                                with open("user_credentials.txt", "ab") as credential_rawData0:
                                    user_credential0 = Credential(site_name0, account_user_name0, password10)
                                    save_credential(user_credential0)
                                    credentials_list.append(user_credential0)
                                    pickle.dump(credentials_list, credential_rawData0)
            
                            elif answer0 == "N":
                                site_name2 = input("Enter the name of the site: ")
                                account_user_name2 = input("Enter account name: ")
                                password2 = input("Enter your preffered password: ")
                                with open("user_credentials.txt", "ab") as credential_rawData2:
                                    user_credential2 = Credential(site_name2, account_user_name2, password2)
                                    save_credential(user_credential2)
                                    credentials_list.append(user_credential2)
                                    pickle.dump(credentials_list, credential_rawData2)
                            else:
                                print("Operation Cancled Please enter a valid entry as requested")
            
                        elif short_code == "fc":
                            print("Enter the site name whose credentials you want to search for")
                            search_site = input()
                            if check_if_credential_exists(search_site):
                                sort_Credential = find_credential(search_site)
                                print(f"{sort_Credential.user_name} \n {sort_Credential.password}")
            
                        elif short_code == "ex":
                            print("Bye .......")
                            break
if __name__ == "__main__":
    main()