# Micro:bit Pendulum Period Modeling
  These set of programs allow a user to collect angular position and acceleration data using a micro:bit attached to the bob of pendulum to model the motion of pendulums of different lengths. Angular position over time as well as angular acceleration over time will be plotted for each length. The period will also be generated for each length. The length of the pendulum can be graphed by the period on a log-log graph, and a relationship will be observed between length and period of a pendulum. This can be compared to a simulation program, which will simulate the motion of pendulum with given length values and calculate a period. These values can also be graphed on a log-log graph, and the graph of the simulated values can be compared to the real-world data to determine how well the pendulum model's an ideal pendulum.

## Instructions

1. Collect Real-World Data:
  Construct a pendulum and attach a micro:bit to the end. Flash the "1_microbit_data_collection.py" code to the microbit, disconnect the microbit, and push the reset button. Start the pendulum at a 90 degree angle. Pushing A will start the time and acceleration collection and B will stop data collection. After each trial (using a pendulum of a unique length), attach the microbit back to the computer and drag the file it has created on to the computer. Repeat five files times, each time saving the file with the length of the pendulum used. 

2. Collect Simulation Data: 

**Please refer to the piece of code used for each step and how to use it!
**Dont forget special things the user must input to the code (do they need to change the file name, or input a new value into a variable, etc)

3. Graph Real-World and Simulation Position and Acceleration Data: MO :)

4. Plot Pendulum Period and Length:
  To observe the relationship between a pendulum's length and its period, graph log(pendulum length) by log(pendulum period) using the "3_plotting_period_and_length.py" file. Input the various lengths of the pendulums used in each trial into the list called Length_of_Pendulum, and input the various periods that correspond to each length into the list called Period_of_Pendulum. When the program is run, it will generate a graph of log(pendulum length) by log(pendulum period), which will show the direct or indirect relationship between length and period of a pendulum. You must input values for the real-world data into the list and run the code to get the first graph, and then input the simulation data over the old data into the same list and run it again. Looking at both these graphs will emonstrate the difference between real-world pendulum length and period data and simulated pendulum length and period data.


## How to format your readme

In your readme, you can:
```
Give code examples
```

You can also include useful links, like this one with information about [formatting markdown](https://help.github.com/en/articles/basic-writing-and-formatting-syntax)

You can
- Also
- Make
- Lists
