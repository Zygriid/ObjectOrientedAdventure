"""
Class Hierarchy:
    Entity
        Actor
            Player
            Monster
        Place
            Room
            Passageway
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
For debugging, will connect everything to cave, but will try
    not to use that information in the code

"""

class Entity:

    def __init__(self, name, description):
        self._name = name
        self._description = description

    def __str__(self):
        return self._description

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description




