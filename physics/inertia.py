import math

from . import physics


class InertiaObject(physics.PhysicsObject):
    def __init__(self, x, y, mass, moi=None):
        super().__init__(x, y, mass)
        if moi is None:
            self.inertia = self.moment_of_inertia()
        else:
            self.inertia = lambda: moi
        self.mass = mass
        self.angular_accel = 0
        self.rotation = 0

    def apply_force(self, fx, fy, x, y):
        dist = math.hypot(self.x - x, self.y - y)
        thetapos = math.atan2(self.x-x, self.y-y)
        torque = math.hypot(fx, fy) * dist * math.sin(math.atan2(fx, fy) + thetapos)
        radforce = math.hypot(fx, fy) * math.cos(math.atan2(fx, fy) + thetapos)

        super().apply_force(radforce * math.cos(thetapos), radforce * math.sin(thetapos), x, y)

        self.angular_accel += torque / self.inertia()

    def move(self):
        super().move()
        self.rotation += self.angular_accel

    def moment_of_inertia(self):
        raise NotImplementedError("Implement this when you subclass, or pass the `moi` argument for a static"
                                  " moment of inertia")
