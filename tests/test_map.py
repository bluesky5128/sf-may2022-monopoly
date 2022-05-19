from unittest import TestCase
from levelup.map import Map

class TestMap(TestCase):
    def test_init(self):
        pass
    
    def test_get_width(self):
        test_map = Map(10, 10)
        self.assertEqual(test_map.get_width(), 10)
    
    def test_get_height(self):
        test_map = Map(10, 10)
        self.assertEqual(test_map.get_height(), 10)

    def test_isValid_newposition(self):
        test_map = Map(10, 10)
        self.assertFalse(test_map.is_valid_position((-1, 0)))
        self.assertFalse(test_map.is_valid_position((11, 2)))
        self.assertFalse(test_map.is_valid_position((3, -2)))
        self.assertFalse(test_map.is_valid_position((6, 14)))
