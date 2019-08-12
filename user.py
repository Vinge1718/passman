import unittest

class User:
    """
    Class that generates new instances of Users
    """
    user_list = []
    users_file = "userdetails.txt"
    test_users_file = "userdetailsTest.txt"

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def save_user(self):
        """
        Method that saves the users in a list
        """
        User.user_list.append(self) 

    def delete_user(self):
        """
        Method that deletes selcted users
        """
        User.user_list.remove(self)

    @classmethod
    def find_by_email(cls, mail):
        '''
        Methos that finds a unique user by their email
        '''
        for user in cls.user_list:
            if user.email == mail:
                return user

        return False

    @classmethod
    def user_exists(cls, mail):
        '''
        Methods for checking the existence of a user from their email
        '''
        for user in cls.user_list:
            if user.email == mail:
                return True

        return False

    @classmethod
    def all_users(cls):
        '''
        Method for returning a list of all users
        '''
        return cls.user_list