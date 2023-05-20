import arcade
from pyglet.math import Vec2
from functions import load_animations2
from projectile_class import Projectile

class Player(arcade.Sprite):
    def __init__(self, window, position):
        self.window = window
        self.scene = self.window.scene
        self.frames = []
        self.time_counter = 0
        self.cur_frame_idx = 0
        self.state = 'idle'
        self.side = 'right'
        file = 'resources/images/tilesets/knight_.png'
        super().__init__(
            filename = file,
            image_x = 0,
            image_y = 32,
            image_width = 32,
            image_height = 32,
            center_x=position[0],
            center_y=position[1],
            scale=3,
            )
        
        self.engine = arcade.PhysicsEngineSimple(self, self.scene['walls2'])

        self.speed = 5
        load = [['idle',4], ['run',4], ['jump',4],  ['turn',4], ['hurt',4], ['death',4]]
        self.animations = load_animations2(load, file)
        self.change_animation(self.side, self.state)
        self.sword = arcade.Sprite(
            'resources/images/tilesets/weapons_.png',
            scale=3, image_x=24, image_y=0, image_width=12, image_height=24,
            center_x=self.right, center_y=self.center_y)
    
    def update(self, delta_time: float = 1 / 60):
        self.change_x = 0
        if self.window.keys[arcade.key.D] and not self.window.keys[arcade.key.A]:
            self.change_x = self.speed
            if self.side != 'right':
                self.change_animation('right', 'run')
        elif self.window.keys[arcade.key.A] and not self.window.keys[arcade.key.D]:
            self.change_x = -self.speed
            if self.side != 'left':
                self.change_animation('left', 'run')

        self.change_y = 0
        if self.window.keys[arcade.key.W] and not self.window.keys[arcade.key.S]:
            self.change_y = self.speed
            if self.state != 'run':
                self.change_animation(self.side, 'run')
        elif self.window.keys[arcade.key.S] and not self.window.keys[arcade.key.W]:
            self.change_y = -self.speed
            if self.state != 'run':
                self.change_animation(self.side, 'run')

        if self.change_x == 0 and self.change_y == 0:
            if self.state == 'run':
                self.change_animation(self.side, 'idle')
        else:
            if self.state != 'run':
                self.change_animation(self.side, 'run')

        vec = Vec2(self.change_x, self.change_y).normalize()
        self.change_x = vec[0]*self.speed
        self.change_y = vec[1]*self.speed
        #super().update()
        if self.side == 'right':
            self.sword.center_x=self.center_x+self.width/2
        else:
            self.sword.center_x=self.center_x-self.width/2
        self.sword.center_y=self.center_y
        self.sword.angle += 1
        pos = arcade.rotate_point(self.sword.center_x, self.sword.center_y, self.center_x, self.center_y, self.sword.angle)
        #self.sword.turn_left(1)
        self.sword.position = pos
        self.engine.update()
        self.update_animation()

    def change_animation(self, side, state):
        self.side, self.state = side, state
        self.frames = self.animations[self.side][self.state]
        #self.cur_frame_idx = -1
        #self.time_counter = 0
        self.update_animation()

    def update_animation(self, delta_time: float = 1 / 60):
        self.time_counter += delta_time
        while self.time_counter > self.frames[self.cur_frame_idx].duration / 1000.0:
            self.time_counter -= self.frames[self.cur_frame_idx].duration / 1000.0
            self.cur_frame_idx += 1
            if self.cur_frame_idx >= len(self.frames):
                self.cur_frame_idx = 0
            cur_frame = self.frames[self.cur_frame_idx]
            self.texture = cur_frame.texture