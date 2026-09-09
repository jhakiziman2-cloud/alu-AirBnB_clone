#!/usr/bin/python3
"""Unit tests for the User class."""
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Tests the User class."""

    def test_is_subclass_of_base_model(self):
        """User inherits from BaseModel."""
        self.assertTrue(issubclass(User, BaseModel))

    def test_email_is_class_attribute(self):
        """email is a public string class attribute."""
        self.assertEqual(str, type(User.email))

    def test_password_is_class_attribute(self):
        """password is a public string class attribute."""
        self.assertEqual(str, type(User.password))

    def test_first_name_is_class_attribute(self):
        """first_name is a public string class attribute."""
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_class_attribute(self):
        """last_name is a public string class attribute."""
        self.assertEqual(str, type(User.last_name))

    def test_default_values_are_empty_strings(self):
        """Default attribute values are empty strings."""
        user = User()
        self.assertEqual("", user.email)
        self.assertEqual("", user.password)
        self.assertEqual("", user.first_name)
        self.assertEqual("", user.last_name)

    def test_to_dict_contains_class_name(self):
        """to_dict() includes the class name User."""
        user = User()
        self.assertEqual("User", user.to_dict()["__class__"])


if __name__ == "__main__":
    unittest.main()
