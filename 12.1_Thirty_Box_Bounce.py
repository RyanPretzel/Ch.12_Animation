'''
30 BOX BOUNCE PROGRAM
--------------------
You will want to incorporate lists to modify the
Ball Bounce Program to create the following:

1.) Screen size 600 x 600
2.) Draw four 30px wide side rails on all four sides of the window
3.) Make each side rail a different color.
4.) Draw 30 black boxes(squares) of random size from 10-50 pixels
5.) Animate them starting at random speeds from -300 to +300 pixels/second. 
6.) All boxes must be moving.
7.) Start all boxes in random positions between the rails.
8.) Bounce boxes off of the side rails when the box edge hits the side rail.
9.) When the box bounces change its color to the rail it just hit.
10.)Title the window 30 Boxes

Helpful Hints:
1.) When you initialize the MyGame class create an empty list called self.boxlist=[] to hold all of your boxes.
2.) Then use a for i in range(30): list to instantiate boxes and append them to the list.
3.) In the on_draw section use: for box in self.boxlist: box.draw_box()
4.) Also in the on_draw section draw the side rails.
5.) In the on_update section use: for box in self.boxlist: box.update_box()
'''

import arcade
import random

screen_height = 600
screen_width = 600


class Box:
    def __init__(self, x, y, side, speed_x, speed_y):
        self.x = x
        self.y = y
        self.wx = side
        self.wy = side
        self.color = arcade.color.BLACK
        self.speed_x = speed_x
        self.speed_y = speed_y
        if self.speed_x == 0:
            self.speed_x = 1
        elif self.speed_y == 0:
            self.speed_y = 1

    def box_draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.wx, self.wy, self.color)  # draw each box
        # draw the walls
        arcade.draw_rectangle_filled(15, screen_height / 2, 30, screen_height - 60, arcade.color.BLUE)
        arcade.draw_rectangle_filled(screen_width / 2, 15, screen_width - 60, 30, arcade.color.LIME_GREEN)
        arcade.draw_rectangle_filled(screen_width - 15, screen_height / 2, 30, screen_height - 60, arcade.color.YELLOW)
        arcade.draw_rectangle_filled(screen_width / 2, screen_height - 15, screen_width - 60, 30, arcade.color.RED)

    def update_box(self):
        self.x += self.speed_x
        self.y += self.speed_y
        # check if the thing is colliding with something
        if self.x - (0.5 * self.wx) <= 30:  # collide with left wall
            if self.speed_x < 0:
                self.speed_x *= -1
            self.color = arcade.color.BLUE
        elif self.x + (0.5 * self.wx) >= screen_width - 30:     # collide with right wall
            if self.speed_x > 0:
                self.speed_x *= -1
            self.color = arcade.color.YELLOW
        elif self.y - (0.5 * self.wy) <= 30:    # collide with bottom wall
            if self.speed_y < 0:
                self.speed_y *= -1
            self.color = arcade.color.LIME_GREEN
        elif self.y + (0.5 * self.wy) >= screen_height - 30:        # collide with top wall
            if self.speed_y > 0:
                self.speed_y *= -1
            self.color = arcade.color.RED


class Render(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)

        self.box_list = []      # define the box list and add the boxes inside of the list
        for i in range(30):
            self.box_list.append(Box(random.randint(100, 500), random.randint(100, 500), random.randint(10, 50),
                                     random.randint(-10, 10), random.randint(-10, 10)))
        # self.box_1 = Box(100, 200, 25, 2, 2)

    def on_draw(self):
        arcade.start_render()
        for i in range(len(self.box_list)):     # for every box in the list
            self.box_list[i].box_draw()         # draw each box

    def on_update(self, delta_time: float):
        for i in range(len(self.box_list)):     # for every box in the list
            self.box_list[i].update_box()       # update each box


def main():
    window = Render(screen_height, screen_width, '30 Boxes')
    arcade.run()


if __name__ == '__main__':
    main()
