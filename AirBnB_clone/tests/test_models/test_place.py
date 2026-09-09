#!/usr/bin/python3
"""Unit tests for the Place class."""
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Tests the Place class."""

    def test_is_subclass_of_base_model(self):
        """Place inherits from BaseModel."""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_city_id_is_class_attribute(self):
        """city_id is a public string class attribute."""
        self.assertEqual(str, type(Place.city_id))

    def test_user_id_is_class_attribute(self):
        """user_id is a public string class attribute."""
        self.assertEqual(str, type(Place.user_id))

    def test_name_is_class_attribute(self):
        """name is a public string class attribute."""
        self.assertEqual(str, type(Place.name))

    def test_description_is_class_attribute(self):
        """description is a public string class attribute."""
        self.assertEqual(str, type(Place.description))

    def test_number_rooms_is_class_attribute(self):
        """number_rooms is a public integer class attribute."""
        self.assertEqual(int, type(Place.number_rooms))

    def test_number_bathrooms_is_class_attribute(self):
        """number_bathrooms is a public integer class attribute."""
        self.assertEqual(int, type(Place.number_bathrooms))

    def test_max_guest_is_class_attribute(self):
        """max_guest is a public integer class attribute."""
        self.assertEqual(int, type(Place.max_guest))

    def test_price_by_night_is_class_attribute(self):
        """price_by_night is a public integer class attribute."""
        self.assertEqual(int, type(Place.price_by_night))

    def test_latitude_is_class_attribute(self):
        """latitude is a public float class attribute."""
        self.assertEqual(float, type(Place.latitude))

    def test_longitude_is_class_attribute(self):
        """longitude is a public float class attribute."""
        self.assertEqual(float, type(Place.longitude))

    def test_amenity_ids_is_class_attribute(self):
        """amenity_ids is a public list class attribute."""
        self.assertEqual(list, type(Place.amenity_ids))

    def test_default_values(self):
        """Default attribute values match the expected defaults."""
        place = Place()
        self.assertEqual("", place.city_id)
        self.assertEqual("", place.user_id)
        self.assertEqual("", place.name)
        self.assertEqual("", place.description)
        self.assertEqual(0, place.number_rooms)
        self.assertEqual(0, place.number_bathrooms)
        self.assertEqual(0, place.max_guest)
        self.assertEqual(0, place.price_by_night)
        self.assertEqual(0.0, place.latitude)
        self.assertEqual(0.0, place.longitude)
        self.assertEqual([], place.amenity_ids)

    def test_to_dict_contains_class_name(self):
        """to_dict() includes the class name Place."""
        place = Place()
        self.assertEqual("Place", place.to_dict()["__class__"])


if __name__ == "__main__":
    unittest.main()
