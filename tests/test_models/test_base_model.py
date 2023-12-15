#!/usr/bin/python3
"""
    Module for testing BaseModel
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    This class will be use to test attributes
    and methodes of an instance
    """
    def setUp(self):
        """ setting up a common instance for testing """
        self.inst_model = BaseModel()

    def test_init(self):
        """ testing the contructor of the BaseModel """
        self.assertIsNotNone(self.inst_model.id)
        self.assertIsNotNone(self.inst_model.created_at)
        self.assertIsNotNone(self.inst_model.updated_at)

    def test_str(self):
        """ testing the __str__() method for string repr of instance """ 
        self.assertTrue(str(self.inst_model).startswith('[BaseModel]'))
        self.assertIn(self.inst_model.id, str(self.inst_model))
        self.assertIn(str(self.inst_model.id), str(self.inst_model))
        self.assertIn(
                f"'created_at': {repr(self.inst_model.created_at)}",
                str(self.inst_model)
                )
        self.assertIn(
                f"'updated_at': {repr(self.inst_model.updated_at)}",
                str(self.inst_model)
                )

    def test_save(self):
        """ testing save() method which is updating the datetime """
        init_updated_at = self.inst_model.updated_at
        self.inst_model.save()
        current_updated_at = self.inst_model.updated_at
        self.assertNotEqual(init_updated_at, current_updated_at)

    def test_to_dict(self):
        """ testing to_dict() method which is doing serialization """
        inst_model_dict = self.inst_model.to_dict()
        self.assertIsInstance(inst_model_dict, dict)
        self.assertEqual(inst_model_dict['__class__'], 'BaseModel')
        self.assertEqual(inst_model_dict['id'], self.inst_model.id)
        self.assertEqual(
                inst_model_dict['created_at'],
                (self.inst_model.created_at).isoformat()
                )
        self.assertEqual(
                inst_model_dict['updated_at'],
                (self.inst_model.updated_at).isoformat()
                )


if __name__ == "__main__":
    unittest.main()
