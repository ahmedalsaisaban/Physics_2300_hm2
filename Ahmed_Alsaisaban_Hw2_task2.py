import numpy as np
import math as m
import matplotlib.pyplot as plt
"""
Ahmed Alsaisaban
1/31/2019
Programming Assignment M2
Task(2)
"""


"""
-the function takes position, velocity, time and acceleration as argument
-the function returns the result of the equation of displacement of projectile
"""
def equation(position,velocity,time,acceleration): 
    return position + velocity*time + 0.5*acceleration*time**2
"""
-the function takes the position, velocity for x and y as user input
-the function fills an array with these values 
-the function returns the array to use
"""
def getInitial():
    #get input & push return array of inputs
    xPosition  = float(input ("x Position:"))
    xVelocity  = float(input ("x Velocity:"))
    yPosition  = float(input ("y Position:"))
    yVelocity  = float(input ("y Velocity:"))
    outPut = [xPosition, xVelocity, yPosition, yVelocity]
    return  outPut
"""
-the function assign the acceleration of x and y 
-the function assign a value to delta and time
-the function restore the values in an array
-the function returns the array to use 
"""
def assignValues():
    #set values and returning them in an array
    x_Acceleration = 0.0
    y_Acceleration = -9.8
    delta =0.1
    time = 0.0
    values = [x_Acceleration, y_Acceleration, delta, time]
    return values
"""
-the function define a holder for x and y to push the graph points to them
-the function assign a value for intervals size
-the function calls the previous tow functions to grab the input and values
-the function loops to run the first function and push values to the holders
-when y reaches zero the loop breaks
-the function plots the points from the holders and display the graph
"""
def display():
    #appending values to x and y arrays and ploting tand showing
    x =[] #x holder to drow points
    y = [] #y holder to drow points
    intervals = 170
    initial = getInitial() #running and Assigning the input function 
    values = assignValues() #running and Assigning the values function 
    for i in range(intervals):
        x.append(equation(initial[0],initial[1],values[3],values[0]))
        y.append(equation(initial[2],initial[3],values[3],values[1])) 
        values[3] = values[3] + values[2] 
        if y[i] < 0.0: #stops when hits the ground 
            break
    plt.plot(x, y)
    plt.show()      
"""
-main function runs display 
"""
def main():
    display()
    
if __name__ == "__main__":
    main()