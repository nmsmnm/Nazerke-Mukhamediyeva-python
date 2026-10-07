# Assignment 1 - Python Basics
# Profile Card Builder

#1:

name = "Nazerke"
age = 22
height = 1.69
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))


#2

user_name = input("What is your name? ")
birth_year = int(input("What year were you born? "))

approx_age = 2026 - birth_year

print(f"Hi, {user_name}! You are approximately {approx_age} years old.")


#3

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

product = number1 * number2

print(f"{number1} × {number2} = {product}")


#4

item_name = "Matcha Latte"
price = 6.50
quantity = 2

total = price * quantity

print("===========================")
print("          RECEIPT")
print("===========================")
print(f"Item:      {item_name}")
print(f"Price:     ${price:.2f}")
print(f"Quantity:  {quantity}")
print("---------------------------")
print(f"Total:     ${total:.2f}")
print("===========================")


#5

profile_name = input("What is your name? ")
hometown = input("What is your hometown? ")
hobby = input("What is your favorite hobby? ")
fun_fact = input("Tell me one fun fact about yourself: ")
profile_birth_year = int(input("What year were you born? "))

profile_age = 2026 - profile_birth_year

print("╔══════════════════════════════╗")
print(f"      PROFILE: {profile_name}")
print("╚══════════════════════════════╝")
print(f"Hometown:   {hometown}")
print(f"Hobby:      {hobby}")
print(f"Fun fact:   {fun_fact}")
print(f"Age:        {profile_age}")
