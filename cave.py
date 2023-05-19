

class Cave:

    def __init__(self,
                 rooms,
                 passages,
                ):
        self._rooms = rooms
        self._passages = passages

    def get_passage(self, name):
        return self._passages.get(name, None)

    def get_room(self, name):
        assert name in self._rooms
        return self._rooms[name]

    def get_rooms(self):
        return self._rooms

    def __str__(self):
        return str("The Cave")

    def describe(self):
        print("State of the Cave:")
        print("\tConnections:")
        for room in self._rooms.values():
            print(f"\t{room.get_name()}")
            for direction, other in room.get_connections().items():
                print(f"""\t\t{direction}: {other.get_name()}""")

#    Rooms:""")

# for name, description in self._rooms.items():
#            print(f"""\t\t{name}: {description}""")
