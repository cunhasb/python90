class Car:
    def __init__(self, brand):
        self.brand = brand

    def get_brand(self):
        print(self.brand)

    def open_door(self, door_number):
        print ("Opening door: %s" % str(door_number))
