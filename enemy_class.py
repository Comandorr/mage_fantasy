import arcade
import math
from pyglet.math import Vec2


class Enemy(arcade.Sprite):
    def __init__(self, filename, window, **kwargs):
        for i in ['flipped_horizontally', 'flipped_vertically', 'flipped_diagonally', 'hit_box_algorithm', 'hit_box_detail']:
            del kwargs[i]
        super().__init__(filename, **kwargs)
        self.window = window
        self.path = None
    def setup(self):
        self.scene = self.window.scene
        #self.barlist = self.window.barlist
        self.pos = 0
        self.speed = 3

    def update(self):
        self.change_x = 0
        self.change_y = 0
        #if self.window.player.change_x!=0 or self.window.player.change_y!=0:
        #if arcade.has_line_of_sight(self.position, self.window.player.position, self.window.scene['Water'], 2000, 16):
        # self.path = arcade.astar_calculate_path(self.position,
        #                                             self.window.player.position,
        #                                             self.window.barlist,
        #                                             diagonal_movement=True)


        # if self.path and len(self.path) > 2:


            # dest_x = self.path[self.pos][0]
            # dest_y = self.path[self.pos][1]

            # x_diff = dest_x - self.center_x
            # y_diff = dest_y - self.center_y

            # angle = math.atan2(y_diff, x_diff)

            # distance = arcade.get_distance(self.center_x, self.center_y, dest_x, dest_y)

            # speed = min(self.speed, distance)

            # self.change_x = math.cos(angle) * speed
            # self.change_y = math.sin(angle) * speed


            # distance = arcade.get_distance(self.center_x, self.center_y, dest_x, dest_y)

            # if distance <= self.speed:
                # self.pos += 1
            # if self.pos >= len(self.path):
                # self.pos = 0

        super().update()