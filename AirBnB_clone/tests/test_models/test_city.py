#!/usr/bin/python3
"""Unit tests for the City class."""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Tests the City class."""

    def test_is_subclass_of_base_model(self):
        """City inherits from BaseModel."""
        self.assertTrue(issubclass(City, BaseModel))

    def test_state_id_is_class_attribute(self):
        """state_id is a public string class attribute."""
        self.assertEqual(str, type(City.state_id))

    def test_name_is_class_attribute(self):
        """name is a public string class attribute."""
        self.assertEqual(str, type(City.name))

    def test_default_values_are_empty_strings(self):
        """Default attribute values are empty strings."""
        city = City()
        self.assertEqual("", city.state_id)
        self.assertEqual("", city.name)

    def test_to_dict_contains_class_name(self):
        """to_dict() includes the class name City."""
        city = City()
        self.assertEqual("City", city.to_dict()["__class__"])


if __name__ == "__main__":
    unittest.main()
