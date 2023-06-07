#!/usr/bin/env python3

# print("Enter two numbers: ")
# x = int(input("Enter the value for x: "))
# y = int(input("Enter the value for y: "))
import math
def area_calculate(x, y):
    print("The area is : ")
    return (x*y)
#circle area calculate 

def circle(x):
    return math.pi*(x**2)

def donut(outside_radius, inside_radius):
    return circle(outside_radius)- circle(inside_radius)
def triangle(base, height):
    return base*height/2

# print(area_calculate(x,y))
# print(area_triangle(base, height))
