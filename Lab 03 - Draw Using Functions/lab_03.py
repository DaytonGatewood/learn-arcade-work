import arcade

screen_width = 1000
screen_height = 1000

def person_sledding(x,y):
    """Draw a person sledding"""

    # Draw the sled
    arcade.draw_lrtb_rectangle_filled(x + 500, x + 600, y + 800, y + 795, arcade.csscolor.BROWN)

    # Draw the head
    arcade.draw_circle_filled(x + 550, y + 830, 10, arcade.csscolor.YELLOW)

    # Draw the Body
    arcade.draw_line(x + 550, y + 800, x + 550, y + 830, arcade.csscolor.YELLOW)
    arcade.draw_line(x + 550, y + 810, x + 565, y + 825, arcade.csscolor.YELLOW)
    arcade.draw_line(x + 535, y + 825, x + 550, y + 810, arcade.csscolor.YELLOW)

    # Draw the Hat
    arcade.draw_triangle_filled(x + 540, y + 837, x + 550, y + 855, x + 560, y + 837, arcade.csscolor.PURPLE)
    arcade.draw_circle_filled(x + 550, y + 855, 5, arcade.csscolor.PINK)


def draw_sun():
    """Draw the sun"""

    arcade.draw_circle_filled(999, 999, 100, arcade.csscolor.YELLOW)


def draw_snow():
    """Draw The Snow"""

    arcade.draw_lrtb_rectangle_filled(0, 1000, 700, 0, arcade.csscolor.WHITE)
    arcade.draw_ellipse_filled(100, 700, 700, 200, arcade.csscolor.WHITE)
    arcade.draw_ellipse_filled(600, 700, 700, 200, arcade.csscolor.WHITE)
    arcade.draw_ellipse_filled(900, 700, 400, 200, arcade.csscolor.WHITE)
def draw_tree(x,y):
    """Draw a tree"""

    # Draw the log
    arcade.draw_lrtb_rectangle_filled(x + 10, x + 20, y + 50, y + 10, arcade.csscolor.BROWN)

    # Draw the leaves
    arcade.draw_triangle_filled(x - 10, y + 40, x + 15, y + 70, x + 40, y + 40, arcade.csscolor.GREEN)
    arcade.draw_triangle_filled(x - 10, y + 65, x + 15, y + 95, x + 40, y + 65, arcade.csscolor.GREEN)
    arcade.draw_triangle_filled(x - 10, y + 90, x + 15, y + 120, x + 40, y + 90, arcade.csscolor.GREEN)

def draw_bear(x,y):
    """Draw a bear"""

    # Draw the body
    arcade.draw_lrtb_rectangle_filled(x + 100, x + 200, y + 200, y + 160, arcade.csscolor.SADDLE_BROWN)
    arcade.draw_lrtb_rectangle_filled(x + 100, x + 115, y + 160, y + 140, arcade.csscolor.SADDLE_BROWN)
    arcade.draw_lrtb_rectangle_filled(x + 185, x + 200, y + 160, y + 140, arcade.csscolor.SADDLE_BROWN)

    # Draw the head
    arcade.draw_circle_filled(x + 210, y + 210, 30, arcade.csscolor.SADDLE_BROWN)

    # Draw the ears and tail
    arcade.draw_circle_filled(x + 190, y + 235, 6, arcade.csscolor.SADDLE_BROWN)
    arcade.draw_circle_filled(x + 230, y + 235, 6, arcade.csscolor.SADDLE_BROWN)
    arcade.draw_circle_filled(x + 97, y + 198, 5, arcade.csscolor.SADDLE_BROWN)


def main():
    arcade.open_window(screen_width, screen_height, "Dayton's Cool New Drawing")
    arcade.set_background_color(arcade.csscolor.DEEP_SKY_BLUE)
    arcade.start_render()

    draw_snow()
    draw_sun()

    person_sledding(0,0)
    person_sledding(-100,-200)
    person_sledding(100,-400)
    person_sledding(-100,-600)
    person_sledding(100,-800)

    draw_tree(100,100)
    draw_tree(300, 500)
    draw_tree(200, 750)
    draw_tree(50, 600)
    draw_tree(800, 500)
    draw_tree(900, 300)
    draw_tree(750, 70)
    draw_tree(920,750)

    draw_bear(50,200)
    draw_bear(80,-90)
    draw_bear(720,-110)

    # Finish and run
    arcade.finish_render()
    arcade.run()


main()