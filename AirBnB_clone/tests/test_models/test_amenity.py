#!/usr/bin/python3
"""Unit tests for the Amenity class."""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Tests the Amenity class."""

    def test_is_subclass_of_base_model(self):
        """Amenity inherits from BaseModel."""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_name_is_class_attribute(self):
        """name is a public string class attribute."""
        self.assertEqual(str, type(Amenity.name))

    def test_default_name_is_empty_string(self):
        """The default name value is an empty string."""
        amenity = Amenity()
        self.assertEqual("", amenity.name)

    def test_to_dict_contains_class_name(self):
        """to_dict() includes the class name Amenity."""
        amenity = Amenity()
        self.assertEqual("Amenity", amenity.to_dict()["__class__"])


if __name__ == "__main__":
    unittest.main()
