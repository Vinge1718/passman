import unittest
import pyperclip
from credential import Credential

class TestCredential(unittest.TestCase):
    '''
    Test class that defines the test cases for the Credentials
    '''

    def setUp(self):
        self.new_credential = Credential("Facebook", "viking", "password")

    def tearDown(self):
        Credential.credential_list = []

    def test_init(self):
        '''
        Unit test case to test whether the credential object initialized with all attributes
        '''

        self.assertEqual(self.new_credential.site_name, "Facebook")
        self.assertEqual(self.new_credential.user_name, "viking")
        self.assertEqual(self.new_credential.password, "password")

    def test_save_credential(self):
        '''
        Test whether the credential is saved into the credential list
        '''

        self.new_credential.save_credential()

        self.assertEqual(len(Credential.credential_list), 1)

    def test_save_multiple_credentials(self):
        '''
        Test whether the list of credentials is being populated properly by more than one object 
        '''
        self.new_credential.save_credential()
        second_credential = Credential("Instagram", "pablo", "password2")
        second_credential.save_credential()

        self.assertEqual(len(Credential.credential_list), 2)

    def test_delete_credential(self):
        '''
        Test tests whether one can delete the selected credential
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Instagram", "pablo", "password2")
        test_credential.save_credential()
        self.new_credential.delete_credential()

        self.assertEqual(len(Credential.credential_list), 1)

    def test_find_credential_by_site_name(self):
        '''
        Test to ascertain whether we can find a credential by the site name and display it's information
        '''

        self.new_credential.save_credential()
        test_credential = Credential("Instagram", "pablo", "password2")
        test_credential.save_credential()

        found_credential = Credential.find_by_site_name("Instagram")

        self.assertEqual(found_credential, test_credential)

    def test_credential_exist(self):
        '''
        Test to ascertain whether a credential for a particular site exists by its name
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Instagram", "pablo", "password2")
        test_credential.save_credential()

        existing_credential = Credential.credential_exists("Instagram")

        self.assertTrue(existing_credential)

    def test_display_all_credential(self):
        '''
        Test to display all credentials saved
        '''
        self.assertEqual(Credential.display_all_credentials(), Credential.credential_list)

    def test_copy_password(self):
        '''
        Test the copying function by the site
        '''
        self.new_credential.save_credential()
        Credential.copy_password("Facebook")
        self.assertEqual(self.new_credential.password, pyperclip.paste())


if __name__ == "__main__":
    unittest.main()