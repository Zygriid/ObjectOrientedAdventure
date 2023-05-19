import unittest
from thing import *
from actor import *
from cave import *
from place import *


class testaffirmative(unittest.TestCase):

    def setUp(self):
        # Create a room instance and other necessary objects
        # for testing the monsterattack function
        self.room = Room("Room1", 'a nice room')
        self.room._connected_rooms = {'room2, room3, room4'}

        self.player = Player(self.room, "Me", "the player")
        self.monster = Monster(self.room, "Monster", "a fierce monster", 'Food', 'axe', self.player)
        self.room._contents = [self.monster, self.player]

    def test_appease_monster_with_food(self):

        # Call the monsterappease function
        self.player.resources.append("Food")
        self.player.monsterappease(self.monster,"Food")

        # Assert the expected behavior
        self.assertNotEqual(self.player.room, self.monster.room)
        self.assertNotIn("Food", self.player.resources)

    def test_appease_monster_without_food(self):
        with self.assertRaises(PlayerDiedException):
            self.player.monsterappease(self.monster, "")


    def test_attack_monster_with_weapon(self):
        # Test the monsterattack function
        self.weapon = Weapon("axe", "a sharp axe")
        self.player.things.append(self.weapon)
        self.assertTrue(self.weapon in self.player.things)

        self.player.monsterattack(self.monster, 'axe')
        self.assertNotIn(self.monster, self.player.room._contents)

    def test_attack_monster_without_weapon(self):
        # Test if the player cannot attack the monster without having a weapon
        weapon = 'sword'
        with self.assertRaises(PlayerDiedException):
            self.player.monsterattack(self.monster, weapon)

    def test_increase_hunger_and_thirst(self):
        # Verify initial hunger and thirst values
        self.assertEqual(self.player.get_hunger(), 0)
        self.assertEqual(self.player.get_thirst(), 0)

        # Increase hunger and thirst
        self.player.increase_hunger_and_thirst()

        # Verify updated hunger and thirst values
        self.assertEqual(self.player.get_hunger(), 1)
        self.assertEqual(self.player.get_thirst(), 0)

        # Increase hunger and thirst again
        self.player.increase_hunger_and_thirst()

        # Verify updated hunger and thirst values
        self.assertEqual(self.player.get_hunger(), 1)
        self.assertEqual(self.player.get_thirst(), 1)

        # Increase hunger and thirst one more time
        self.player.increase_hunger_and_thirst()

        # Verify updated hunger and thirst values
        self.assertEqual(self.player.get_hunger(), 2)
        self.assertEqual(self.player.get_thirst(), 1)

    def test_pick_up_food(self):

        # Test if the player can successfully pick up food
        item = "food"
        room_contents = ["food"]
        self.player.room._contents = room_contents
        self.player.pick_up(item)
        # Check if the item is added to the resources list
        self.assertIn(item, self.player.resources)
        # Check if the hunger is reset to 0
        self.assertEqual(self.player.get_hunger(), 0)

    def test_pick_up_weapon(self):
        # Test if the player can pick up a generic item (axe)
        item = "axe"
        room_contents = ["axe"]
        self.player.room._contents = room_contents
        self.player.pick_up(item)
        # Check if the item is added to the things list
        self.assertIn(item, self.player.things)

    def test_pick_up_nonexistent_item(self):
        # Test if the player cannot pick up a nonexistent item (key)
        item = "key"
        room_contents = ["food", "water", "axe"]
        self.player.room._contents = room_contents
        self.player.pick_up(item)
        # Check if the item is not added to the resources list
        self.assertNotIn(item, self.player.resources)
        # Check if the item is not added to the things list
        self.assertNotIn(item, self.player.things)


if __name__ == '__main__':
    unittest.main()
