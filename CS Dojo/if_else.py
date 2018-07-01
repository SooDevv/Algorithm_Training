name = input("What's your name : ")
height_m = int(input("Write your height : "))
weight_kg = int(input("Write your weight : "))

bmi = weight_kg / (height_m ** 2)
if bmi < 25:
    print("%s, you are not overweight" % name)
else:
    print("WARNING %s, you are overweight" % name)