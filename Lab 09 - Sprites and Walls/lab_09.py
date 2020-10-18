import random
import arcade
import os

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 50

MOVEMENT_SPEED = 5

NUMBER_OF_WORMS = 100


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.player_list = None

        self.worm_list = None
        self.score = 0

        self.player_sprite = None
        self.wall_list = None
        self.physics_engine = None
        self.worm_sound = arcade.load_sound("sd_0.wav")

        # Used in scrolling
        self.view_bottom = 0
        self.view_left = 0
        self.set_mouse_visible(False)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.worm_list = arcade.SpriteList()
        # Set up the player
        # Icon from kenny.nl
        self.player_sprite = arcade.Sprite("chicken.png", 0.4)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 270
        self.player_list.append(self.player_sprite)

        # -- Set up several columns of walls
        # long piece
        for x in range(100, 940, 80):
            # Randomly skip a box so the player can find a way through
            # Image from iconfinder.com
            wall = arcade.Sprite("fence.png", .3)
            wall.center_x = x
            wall.center_y = 400
            self.wall_list.append(wall)

        for x in range(-1500, 940, 80):
            wall = arcade.Sprite("fence.png", .3)
            wall.center_x = x
            wall.center_y = 250
            self.wall_list.append(wall)

        for y in range(250, 1260, 75):
            wall = arcade.Sprite("fence.png", .3)
            wall.center_x = 980
            wall.center_y = y
            self.wall_list.append(wall)
    # Square piece
        for y in range(460, 530, 75):
            wall = arcade.Sprite("fence.png", .3)
            wall.center_x = 100
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(600, 750, 75):
            wall = arcade.Sprite("fence.png", .3)
            wall.center_x = 100
            wall.center_y = y
            self.wall_list.append(wall)

        for x in range(100, 640, 75):
            wall = arcade.Sprite("fence.png", .3)
            wall.center_x = x
            wall.center_y = 750
            self.wall_list.append(wall)

        for y in range(820, 1200, 75):
            wall = arcade.Sprite("fence.png", .3)
            wall.center_x = 625
            wall.center_y = y
            self.wall_list.append(wall)

        for x in range(-1500, 1000, 80):
            wall = arcade.Sprite("fence.png", .3)
            wall.center_x = x
            wall.center_y = 1265
            self.wall_list.append(wall)

        for y in range(250, 1300, 80):
            wall = arcade.Sprite("fence.png", .3)
            wall.center_x = -1580
            wall.center_y = y
            self.wall_list.append(wall)

        # Tree walls
        for y in range(800, 1220, 80):
            wall = arcade.Sprite("tree.png", 1)
            wall.center_x = -900
            wall.center_y = y
            self.wall_list.append(wall)

        for x in range(-1420, -600, 80):
            wall = arcade.Sprite("tree.png", 1)
            wall.center_x = x
            wall.center_y = 700
            self.wall_list.append(wall)
        # Dogs
        wall = arcade.Sprite("dog.png", .3)
        wall.center_x = -300
        wall.center_y = 700
        self.wall_list.append(wall)

        wall = arcade.Sprite("dog.png", .3)
        wall.center_x = -1200
        wall.center_y = 1000
        self.wall_list.append(wall)

        wall = arcade.Sprite("dog.png", .3)
        wall.center_x = -800
        wall.center_y = 500
        self.wall_list.append(wall)

        wall = arcade.Sprite("dog.png", .3)
        wall.center_x = -1350
        wall.center_y = 400
        self.wall_list.append(wall)

        for i in range(NUMBER_OF_WORMS):

            # worm image from shareicon.net
            worm = arcade.Sprite("worm.png", .2)

            # --- IMPORTANT PART ---

            worm_placed_successfully = False

            while not worm_placed_successfully:
                worm.center_x = random.randrange(-1400, 1100)
                worm.center_y = random.randrange(350, 1000)

                wall_hit_list = arcade.check_for_collision_with_list(worm, self.wall_list)

                worm_hit_list = arcade.check_for_collision_with_list(worm, self.worm_list)

                if len(wall_hit_list) == 0 and len(worm_hit_list) == 0:
                    worm_placed_successfully = True

            self.worm_list.append(worm)

            # --- END OF IMPORTANT PART ---

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.worm_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, -500, 500, arcade.color.WHITE, 36)

        if len(self.worm_list) == 0:
            output = f"Game over."
            arcade.draw_text(output, 500, 400, arcade.color.WHITE, 60)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """
        worm_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.worm_list)

        self.physics_engine.update()

        if len(self.worm_list) > 0:
            for worm in worm_hit_list:
                worm.remove_from_sprite_lists()
                self.score += 1
                arcade.play_sound(self.worm_sound)

        # --- Manage Scrolling ---

        # Keep track of if we changed the boundary. We don't want to call the
        # set_viewport command if we didn't change the view port.
        changed = False

        # Scroll left
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        # Make sure our boundaries are integer values. While the view port does
        # support floating point numbers, for this application we want every pixel
        # in the view port to map directly onto a pixel on the screen. We don't want
        # any rounding errors.
        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

        # If we changed the boundary values, update the view port to match
        if changed:
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
