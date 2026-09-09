#!/usr/bin/python3
"""Unit tests for the BaseModel class."""
import unittest
from datetime import datetime
from time import sleep
import models
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Tests instantiation of the BaseModel class."""

    def test_no_args_instantiates(self):
        """An instance is created with no arguments."""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        """A new instance is added to storage."""
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        """The id attribute is a public string."""
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        """created_at is a public datetime instance."""
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        """updated_at is a public datetime instance."""
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        """Two instances have different ids."""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_two_models_different_created_at(self):
        """Two instances have different created_at timestamps."""
        bm1 = BaseModel()
        sleep(0.01)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_two_models_different_updated_at(self):
        """Two instances have different updated_at timestamps."""
        bm1 = BaseModel()
        sleep(0.01)
        bm2 = BaseModel()
        self.assertLess(bm1.updated_at, bm2.updated_at)

    def test_str_representation(self):
        """__str__ returns the expected format."""
        bm = BaseModel()
        string = str(bm)
        self.assertIn("[BaseModel] ({})".format(bm.id), string)

    def test_args_unused(self):
        """Positional arguments are not used."""
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """An instance can be created from kwargs."""
        dt = datetime.now()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="123", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "123")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)


class TestBaseModel_save(unittest.TestCase):
    """Tests the save method of the BaseModel class."""

    def test_save_updates_updated_at(self):
        """save() updates the updated_at attribute."""
        bm = BaseModel()
        old_updated_at = bm.updated_at
        sleep(0.01)
        bm.save()
        self.assertLess(old_updated_at, bm.updated_at)

    def test_save_with_arg_raises(self):
        """save() with an argument raises a TypeError."""
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)


class TestBaseModel_to_dict(unittest.TestCase):
    """Tests the to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        """to_dict() returns a dictionary."""
        bm = BaseModel()
        self.assertEqual(dict, type(bm.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """to_dict() output contains the expected keys."""
        bm = BaseModel()
        d = bm.to_dict()
        for key in ("id", "created_at", "updated_at", "__class__"):
            self.assertIn(key, d)

    def test_to_dict_datetime_are_strings(self):
        """created_at/updated_at are ISO format strings in to_dict()."""
        bm = BaseModel()
        d = bm.to_dict()
        self.assertEqual(str, type(d["created_at"]))
        self.assertEqual(str, type(d["updated_at"]))

    def test_to_dict_class_value(self):
        """to_dict() adds the correct class name."""
        bm = BaseModel()
        self.assertEqual("BaseModel", bm.to_dict()["__class__"])

    def test_to_dict_with_arg_raises(self):
        """to_dict() with an argument raises a TypeError."""
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)


if __name__ == "__main__":
    unittest.main()
