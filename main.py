import arcade
from pyglet.math import Vec2


class Game(arcade.Window):
	def __init__(self):
		super().__init__(1280, 720, vsync=True, title='Mage Fantasy')
		self.center_window()
		options = {
			'Ground':{
				'use_spatial_hash':True,
				'hit_box_algorithm':None,}
		}
		self.tile_map = arcade.load_tilemap(
			'resources/images/tilesets/map.tmx',
			scaling=3*self.width/1280,
			layer_options=options
			)
		self.scene = arcade.Scene.from_tilemap(self.tile_map)
		self.camera = arcade.Camera()
		self.camera.move(Vec2(1920-self.width/2, 1080-self.height/2))
	
	def on_draw(self):
		self.clear()
		self.scene.draw(pixelated=True)

	def on_update(self, delta_time):
		self.camera.use()

	def on_key_press(self, key, modifiers):
		pass

	def on_key_release(self, key, modifiers):
		pass

Game().run()