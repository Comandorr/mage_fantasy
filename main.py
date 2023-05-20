import arcade
from pyglet.math import Vec2
from player_class import Player
from enemy_class import Enemy
from functions import load_animation

class Game(arcade.Window):
    def __init__(self):
        super().__init__(1280, 720, vsync=False, title='Mage Fantasy')
        self.center_window()
        arcade.enable_timings()
        self.keys = {
            arcade.key.A:False, 
            arcade.key.D:False,
            arcade.key.W:False,
            arcade.key.S:False,
            arcade.key.SPACE:False,
            arcade.key.ESCAPE:False,
            }
        options = {
            'floor':{
                'use_spatial_hash':True,
                'hit_box_algorithm':'None',},
            'walls1':{
                'use_spatial_hash':True,
                'hit_box_algorithm':'None',},
            'walls2':{
                'use_spatial_hash':True,},
            }
        self.tile_map = arcade.load_tilemap(
            'resources/images/tilesets/map.tmx',
            layer_options=options,
            scaling=3
            )
        
        self.scene = arcade.Scene.from_tilemap(self.tile_map)
        self.scene.add_sprite('Player', Player(self, (100, 100)))
        self.player = self.scene['Player'][0]
        self.scene.add_sprite('sword', self.player.sword)
        #self.bars = self.scene['Water']
        #self.bars.extend(self.scene['Walls'])
        #self.barlist = arcade.AStarBarrierList(self.player, self.scene['Water'], 32, 1300, 2600, 130, 1400)

        self.camera = arcade.Camera()
        self.camera.move(Vec2(1920-self.width/2, 1080-self.height/2))

        self.fps_counter = arcade.Text('', 0, 0, bold = True, font_size = 20)
        arcade.get_fps()
    
    def on_draw(self):
        self.clear()
        self.scene.draw(pixelated=True)
        #self.scene.draw_hit_boxes()
        self.fps_counter.draw()

    def on_update(self, delta_time):
        self.camera.use()
        pos = Vec2(self.player.center_x-self.width/2, self.player.center_y-self.height/2)
        self.camera.move_to(pos, 0.05)
        self.scene.update()
        self.fps_counter.text = str(int(arcade.get_fps()))

        self.fps_counter.position = (self.camera.position[0]+10, self.camera.position[1]+690)

    def on_key_press(self, key, modifiers):
        self.keys[key] = True

    def on_key_release(self, key, modifiers):
        self.keys[key] = False

Game().run()