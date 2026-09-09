#!/usr/bin/python3
"""Unit tests for the State class."""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Tests the State class."""

    def test_is_subclass_of_base_model(self):
        """State inherits from BaseModel."""
        self.assertTrue(issubclass(State, BaseModel))

    def test_name_is_class_attribute(self):
        """name is a public string class attribute."""
        self.assertEqual(str, type(State.name))

    def test_default_name_is_empty_string(self):
        """The default name value is an empty string."""
        state = State()
        self.assertEqual("", state.name)

    def test_to_dict_contains_class_name(self):
        """to_dict() includes the class name State."""
        state = State()
        self.assertEqual("State", state.to_dict()["__class__"])


if __name__ == "__main__":
    unittest.main()
