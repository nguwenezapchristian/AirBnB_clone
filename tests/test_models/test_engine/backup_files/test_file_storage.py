#!/usr/bin/python3
"""
Test for file_storage
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.__init__ import storage

class TestFileStorage_instantiation(unittest.TestCase):
    """
    Test for storage
    """

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)
    
    def test_save(self):
        my_base_model = BaseModel()
        my_user = User()
        my_state = Place()
        my_city = City()
        my_amenity = Amenity()
        my_review = Review()
        models.storage.new(my_base_model)
        models.storage.new(my_user)
        models.storage.new(my_state)
        models.storage.new(my_place)
        models.storage.new(my_city)
        models.storage.new(my_amenity)
        models.storage.new(my_review)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + my_base_model.id, save_text)
            self.assertIn("User." + my_user.id, save_text)
            self.assertIn("State." + my_state.id, save_text)
            self.assertIn("Place." + my_place.id, save_text)
            self.assertIn("City." + my_city.id, save_text)
            self.assertIn("Amenity." + my_amenity.id, save_text)
            self.assertIn("Review." + my_review.id, save_text)

        def test_save_with_arg(self):
            with self.assertRaises(TypeError):
                models.storage.save(None)

        def tes_reload(self):
            my_base_model = BaseModel()
            my_user = User()
            my_state = State()
            my_place = Place()
            my_city = City()
            my_amenity = Amenity()
            my_review = Review()
            models.storage.new(my_base_model)
            models.storage.new(my_user)
            models.storage.new(my_state)
            models.storage.new(my_place)
            models.storage.new(my_city)
            models.storage.new(my_amenity)
            models.storage.new(my_review)
            models.storage.save()
            models.storage.reload()
            objs = FileStorage._FileStorage__objects
            self.assertIn("BaseModel." + my_base_model.id, objs)
            self.assertIn("User." + my_user.id, objs)
            self.assertIn("State." + my_state.id, objs)
            self.assertIn("Place." + my_place.id, objs)
            self.assertIn("City." + my_city.id, objs)
            self.assertIn("Amenity." + my_amenity.id, objs)
            self.assertIn("Review." + my_review.id, objs)

        def test_reload_with_arg(self):
            with self.assertraises(TypeError):
                models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
