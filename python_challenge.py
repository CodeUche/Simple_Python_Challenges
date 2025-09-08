import math
from math import *

# --------------------------Challenge 1------------------------------------------------

# Create a multiplication table for any number and ensure the next one starts on a new line.
# This demonstrates the possibilities with for loop iterations

# Prompt user to choose a number
number = int(input("Enter a number to see its multiplication table: "))

for i in range(1, 13):
    # Inner loop iterates through columns (other factors)
    total = number * i
    print(f"{number} x {i} = {total}", end=" ")  # Print with tabs for better formatting
    print()  # Move to a new line after each rows


# --------------------------Challenge 2------------------------------------------------
# Create 2 classes a parent and child class, have the child class inherit Parent class attributes
# To display how inheritance works


class Parent:
    def __init__(self, fname, mname, lname):
        self.fname = fname
        self.lname = lname
        self.mname = mname


class Child(Parent):

    def __init__(self, *args, **kwargs):
        # Stores first 3 args in the Parent(fname, mname, lname)
        super().__init__(*args[:3])

        self.level = kwargs.get("level")
        self.occupation = kwargs.get("occupation")

    def child_details(self, **kwargs):
        print(f"student details are as follows: ")
        details = {
            "First name": self.fname,
            "Middle name": self.mname,
            "Last name": self.lname,
            "Level": self.level,
            "Occupation": self.occupation,
        }

        # Print students in a loop to avoid repetition
        for key, value in details.items():
            print(f"{key}: {value}")


# Use the Child class to create an object, and then execute the child_details method:

child_x = Child(
    "Uche", "Ihuoma", "Eze", level="Masters", occupation="Software Engineer"
)
child_x.child_details()


# --------------------------QUESTION 3-----------------------------------------------------------------------------------------
# Calculate and print the area of a circle with a radius of 5 units. You can be as accurate as you like with the value of pi.
# ------------------------------------------------------------------------------------------------------------------------------
radius = 5
area = pi * radius**2
print(f"The area of a circle is: {area}")


# --------------------------QUESTION 4------------------------------------------
# Write a Python program to sum all the items in a list.
# ------------------------------------------------------------------------------------
list_1 = [2, 3, 6, 8, 9, 6, 8]
summary = 0
for i in list_1:
    summary += i
print(summary)


# --------------QUESTION 5------------------
# Write a Python program that calculates and displays the union of two sets. Set A and Set B are provided as input,
# and the program should find the union of these two sets.
# ------------------------------------------

set_01 = {23, 4, 56, 91, 42, 33, 29}
set_02 = {45, 56, 34, 33, 91, 22, 90}

print(f"Union of Set A and Set B: {set_01.union(set_02)}")


# Another way to achieve this is

print(f"Union of Set A and Set B: {set_01 | set_02}")


# --------------------------------QUESTION 6------------------------------------------
# Write an example for different Python data types such as
# Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
# ------------------------------------------------------------------------------------

num1 = 55
float_1 = 55.0
tuple_1 = (
    "Male",
    "Female",
)
complex_1 = 5 + 7j
list_001 = [23, 45, 55, 77]
set_A = {"boys", "girls", "toddlers", "teenagers"}
dictionary = {"name": "Uche", "age": "32"}

print(type(num1))
print(type(float_1))
print(type(tuple_1))
print(type(complex_1))
print(type(list_001))
print(type(set_A))
print(type(dictionary))


# --------------------------------QUESTION 7------------------------------------------
# Find an Euclidian distance between (2, 3) and (10, 8)
# ------------------------------------------------------------------------------------

point_x = (2, 3)
point_y = (10, 8)

distance = math.dist(point_x, point_y)
print(f"The distance between them is: {distance}")


# --------------------------------QUESTION 8------------------------------------------
# If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace
# (time per mile in minutes and seconds)? What is your average speed in miles per hour?
# ------------------------------------------------------------------------------------

# Given values
distance_km = 10

# convert distance from km to miles
distance_miles = 10 * 0.621371

# convert time to minutes
time_in_minutes = 42 + 42 / 60

# Average pace per mile
average_pace = time_in_minutes / distance_miles

# Average speed in miles per hour(mph)
average_speed = distance_miles / (time_in_minutes / 60)

# convert average pace to minutes and seconds
pace_minutes = int(average_pace)
pace_seconds = (average_pace - pace_minutes) * 60


# Print result in minutes, seconds and miles per hour
print(f"Average pace is: {pace_minutes} minutes and {int(pace_seconds)} seconds per mile")
print(f"Average speed is: {average_speed:.2f} mph")
