from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Testing creating new user with email successful"""
        email = "test@finduy.com"
        password = "test@test"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test the email for a new user is normalized"""
        email = "test@FINDUY.COM"
        password = 'test@test'

        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email.lower())
        self.assertTrue(user.check_password(password))

    def test_new_user_invalid_email(self):
        """tetst creating user with invalid email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '232553')

    def test_create_new_superuser(self):
        """test creating new superuser"""
        user = get_user_model().objects.create_superuser('test@finduy.com', 'test@test')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
