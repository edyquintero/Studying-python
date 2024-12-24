class Ship:
    def __init__(self, ship_location, size, orientation):
        self.ship_location = ship_location
        self.size = size
        self.orientation = orientation
        self.hits = 0

    def is_sunk(self):
        return self.hits >= self.size
