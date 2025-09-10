import math
from math import *
from datetime import datetime, timedelta


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
print(
    f"Average pace is: {pace_minutes} minutes and {int(pace_seconds)} seconds per mile"
)
print(f"Average speed is: {average_speed:.2f} mph")


# --------------------------------QUESTION 9------------------------------------------
# The volume of a sphere with radius r is 4/3 πr^3.
# What is the volume of a sphere with radius 5?
# ------------------------------------------------------------------------------------

radius = 5
sphere = (4 / 3) * pi * (radius**3)

print(f"The Volume of the sphere is: {sphere}")

# Alternatively
sphere_alt = (4 / 3) * math.pi * (radius**3)
print(f"The Volume of the sphere is: {sphere_alt}")


# --------------------------------QUESTION 10------------------------------------------
# Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
# Shipping costs $3 for the first copy and 75 cents for each additional copy.
# What is the total wholesale cost for 60 copies?
# -------------------------------------------------------------------------------------

book_price = 24.95
bookstore_discount = 0.40
shipping_first = 3
shipping_additional = 0.75
total_books_ordered = 60

cost_per_book_after_discount = book_price * (1 - bookstore_discount)
total_shipping_cost = shipping_first + shipping_additional * (total_books_ordered - 1)
total_book_cost = total_books_ordered * cost_per_book_after_discount
total_wholesale_cost = total_book_cost + total_shipping_cost

print(f"Cost per book after discount: {cost_per_book_after_discount:.2f}")
print(f"Total shipping cost is: {total_shipping_cost}")
print(f"Total wholesale cost for 60 books is: ${total_wholesale_cost:.2f}")



# --------------------------------QUESTION 11------------------------------------------
# Write a program to prompt the user for hours and rate per hours to compute gross pay.
# you need to take into account the result which must be in 2 decimal places.
# -------------------------------------------------------------------------------------

# Lets us thhe try/except condiditional statement to fix this

try:
    hours_worked = int(input("How many hours did you work: "))
    rate_per_hour = float(input("Enter your hourly rate: "))
    gross_pay = hours_worked * rate_per_hour
    print(f"Your gross payment is: {gross_pay}")

except ValueError:
    print("Enter a valid integer")



# --------------------------------QUESTION 12------------------------------------------
# write a program that converts temperature from Celsius to Fahrenhiet.
# Using users information.
# -------------------------------------------------------------------------------------

# Create a function for this conversion
def convert_to_fahrenheit(celsius):
    # celsius = input("Enter temperature in celsius: ")
    convert_celsius = 9/5 * (celsius + 32)
    print(f"{celsius} degrees Celsius = {convert_celsius} Fahrenheit.")

convert_to_fahrenheit(32)
convert_to_fahrenheit(35)



# --------------------------------QUESTION 13------------------------------------------
# How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
# -------------------------------------------------------------------------------------

# Assign variables
kilometers = 10
kilometers_in_mile = 1.61
miles = kilometers / kilometers_in_mile

print(f"There are {miles} miles in a kilometer")


# Alternatively
# This is my choice of solution because of its flexibility and scalability


def miles_in_km(kilometer):
    km_in_mile = 1.61
    miles = kilometer / km_in_mile
    print(f"There are {miles} miles in a kilometer")


# Call the function and pass an argument
miles_in_km(10)



# --------------------------------QUESTION 14------------------------------------------
# How many seconds are there in 42 minutes 42 seconds?
# -------------------------------------------------------------------------------------


# Functions are a girl's best friend
# Create a function and pass the number of minutes as an argument
def convert_secs_to_mins(minutes):

    seconds_per_minute = 60
    total_seconds = minutes * seconds_per_minute
    print(f"The total numner of time is {total_seconds} seceonds")


# 42 minutes and 42 seconds is 42.7 in decimals.
# That is 42/60 = 0.7
# 42.7 ;-)
convert_secs_to_mins(42.7)



# --------------------------------QUESTION 15------------------------------------------
#  Write a program which calculate trip cost for a user.
#       * create a greeting for your program.
#       * Ask the user for number of days.
#       * Ask user for hotel price.
#       * Ask the user for rental car price.
#       * Ask for other expenses
#       * combine all expenses and print with 2 digits after decimal 2 places.
# -------------------------------------------------------------------------------------


# This is the most straight forward and literally the easiest way I know
# Define a function
def trip_budget(*args):
    print(f"Hello customer! Welcome to your cost calculator.")

    duration = int(input("How many days will you be staying: "))
    hotel = int(input("How much does the hotel cost per night: "))
    flight = int(input("How does your flight cost: "))
    rental_car = int(
        input("If you need a rental car, please enter the price else enter 0: ")
    )
    total_cost = float(hotel * duration) + (flight + rental_car)
    print(f"Your total cost is: ${total_cost:.2f}")


trip_budget()


# Alternatively you could create a class and method.
# The task can be achieved both ways.


class TripCalculator:
    def __init__(self):
        pass

    # Define a function that can be called at any time to prevent repetitions
    def trip_estimate(self, *args):

        # Print welcome message
        print(f"Hello customer! Welcome to your cost calculator.")

        duration = int(input("How many days will you be staying: "))
        hotel = int(input("How much does the hotel cost per night: "))
        flight = int(input("How does your flight cost: "))
        rental_car = int(
            input("If you need a rental car, please enter the price else enter 0: ")
        )
        total_cost = hotel * duration + (flight + rental_car)
        return f"Your total cost is: ${total_cost:.2f}"


trip_cost = TripCalculator()
message = trip_cost.trip_estimate()
print(message)
