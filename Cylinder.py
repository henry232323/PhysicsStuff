import InertiaObject


class Cylinder(InertiaObject.InertiaObject):
    def __init__(self, x, y, mass, radius, hollow=True, thickness=0):
        if hollow:
            moi = .5 * mass * ((radius - thickness) ** 2 + radius ** 2)
        else:
            moi = .5 * mass * radius ** 2

        super().__init__(x, y, mass, moi)
        