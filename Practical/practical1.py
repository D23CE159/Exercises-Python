# Practical 1 - Write a python program to calculate simple interest
principle = float(input("Enter the principle number: "))
interest_time = int(input("Enter the interest time: "))
interest_rate = float(input("Enter the interest rate: "))

simple_interest = (principle * interest_time * interest_rate) / 100
print("The simple interest : ",simple_interest)