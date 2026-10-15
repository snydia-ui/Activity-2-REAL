# COMPUTER SCIENCE 2 – HANDS-ON ACTIVITY
# Topic: Python Functions and Modular Programming
# Activity Title: Sum and Difference Calculator
# SEBASTIAN JOAQUIN N YDIA 8 CAMIA 10/15/26

# Program
number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))

# Defining Functions
def calculate_sum():
    global number_1, number_2
    sum = number_1 + number_2 #sum is a local variable
    print("The sum of the two numbers is: ", sum)


def calculate_difference():
    global number_1, number_2
    difference = number_1 - number_2 # difference is a local variable
    print("The difference of the two numbers is: ", difference)

# Program continuation
calculate_sum()
calculate_difference()
