class Car:
    def __init__(self, brand):
        self.brand = brand

    def get_brand(self):
        print(self.brand)

    def open_door(self, door_number):
        print ("Opening door: %s" % str(door_number))

    def blinker_control(self, left_blinker="Off", right_blinker="Off"):
        self.left_blinker = left_blinker
        self.right_blinker = right_blinker
        print ("L: %s, R: %s" % (self.left_blinker, self.right_blinker))
