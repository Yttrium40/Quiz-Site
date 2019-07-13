from django.test import TestCase

from .utils import validate_new_user

class UtilsValidateNewUserTests(TestCase):
    def test_empty_username_and_password(self):
        error_messages = validate_new_user('', '', '')

        are_messages_correct = (
            'Username may not be empty.' in error_messages and
            'Password may not be empty.' in error_messages
        )

        self.assertIs(are_messages_correct, True)

    def test_password_different_from_confirm_password(self):
        error_messages = validate_new_user('IGNORE', 'onepass', 'diffpass')

        are_messages_correct = (
            'Passwords do not match.' in error_messages
        )
        
        self.assertIs(are_messages_correct, True)
