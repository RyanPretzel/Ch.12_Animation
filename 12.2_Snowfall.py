'''
SNOWFALL
--------
Try to create the snowfall animation by meeting
the following requirements:

1.) Create a 600 x 600 window with black background
2.) Window title equals "Snowfall"
3.) Crossbars 10 px wide. Snow must be outside!
4.) Make snowflake radius random between 1-3
5.) Randomly start snowflakes anywhere in the window.
6.) Random downward speed of -4 to -1
7.) Start snowflakes again at random x from 0-600 and random y from 600-700
8.) Generate 300 snowflakes
9.) Color snowflake #1 red just for fun.
10.) All other snowflakes should be white.


'''

import arcade
import random

screen_height = 600
screen_width = 600
window_title = "Snowfall"


class Snowflake:
    def __init__(self, x, y, radius, speed, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.color = color

    def draw_snowflake(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, self.color)

    def update_snowflake(self):
        self.y -= self.speed


class Render(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)

        self.snowflake_list = []
        for i in range(300):        # generate all of the snowflakes
            if i == 0:      # make the first one red
                self.snowflake_list.append(Snowflake(random.randint(0, 600), random.randint(0, 600),
                                                     random.randint(1, 3), random.randint(1, 4), arcade.color.RED))
            else:           # the rest get to be white
                self.snowflake_list.append(Snowflake(random.randint(0, 600), random.randint(0, 600),
                                                     random.randint(1, 3), random.randint(1, 4), arcade.color.WHITE))

    def on_draw(self):
        arcade.start_render()
        for i in range(len(self.snowflake_list)):
            self.snowflake_list[i].draw_snowflake()

        arcade.draw_rectangle_filled(300, 300, 600, 15, arcade.color.ASH_GREY)
        arcade.draw_rectangle_filled(300, 300, 15, 600, arcade.color.ASH_GREY)

    def on_update(self, delta_time: float):
        for i in range(len(self.snowflake_list)):
            if self.snowflake_list[i].y <= 0:       # if the snowflake hits the bottom of the screen
                self.snowflake_list.remove(self.snowflake_list[i])      # remove and replace the snowflake
                self.snowflake_list.append(Snowflake(random.randint(0, 600), random.randint(600, 700),
                                                     random.randint(1, 3), random.randint(1, 4), arcade.color.WHITE))

            self.snowflake_list[i].update_snowflake()  # otherwise just update the snowflake


def main():
    window = Render(screen_width, screen_height, window_title)
    arcade.run()


if __name__ == "__main__":
    main()
