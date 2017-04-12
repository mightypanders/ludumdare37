from const import *


class OneRoom(arcade.Window):
	def __init__(self, w, h):
		super().__init__(w, h, "One Room Game")

		arcade.set_background_color(arcade.color.DARK_PINK)
		self.texture = get_wall_tex()
		self.allsprites = arcade.SpriteList()
		self.wallsprites = arcade.SpriteList()
		self.setup_walls()
		self.texture = get_tile_tex()
		self.setup_grid()
		arcade.schedule(self.paint, 1 / 160)

	def setup_walls(self):
		col_w = self.texture.width
		row_h = self.texture.height
		col_c = int(SCREENW // col_w)
		row_c = int(SCREENH // row_h)

		for i in range(0, col_c, 1):
			self.wallsprites.append(tile(self.texture, i * col_w, 0))
			self.wallsprites.append(tile(self.texture, i * col_w, SCREENH - row_h))

		for j in range(0, row_c, 1):
			self.wallsprites.append(tile(self.texture, 0, j * row_h))
			self.wallsprites.append(tile(self.texture, SCREENW - col_w, j * row_h))

	def setup_grid(self):
		col_w = self.texture.width
		row_h = self.texture.height
		col_c = int((SCREENW - (col_w * 2)) // col_w)
		row_c = int((SCREENH - (row_h * 2)) // row_h)

		for j in range(1, row_c + 1, 1):
			for i in range(1, col_c + 1, 1):
				self.allsprites.append(tile(self.texture, i * col_w, j * row_h))

	def paint(self, deltatime):

		arcade.start_render()
		self.allsprites.draw()
		self.wallsprites.draw()


class tile(arcade.Sprite):
	def __init__(self, texture, x, y):
		super().__init__()
		self.left = x + (texture.width // 2)
		self.bottom = y + (texture.height // 2)

		self.texture = texture


class player(arcade.AnimatedWalkingSprite):
	def __init__(self):
		super().__init__()


def main():
	OneRoom(SCREENW, SCREENH)
	arcade.run()


if __name__ == '__main__':
	main()
