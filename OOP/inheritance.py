class Robot:

    def __init__(self, name, version):
        self.name = name
        self.version = version

    def move_forward(self):
        print(f'{self.name} is moving forward!')

    def move_backward(self):
        print(f'{self.name} is moving backward!')

    def move_right(self):
        print(f'{self.name} is moving right!')

    def move_left(self):
        print(f'{self.name} is moving left!')


# delight class, subclass, child class
class HouseBot(Robot):
    def __init__(self, name, version, area_covered):
        super().__init__(name, version)
        self.area_covered = area_covered

    # new method
    def clean(self):
        if self.area_covered > 0:
            print(f'{self.name} is cleaning the house!')
            self.area_covered -= 30

            if self.area_covered < 0:
                self.area_covered = 0

        else:
            print('CANNOT CLEAN! PLEASE RESET THE AREA COVERED PERIMETER')

    def set_cover_area(self, area):
        if self.area_covered == 0:
            self.area_covered = area

        else:
            print('I can still clean more area!')

    @staticmethod
    def halt():
        print('I am halting.')

    # Overriding the forward method
    def move_forward(self):
        print('This is in house bot class!')
        super().move_forward()


hBot = HouseBot('hBot', 1.1, 50)
print(hBot.name)
print(hBot.version)
hBot.move_forward()
hBot.move_right()
hBot.clean()
hBot.clean()
hBot.clean()
print(hBot.area_covered)
hBot.set_cover_area(50)
hBot.clean()