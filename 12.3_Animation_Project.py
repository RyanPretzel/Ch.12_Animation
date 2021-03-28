'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.

'''


import arcade

screen_height = 600
screen_width = 600
window_title = "elevator"


class Door:
    def __init__(self, x, y, width, height, speed, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color

    def draw_door(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color)

    def update_door(self):
        self.x -= self.speed


class Render(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)

        self.door_list = []
        for i in range(2):
            if i % 2 == 0:
                self.door_list.append(Door(230, 280, 140, 310, 2, arcade.color.RED))
            else:
                self.door_list.append(Door(370, 280, 140, 310, -2, arcade.color.RED))

    def on_draw(self):
        arcade.start_render()
        for i in range(len(self.door_list)):
            self.door_list[i].draw_door()

        # arcade.draw_rectangle_filled(300, 525, 600, 150, arcade.color.ASH_GREY)
        arcade.draw_rectangle_filled(70, 280, 140, 340, arcade.color.WHITE)
        arcade.draw_rectangle_filled(530, 280, 140, 340, arcade.color.WHITE)

    def on_update(self, delta_time: float):
        for i in range(len(self.door_list)):
            self.door_list[i].update_door()


def main():
    window = Render(screen_width, screen_height, window_title)
    arcade.run()


if __name__ == "__main__":
    main()

