import arcade
from functions import load_animation
from pyglet.math import Vec2
import random

class Explosion(arcade.AnimatedTimeBasedSprite):
    def __init__(self, owner, wall):
        super().__init__()
        self.window = owner.window
        self.frames = load_animation(
            ':resources:images/spritesheets/explosion.png',
            256, (4096, 3584), 5)
        self.center_x = wall.center_x
        self.center_y = wall.center_y
        self.set_hit_box(self.frames[10].texture.hit_box_points)
        owner.window.scene['Projectiles'].append(self)
        owner.window.camera.shake(Vec2(random.choice([-2, 2]), random.choice([-3, 3])), speed=1, damping=0.95)
        owner.window.camera.update()
        arcade.play_sound(owner.window.explosion_sound)
        for wall in arcade.check_for_collision_with_list(self, self.window.scene['Walls']):
            wall.kill()
        for wall in arcade.check_for_collision_with_list(self, self.window.scene['Walls_sides']):
            wall.kill()
        #for wall in arcade.check_for_collision_with_list(self, self.window.scene['Ground']):
        #    wall.kill()
    
    def update(self):
        super().update()
        self.update_animation()
        if self.cur_frame_idx == len(self.frames)-1:
            self.kill()