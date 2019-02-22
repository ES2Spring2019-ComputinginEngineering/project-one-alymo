import microbit

fout = open("pendulum_data.txt", "w+")


fout.write(time + "\t" + accleration + "\n")