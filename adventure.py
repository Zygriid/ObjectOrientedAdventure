from cave import *
from place import *
from thing import *
from actor import *


"""
Class Hierarchy:
    Entity
        Actor
            Player
            Monster
        Place
            Room
            Passage
        Thing
            Resource
            Weapon

Places
    are connected to other places
    contain Things
    contain Actors

Actors
    are located in a place
    carry Things
    need Resources
    can move from where they are through a connection

This Adventure class creates and places everything.
Initial assumption is that once the game starts nothing
    needs to know about the cave

"""

#  This game's initial setup is fixed, not randomly generated
class Adventure:

    cave_layout = {
        'RA': {'N': 'RB', 'S': 'RC', },
        'RB': {'E': 'RD', 'W': 'RE', },
        'RC': {'W': 'RA', 'E': 'RB', 'S': 'RD', },
        'RD': {'W': 'RB', 'E': 'RC', },
        'RE': {'E': 'RB', 'S': 'RF', },
        'RF': {'N': 'RE'},
    }

    def __init__(self):
        self.setup_cave()

        self.create_things()

        self.create_monsters()
        self.player = Player(self, "Me", "the player")

    def setup_cave(self):
        self.create_cave()
        self.connect_places()

    def create_cave(self):
        """Create the cave and initialize it with Rooms
        Passages. The Rooms and Passages have no
        connections yet"""
        self._cave = Cave(
            {
                'RA': Room('RA', "room A"),
                'RB': Room('RB', "room B"),
                'RC': Room('RC', "room C"),
                'RD': Room('RD', "room D"),
                'RE': Room('RE', "room E"),
                'RF': Room('RF', "room F"),
            },
            {
                'P1': Passage('P1', 'passage 1'),
                'P2': Passage('P2', 'passage 2'),
            },
         )

    def connect_places(self):
        for room_name, connections in self.cave_layout.items():
            for direction, other_room_name in connections.items():
                self._cave.get_rooms()[room_name].connect(
                    direction,
                    self._cave.get_room(other_room_name)
                )

    def create_things(self):
        self.create_treasures()
        self.create_weapons()
        self.create_resources()

    def create_resources(self):
        self._resources = {
            'water': Resource('water', 'a bottle of water'),
            'food': Resource('food', 'some delicions food'),
        }

    def create_treasures(self):
        self._treasures = {
            'diamonds': Treasure('diamonds', '6 diamonds', 100),
            'coins': Treasure('coins', '10 coins', 50),
        }

    def create_weapons(self):
        self._weapons = {
            'axe': Weapon('axe', 'a sharp axe'),
            'rock': Weapon('rock', 'a heavy stone'),
        }

    def create_monsters(self):
        self._monsters = {
            'M1': Monster(self,
                          'miniturtle',
                          'a tiny turtle',
                          self._resources['food'],
                          self._weapons['axe'],
                          player),
            'M2': Monster(self,
                          'Turtlemonster',
                          'a giant turtle',
                          self._resources['water'],
                          self._weapons['rock'],
                          player),
        }



    def place_everything(self):
        """Put the things in rooms"""

    def create_player(self):
        self.player = {
            'player': Player(self,
                             self._location,
                             'Tosca',
                             'An intrepid turtle hunter')
        }
game = Adventure()

script = GameScript()
script.play(game)

game._cave.describe()

