from unittest import TestCase
from levelup.character import Player
from levelup.controller import Direction

class TestPlayer(TestCase):
    def test_init(self):
        pass

    def test_init_player(self):
        test_player = Player('Hello_Kitty')
        self.assertEqual(test_player.name, 'Hello_Kitty')

    def test_set_position(self):
        test_player=Player('XYZ')
        test_player.setposition((0, 2))
        self.assertEqual(test_player.position , (0, 2))
    
    def test_get_position(self):
        test_player = Player('Haha')
        test_player.setposition((3, 2))
        self.assertEqual(test_player.getposition(), (3, 2))