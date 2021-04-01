'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.

'''
# next goal: change the door timer to track the floor level
# Elevator class should not be necessary

import arcade
import random


screen_height = 600
screen_width = 600
window_title = "elevator"


class Door:
    def __init__(self, x, y, width, height, speed, color, timer):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.timer = timer

    def draw_door(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color)

    def update_door(self):
        self.x -= self.speed


class Fly:
    def __init__(self, x, y, speed, size):
        self.x = x
        self.y = y
        self.speed = speed
        self.size = size

    def draw_fly(self):
        arcade.draw_circle_filled(self.x, self.y, self.size, arcade.color.BLACK)

    def update_fly(self):
        self.x += self.speed
        self.y += random.randint(-2, 2)


class Render(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.TAN)

        self.door_list = []
        for i in range(2):                                              # create the doors
            if i % 2 == 0:
                self.door_list.append(Door(220, 280, 160, 320, 2, arcade.color.BROWN, 100))
            else:
                self.door_list.append(Door(380, 280, 160, 320, -2, arcade.color.BROWN, 100))

        self.fly_list = []                                              # create the list for the flies

    def on_draw(self):
        arcade.start_render()
        for i in range(len(self.door_list)):        # draw doors
            self.door_list[i].draw_door()

        arcade.draw_rectangle_filled(300, 525, 600, 150, arcade.color.WHITE)
        arcade.draw_rectangle_filled(70, 280, 140, 340, arcade.color.WHITE)
        arcade.draw_rectangle_filled(530, 280, 140, 340, arcade.color.WHITE)
        arcade.draw_rectangle_filled(300, 60, 600, 120, arcade.color.ASH_GREY)

        arcade.draw_rectangle_filled(300, 450, 340, 20, arcade.color.BATTLESHIP_GREY)
        arcade.draw_rectangle_filled(140, 280, 20, 340, arcade.color.BATTLESHIP_GREY)
        arcade.draw_rectangle_filled(460, 280, 20, 340, arcade.color.BATTLESHIP_GREY)

        for i in range(len(self.fly_list)):         # draw flies
            self.fly_list[i].draw_fly()

    def on_update(self, delta_time: float):
        for i in range(len(self.door_list)):
            if self.door_list[i].speed == 0:        # if the door is stopped then start the timer
                self.door_list[i].timer -= 1

            if self.door_list[i].timer == 0:
                if self.door_list[i].x == 90:       # if the timer is finished then start the door again
                    self.door_list[i].speed = -2    # depending on the position, the door must go in the right direction
                elif self.door_list[i].x == 220:
                    self.door_list[i].speed = 2
                elif self.door_list[i].x == 380:
                    self.door_list[i].speed = -2
                else:
                    self.door_list[i].speed = 2
                self.door_list[i].timer = 200       # after the speed is set, set the timer again

            elif (self.door_list[i].x == 90 and self.door_list[i].speed == 2) or \
                    (self.door_list[i].x == 510 and self.door_list[i].speed == -2) or \
                    (self.door_list[i].x == 380 and self.door_list[i].speed == 2) or \
                    (self.door_list[i].x == 220 and self.door_list[i].speed == -2):
                self.door_list[i].speed = 0         # if the door is in the right position then stop the door

            self.door_list[i].update_door()  # once the speed, timer, and position is right, then update the door

        if self.door_list[0].x == 90 and self.door_list[0].speed != 0:  # when the door opens, make a fly fly out
            self.fly_list.append(Fly(173, 300, random.randint(2, 5), random.randint(3, 8)))

        for i in range(len(self.fly_list)):
            if self.fly_list[i].y >= 620:       # if the fly flies off of the screen then remove it
                self.fly_list.remove(self.fly_list[i])
            self.fly_list[i].update_fly()


def main():
    window = Render(screen_width, screen_height, window_title)
    arcade.run()


if __name__ == "__main__":
    main()

