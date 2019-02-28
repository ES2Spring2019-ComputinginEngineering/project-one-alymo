import microbit, math, os, random

#cwd = os.getcwd()

filename = "pendulum_data" + str(random.randint(1,999)) + ".txt"

while not microbit.button_a.is_pressed():
    microbit.sleep(50)

with open(filename, "w") as file:
    start_time = (microbit.running_time())/1000
    while not microbit.button_b.is_pressed():
        acceleration_x = (microbit.accelerometer.get_x())/1000
        acceleration_y = (microbit.accelerometer.get_y())/1000
        microbit.display.show(microbit.Image.HAPPY)
        time = (microbit.running_time())/1000 - start_time
        values = str(acceleration_x) + "," + str(acceleration_y) + "," + str(time) + "\n"
        file.write(values)
        microbit.sleep(50)
        print(values)
file.close()