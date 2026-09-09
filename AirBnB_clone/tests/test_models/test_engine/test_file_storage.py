#!/usr/bin/python3
"""Unit tests for the FileStorage class."""
import json
import os
import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User


class TestFileStorage_instantiation(unittest.TestCase):
    """Tests instantiation of the FileStorage class."""

    def test_no_args_instantiates(self):
        """An instance is created with no arguments."""
        self.assertEqual(FileStorage, type(FileStorage()))

    def test_file_path_is_private_str(self):
        """__file_path is a private class attribute of type str."""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_objects_is_private_dict(self):
        """__objects is a private class attribute of type dict."""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes_in_models(self):
        """The models module exposes a unique FileStorage instance."""
        self.assertEqual(FileStorage, type(storage))


class TestFileStorage_methods(unittest.TestCase):
    """Tests the methods of the FileStorage class."""

    def setUp(self):
        """Save the current state of __file_path if it exists."""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        """Restore the original file.json and clear __objects."""
        FileStorage._FileStorage__objects = {}
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_all_returns_dict(self):
        """all() returns the __objects dictionary."""
        self.assertEqual(dict, type(storage.all()))

    def test_new_adds_object(self):
        """new() adds an object to __objects."""
        bm = BaseModel()
        storage.new(bm)
        key = "BaseModel.{}".format(bm.id)
        self.assertIn(key, storage.all())
        self.assertEqual(bm, storage.all()[key])

    def test_save_creates_file(self):
        """save() creates the JSON file."""
        bm = BaseModel()
        storage.new(bm)
        storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_save_writes_valid_json(self):
        """save() writes JSON that can be reloaded."""
        bm = BaseModel()
        storage.new(bm)
        storage.save()
        with open("file.json", "r") as f:
            data = json.load(f)
        key = "BaseModel.{}".format(bm.id)
        self.assertIn(key, data)

    def test_reload_restores_objects(self):
        """reload() restores previously saved objects."""
        user = User()
        storage.new(user)
        storage.save()
        FileStorage._FileStorage__objects = {}
        storage.reload()
        key = "User.{}".format(user.id)
        self.assertIn(key, storage.all())

    def test_reload_no_file_no_exception(self):
        """reload() does nothing if the JSON file doesn't exist."""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            storage.reload()
        except Exception:
            self.fail("reload() raised an exception with no file")


if __name__ == "__main__":
    unittest.main()
