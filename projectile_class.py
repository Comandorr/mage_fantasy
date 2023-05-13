import arcade
from pyglet.math import Vec2
from functions import load_animation
from math import degrees
from explosion_class import Explosion


class Projectile(arcade.Sprite):
    def __init__(self, owner, target, walls):
        self.vec = Vec2(target[0]-owner.center_x, target[1]-owner.center_y).normalize()
        super().__init__(
            filename=':resources:images/space_shooter/laserRed01.png',
            center_x=owner.center_x,
            center_y=owner.center_y,
            scale = 1.5,
            angle = degrees(self.vec.heading)-90
            )
        self.speed = 10
        self.walls = walls
        self.window = owner.window

    def update(self):
        for wall in self.collides_with_list(self.walls):
            self.kill()
            Explosion(self, wall)

        self.change_x = self.vec.x*self.speed
        self.change_y = self.vec.y*self.speed
        super().update()