import random

for i in range(0,10):
    temperature=random.randrange(50)
    humidity=random.randrange(20,80)
    print(temperature,"C")
    if temperature <27:
        print("Alarm = High")
    else:
        print("Alarm = Low")
    print(humidity,"%")
    print("**************************")
