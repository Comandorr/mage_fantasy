import arcade
from pyglet.math import Vec2

class Player(arcade.Sprite):
    def __init__(self, window, position):
        self.window = window
        self.scene = self.window.scene
        super().__init__(
            filename = 'resources/images/tilesets/player.png',
            image_x = 0,
            image_y = 32,
            image_width = 32,
            image_height = 32,
            center_x=position[0],
            center_y=position[1],
            scale=3,
            )
        
        self.speed = 5
        self.load = {
            'spawn':4, 
            'idle':4, 
            'run':8, 
            'jump_idle':1, 
            'jump_run':1, 
            'land':3, 
            'roll':8, 
            'turn':4, 
            'hit':4, 
            'death':4
            }


    def update(self, delta_time: float = 1 / 60):
        self.change_x = 0
        if self.window.keys[arcade.key.D] and not self.window.keys[arcade.key.A]:
            self.change_x = self.speed
        elif self.window.keys[arcade.key.A] and not self.window.keys[arcade.key.D]:
            self.change_x = -self.speed

        self.change_y = 0
        if self.window.keys[arcade.key.W] and not self.window.keys[arcade.key.S]:
            self.change_y = self.speed
        elif self.window.keys[arcade.key.S] and not self.window.keys[arcade.key.W]:
            self.change_y = -self.speed

        vec = Vec2(self.change_x, self.change_y).normalize()
        self.change_x = vec[0]*self.speed
        self.change_y = vec[1]*self.speed
        super().update()

