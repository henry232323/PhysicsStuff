from . import inertia


class Cylinder(inertia.InertiaObject):
    def __init__(self, x, y, mass, radius, hollow=True, thickness=0):
        moi = self.moment_of_inertia()
        self.hollow = hollow
        self.thickness = thickness
        self.radius = radius
        super().__init__(x, y, mass, moi)

    def moment_of_inertia(self):
        if self.hollow:
            moi = .5 * self.mass * ((self.radius - self.thickness) ** 2 + self.radius ** 2)
        else:
            moi = .5 * self.mass * self.radius ** 2
        return moi
