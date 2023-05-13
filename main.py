import arcade
from pyglet.math import Vec2
from player_class import Player


class Game(arcade.Window):
    def __init__(self):
        super().__init__(1280, 720, vsync=True, title='Mage Fantasy')
        self.center_window()
        self.keys = {
            arcade.key.A:False, 
            arcade.key.D:False,
            arcade.key.W:False,
            arcade.key.S:False,
            arcade.key.SPACE:False,
            arcade.key.ESCAPE:False,
            }
        options = {
            'Water':{
                'use_spatial_hash':True,
                'hit_box_algorithm':'None',},
            'Ground':{
                'use_spatial_hash':True,
                'hit_box_algorithm':'None',},
            'Walls_sides':{
                'use_spatial_hash':True,},
            'Walls':{
                'use_spatial_hash':True,
},
            }
        self.tile_map = arcade.load_tilemap(
            'resources/images/tilesets/map.tmx',
            scaling=3*self.width/1280,
            layer_options=options
            )
        
        self.scene = arcade.Scene.from_tilemap(self.tile_map)
        self.scene.add_sprite_list('Projectiles')
        self.scene.add_sprite('Player', Player(self, (1920, 1080)))
        self.player = self.scene['Player'][0]

        self.camera = arcade.Camera()
        self.camera.move(Vec2(1920-self.width/2, 1080-self.height/2))

        self.explosion_sound = arcade.load_sound('resources/sounds/explosion.ogg')
    
    def on_draw(self):
        self.clear()
        self.scene.draw(pixelated=True)
        #self.scene.draw_hit_boxes()

    def on_update(self, delta_time):
        self.camera.use()
        pos = Vec2(self.player.center_x-self.width/2, self.player.center_y-self.height/2)
        self.camera.move_to(pos, 0.05)
        self.scene.update()

    def on_key_press(self, key, modifiers):
        self.keys[key] = True

    def on_key_release(self, key, modifiers):
        self.keys[key] = False

    def on_mouse_press(self, x, y, button, key_modifiers):
        x+=self.camera.position[0]
        y+=self.camera.position[1]
        self.player.shoot((x, y))

Game().run()