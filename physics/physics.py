class PhysicsObject:
    def __init__(self, x, y, mass):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0

        self.mass = mass

    def apply_force(self, fx, fy, x, y):
        self.vx += fx / self.mass
        self.vy += fy / self.mass

    def move(self):
        self.x += self.vx
        self.y += self.vy

    def position(self):
        return self.x, self.y