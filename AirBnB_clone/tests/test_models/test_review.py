#!/usr/bin/python3
"""Unit tests for the Review class."""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Tests the Review class."""

    def test_is_subclass_of_base_model(self):
        """Review inherits from BaseModel."""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_place_id_is_class_attribute(self):
        """place_id is a public string class attribute."""
        self.assertEqual(str, type(Review.place_id))

    def test_user_id_is_class_attribute(self):
        """user_id is a public string class attribute."""
        self.assertEqual(str, type(Review.user_id))

    def test_text_is_class_attribute(self):
        """text is a public string class attribute."""
        self.assertEqual(str, type(Review.text))

    def test_default_values_are_empty_strings(self):
        """Default attribute values are empty strings."""
        review = Review()
        self.assertEqual("", review.place_id)
        self.assertEqual("", review.user_id)
        self.assertEqual("", review.text)

    def test_to_dict_contains_class_name(self):
        """to_dict() includes the class name Review."""
        review = Review()
        self.assertEqual("Review", review.to_dict()["__class__"])


if __name__ == "__main__":
    unittest.main()
