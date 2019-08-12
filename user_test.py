import unittest
import pyperclip
import user
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines the test cases for the User class behaviours
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases
        '''
        self.new_user = User("Victor", "Njonge", "vnjonge@yahoo.com", "password")

    def tearDown(self):
        '''
        This resets the Users in the testing array before every test
        '''
        User.user_list = []

    def test_init(self):
        '''
        test_unit test case to test if the user object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name, "Victor")
        self.assertEqual(self.new_user.last_name, "Njonge")
        self.assertEqual(self.new_user.email, "vnjonge@yahoo.com")
        self.assertEqual(self.new_user.password, "password")

    def test_save_user(self):
        '''
        Test for the save User function upon entering the user details
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def test_save_multiple_users(self):
        '''
        Test for saving more than one user
        '''
        self.new_user.save_user()
        second_user = User("Rehema", "Wambui", "rw@hotmail.com", "pass2")
        second_user.save_user()

        self.assertEqual(len(User.user_list), 2)

    def test_delete_credential(self):
        '''
        Test for deleting Users accounts
        '''
        self.new_user.save_user()
        test_user = User("Rehema", "Wambui", "rw@hotmail.com", "pass2")
        test_user.save_user()

        self.new_user.delete_user()

        self.assertEqual(len(User.user_list), 1)

    def test_find_user_by_mail(self):
        '''
        Test to locate an object by it's associated ID
        '''

        self.new_user.save_user()
        test_user = User("Rehema", "Wambui", "rw@hotmail.com", "pass2")
        test_user.save_user()

        found_user = User.find_by_email("rw@hotmail.com")

        self.assertEqual(found_user, test_user)

    def test_if_user_exists_by_email(self):
        '''
        Test for checking whether a user exists from their email
        '''
        self.new_user.save_user()
        test_user = User("Rehema", "Wambui", "rw@hotmail.com", "pass2")
        test_user.save_user()

        existing_user = User.user_exists("rw@hotmail.com")
        self.assertTrue(existing_user)

    def test_for_displaying_all_users(self):
        '''
        Test for returning a list of all users
        '''
        self.assertEqual(User.user_list, User.all_users())

    # def test_write_data(self):
    #     '''
    #     Test whether the users data is being written in the users text file
    #     '''
    #     with open("userdetailsTest.txt", "r+") as rawData:
    #         mail = self.new_user.email
    #         passcode = self.new_user.password
    #         rawData.write(mail + " " + passcode)
    #         data = rawData.read()
    #         self.assertEquals(data, User.write_user("userdetailsTest.txt"))
                    
if __name__ == "__main__":
    unittest.main()