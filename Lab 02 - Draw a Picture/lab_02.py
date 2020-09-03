# This is a program to draw Nature
import arcade
arcade.open_window(600,600, "Dayton's Drawing")

#Setting background color to deep sky blue
arcade.set_background_color(arcade.csscolor.DEEP_SKY_BLUE)

# Start Drawing
arcade.start_render()

# Draw the grass
arcade.draw_lrtb_rectangle_filled(0,598,200,0,arcade.csscolor.DARK_GREEN)

# Draw a Lake
arcade.draw_ellipse_filled(300,90,500,200,arcade.csscolor.DARK_BLUE)

# Draw lake Ripples
arcade.draw_line(150,120,425,120,arcade.csscolor.BLACK)
arcade.draw_line(100,50,175,50,arcade.csscolor.BLACK)
arcade.draw_line(200,30,350,30,arcade.csscolor.BLACK)

# Draw fish
arcade.draw_circle_filled(425,90,7,arcade.csscolor.ORANGE)
arcade.draw_triangle_filled(431,90,436,94,436,86,arcade.csscolor.ORANGE)
arcade.draw_circle_filled(125,125,7,arcade.csscolor.ORANGE)
arcade.draw_triangle_filled(108,120,108,130,118,125,arcade.csscolor.ORANGE)

# Draw sun
arcade.draw_circle_filled(100,400,100,arcade.csscolor.YELLOW)

# Draw mountain 1
arcade.draw_triangle_filled(1,200,100,470,300,200,arcade.csscolor.PURPLE)
# Draw mountain 2
arcade.draw_triangle_filled(200,200,300,550,400,200,arcade.csscolor.PURPLE)
# Draw mountain 3
arcade.draw_triangle_filled(300,200,500,590,599,200,arcade.csscolor.PURPLE)

# Draw Trees
arcade.draw_lrtb_rectangle_filled(75,100,195,180,arcade.csscolor.BROWN)
arcade.draw_triangle_filled(65,195,90,250,110,195,arcade.csscolor.GREEN)
arcade.draw_lrtb_rectangle_filled(500,520,195,180,arcade.csscolor.BROWN)
arcade.draw_triangle_filled(490,195,505,250,530,195,arcade.csscolor.GREEN)

# Finish Drawing
arcade.finish_render()

# Keep Drawing up until someone closes it
arcade.run()
