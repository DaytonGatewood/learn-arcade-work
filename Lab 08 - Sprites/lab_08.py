import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.7
SPRITE_SCALING_BANANA = 0.2
BANANA_COUNT = 80
SPRITE_SCALING_SNAKE = 0.4
SNAKE_COUNT = 25

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800


class Banana(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.magical_sound = arcade.load_sound("magical_1.ogg")

        self.change_y = 0
        self.change_x = 0

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class Snake(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

    def update(self):
        self.center_y -= 1

        if self.top < 0:
            self.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 40)
            self.center_x = random.randrange(SCREEN_WIDTH)


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists
        self.player_list = None
        self.banana_list = None
        self.snake_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.GO_GREEN)

        # Sounds from OpenGameArt.org
        self.good_sound = arcade.load_sound("sd_0.wav")
        self.bad_sound = arcade.load_sound("MS_Realization.wav")

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.banana_list = arcade.SpriteList()
        self.snake_list = arcade.SpriteList()
        # Score

        self.score = 0

        # Elephant image from kenney.nl
        self.player_sprite = arcade.Sprite("elephant.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 60
        self.player_sprite.center_y = 60
        self.player_list.append(self.player_sprite)

        for i in range(BANANA_COUNT):
            # banana image from icon-library.com
            banana = Banana("banana.png", SPRITE_SCALING_BANANA)

            banana.center_x = random.randrange(SCREEN_WIDTH)
            banana.center_y = random.randrange(SCREEN_HEIGHT)
            banana.change_x = random.randrange(-3, 4)
            banana.change_y = random.randrange(-3, 4)

            self.banana_list.append(banana)

        for i in range(SNAKE_COUNT):
            # banana image from kenny.nl
            snake = Snake("snake.png", SPRITE_SCALING_SNAKE)

            snake.center_x = random.randrange(SCREEN_WIDTH)
            snake.center_y = random.randrange(SCREEN_HEIGHT)


            self.snake_list.append(snake)

    def on_draw(self):
        arcade.start_render()

        self.banana_list.draw()
        self.player_list.draw()
        self.snake_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 36)

        if len(self.banana_list) == 0:
            output = f"Game over."
            arcade.draw_text(output, 300, 400, arcade.color.WHITE, 60)

    def on_mouse_motion(self, x, y, dx, dy):
        """"Handle Mouse Motion"""
        if len(self.banana_list) > 0:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def update(self, delta_time):
        """Movement and game logic"""
        self.banana_list.update()

        bananas_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.banana_list)
        snake_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.snake_list)

        if len(self.banana_list) > 0:
            for banana in bananas_hit_list:
                banana.remove_from_sprite_lists()
                self.score += 1
                arcade.play_sound(self.good_sound)

            self.snake_list.update()

            for snake in snake_hit_list:
                snake.remove_from_sprite_lists()
                self.score -= 1
                arcade.play_sound(self.bad_sound)


def main():
    """ Main method """
    window = MyGame()

    window.setup()

    arcade.run()


if __name__ == "__main__":
    main()
