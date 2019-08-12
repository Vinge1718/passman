import pyperclip

class Credential:
    """
    Class responsible for creating a sites credentias for the user
    """

    credential_list = []

    def __init__(self, site_name, user_name, password):
        self.site_name = site_name
        self.user_name = user_name
        self.password = password

    def save_credential(self):
        '''
        save_credential method saves credential objects into contact_list.
        '''

        Credential.credential_list.append(self)

    def delete_credential(self):
        '''
        deletes the selected credential.
        '''
        Credential.credential_list.remove(self)
    @classmethod
    def find_by_site_name(cls, site):
        '''
        A method that takes in a site name and returrns the credentials for that site
        '''
        for credential in cls.credential_list:
            if credential.site_name == site:
                return credential

    @classmethod
    def credential_exists(cls, site):
        '''
        Method that checks whether credentials for a particular site exist
        '''
        for credential in cls.credential_list:
            if credential.site_name == site:
                return True

        return False

    @classmethod
    def display_all_credentials(cls):
        '''
        method that returns the method list
        '''
        return cls.credential_list

    @classmethod
    def copy_password(cls, site):
        credential_found = cls.find_by_site_name(site)
        pyperclip.copy(credential_found.password)