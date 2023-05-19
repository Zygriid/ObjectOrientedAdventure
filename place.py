from entity import Entity

class Place(Entity):

    def __init__(self, name, description):
        super().__init__(name, description)
        self._contents = {}
        self._connections = {}

    def get_place(self, direction):
        return self._connections.get(direction, None)

    def get_connections(self):
        return self._connections

class Room(Place):

    def __init__(self, name, description):
        super().__init__(name, description)
        self._contents = []
        self._connected_rooms = {}
        self._name = name

    def connect(self, direction, other):
        assert direction in ['N', 'E', 'W', 'S']
        self._connections[direction] = other

    def describe(self):
        "Describe the things and actors in the room"
        print(self._room, self._description)

class Passage(Place):
    """Goes from one room to another where rooms do not
    connect directly"""

    def __init__(self, name, description):
        super().__init__(name, description)

