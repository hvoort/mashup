

left_engine = 17
right_engine = 21


class Engine():

    def __init__(self, gpio_pin, clockwise=True):
        self.gpio_pin = gpio_pin
        self.clockwise = clockwise
        # TODO get speed
        self.speed = 0

    def set_engine(self):
        # TODO calc and set angle
        print "set engine"

    def change_speed(self, increase):
        new_speed = self.speed + increase
        if new_speed > 0:
            self.speed = min(new_speed, 100)
        elif new_speed < 0:
            self.speed = max(new_speed, -100)
        else:
            self.speed = 0

    def forward(self):
        self.change_speed(10)
        self.set_engine()

    def reverse(self):
        self.change_speed(-10)
        self.set_engine()






def forward(speed=20):
    set

