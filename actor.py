from entity import Entity
import random


class PlayerDiedException(Exception):
    pass
class Actor(Entity):

    def __init__(self, room, name, description):
        super().__init__(name, description)
        self._room = room

class Player(Actor):

    def __init__(self, room, name, description):
        super().__init__(room, name, description)
        self.resources = []
        self.things = []
        self.room = room
        self._hunger = 0
        self._thirst = 0
        self._hunger_turn = True
    def get_hunger(self):
        return self._hunger
    def get_thirst(self):
        return self._thirst
    def increase_hunger(self):
        self._hunger += 1
    def increase_thirst(self):
        self._thirst += 1
    def reset_hunger(self):
        self._hunger = 0
    def reset_thirst(self):
        self._thirst = 0

    def move(self, direction):
        if self._room.get_place(direction) is not None:
            self._room = self._room.get_place(direction)
            self.increase_hunger_and_thirst
        else:
            print("You cannot move in that direction.")

    def increase_hunger_and_thirst(self):
        if self._hunger_turn:
            self._hunger += 1
        else:
            self._thirst += 1
        self._hunger_turn = not self._hunger_turn

    def pick_up(self, item):
        if item in self.room._contents:
            if item == "food":
                self.reset_hunger()
                print("You pick up the food.")
                self.resources.append(item)
            elif item == "water":
                self.reset_thirst()
                print("You pick up the water.")
                self.resources.append(item)
            else:
                print(f"you pick up the {item}")
                self.things.append(item)
        else:
            print("There is no such thing!")


    def monsterattack(self, monstername, weapon):
        if self.room == monstername.room:
            monstername.recieveattack(self, weapon)
        else:
            print(f"Luckily, you are not in the same room as {monstername}")

    def monsterappease(self, monstername, item):
        if self.room == monstername.room:
            monstername.recieveappease(self, item)
            self.resources.remove(item)
        else:
            print(f"You arent in the same room as {monstername}!")


    def die(self):
        raise PlayerDiedException('you have been killed.')



class Monster(Actor):

    def __init__(self, room, name, description, wants, killed_by, player):
        super().__init__(room, name, description)
        self._wants = wants
        self._killed_by = killed_by
        self._player = player
        self.room = room
        self.name = name

    def recieveattack(self, player, weapon):
        if weapon == self._killed_by:
            self._player.room._contents.remove(self)  # Remove the monster from the room's contents
            del self  # Delete the monster object
            return f'you have killed the monster'
        else:
            print('the monster kills you')
            player.die()

    def recieveappease(self, player, food):
        if food == self._wants:
            #choose random room
            self.room = random.choice(list(self.room._connected_rooms))
            print(f'{self.name} has been appeased and has moved rooms')

        else:
            print('Appeasing failed')
            player.die()









