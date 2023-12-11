#!/usr/bin/python3
"""
Module to test The FileStorage class
"""
import os
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorageInstatiation(unittest.TestCase):
    """ Here we will be testing the instatiation of a file storage """
    def test_FileStorage_instation_with_no_args(self):
        """ creating a FileStorage instance wtih no argument """
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instatiation_with_args(self):
        """
        Raises a TypeError when creating a FileStorage
        instance with an argument
        """
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_initialize(self):
        """
        test if the storage variable in models
        is an instance of FileStorage
        """
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage(unittest.TestCase):
    """ Test the File Storage """
    def setUp(self):
        """ create a test file for testing the storage """
        self.test_file = "test_file.json"

    def tearDown(self):
        """ remove the created test file after testing """
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_all_storage_returns_dictionary(self):
        """ testing if all() returns a dict. """
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
        """ Testing new() method """
        obj = BaseModel()
        models.storage.new(obj)
        self.assertIn("BaseModel.{}".format(obj.id), models.storage.all())

    def test_new_with_args(self):
        """ test new() method with args """
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel, 1)

    def test_new_with_no_arg(self):
        """ test new() method with no arg """
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save_and_reload(self):
        """ testing the save() method and reload() """
        obj_one = BaseModel()
        obj_two = BaseModel()
        models.storage.new(obj_one)
        models.storage.new(obj_two)
        models.storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        self.assertTrue(new_storage.all().get(
            "BaseModel.{}".format(obj_one.id)) is not None
            )
        self.assertTrue(new_storage.all().get(
            "BaseModel.{}".format(obj_two.id)) is not None
            )

    def test_save_to_file(self):
        """
        check if objects are being saved
        on file and if the file created
        """
        obj = BaseModel()
        models.storage.new(obj)
        models.storage.save()
        self.assertTrue(os.path.exists(models.storage._FileStorage__file_path))

    def test_reload_empty_file(self):
        """ testing reloading an empty file """
        with self.assertRaises(TypeError):
            models.storage()
            models.storage.reload()


if __name__ == "__main__":
    unittest.main()
