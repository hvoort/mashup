
from time import sleep

all_lights = range(0, 25)

left_lights = []
right_lights = []

front_lights = []
rear_lights = []
reverse_lights = []

def set_light(i, color):
    print "Set light #{} to color {}".format(i, color)

def set_lights(i_list, color):
    for light in i_list:
        set_light(light, color)

def blink(lights = [], wait_time=0.5, loops=3):
    for i in range(0, loops):
        set_lights(lights, colors.DarkOrange)
        # TODO BLEEP
        # TODO CLick
        sleep(wait_time)
        set_lights(lights, colors.Black)
        sleep(wait_time)


def left_blink():
    blink(left_lights)

def right_blink():
    blink(right_lights)

def open_car():
    blink(left_lights + right_lights, 0.2, 2)

def close_car():
    open_car()

def start_engine():
    # TODO Motor
    set_lights(front_lights, colors.LightBlue)
    set_lights(rear_lights, colors.Red)

def stop_engine():
    set_lights(all_lights, colors.Black)

def reverse():
    set_lights(reverse_lights, colors.White)

def non_reverse():
    set_lights(reverse_lights, colors.Black)

def horn():
    # TODO horn