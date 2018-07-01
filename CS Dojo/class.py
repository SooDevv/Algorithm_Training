class Robot():
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def introduce(self):
        print("Hi, My name is %s" % self.name)

class  Person():
    def __init__(self, n, p, i):
        self.name = n
        self.personality = p
        self.is_sitting = i

    def sit_down(self):
        self.is_sitting = True

    def stand_up(self):
        self.is_sitting = False

r1 = Robot("kakaoBot", "Yellow", 3)
r2 = Robot("gooBot", "Blue", 2)

p1 = Person("Soo", "passionative", False)
p2 = Person("Kang", "happy", True)

p1.robot_owned = r2

print("p1 bot, What's your name?")
p1.robot_owned.introduce()