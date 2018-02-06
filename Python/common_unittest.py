import unittest
from user_email import email_validation_check

class CommonTestCase(unittest.TestCase):
    def test_email_validation_check(self):
        self.assertFalse(email_validation_check('#@c#o@gmail.com'))

        self.assertTrue(email_validation_check('isi.cho@gmail.com'))
