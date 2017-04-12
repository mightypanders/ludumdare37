import arcade

SCREENW=800
SCREENH=600

tile_tex=arcade.draw_commands.Texture

def get_wall_tex():
	tile_tex=arcade.load_texture("../tiles/wall.png")
	return tile_tex

def get_tile_tex():
	tile_tex=arcade.load_texture("../tiles/til2.png")
	return  tile_tex