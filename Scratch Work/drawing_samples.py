""" Sprite Sample Program """

import arcade

# --- Constants ---
SPRITE_SCALING_BOX = 0.5
SPRITE_SCALING_PLAYER = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ This class represents the main window of the game. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprites With Walls Example")

        # Sprite List
        self.player_list = None
        self.wall_list = None

        # Players
        self.player_sprite = None

        # Physics engine
        self.physics_engine = None

    def setup(self):
        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        self.score = 0

        self.player_sprite = arcade.Sprite("elephant.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 64
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        arcade.start_render()
        self.wall_lsit.draw()
        slef.player_list.draw()

def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()