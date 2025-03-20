import math

"""
Exercise 2.1 Arithmetic and Numeric Types
Ex2_1.py
"""

print('This is exercise 2.1')

# Part A
num1 = '5'
num2 = '9'
print("\nPart A\n" + '-' * 6)
print("5/9 is:", f"{float(num1) / float(num2):.3f}")

# Part B
paris_temp = '25'
honolulu_temp = '81'
freezing = 32.0
print("\nPart B\n" + '-' * 6)
print("Paris temp in 'C:", f"{float(paris_temp):.0f}")
print("Paris temp in 'F:", f"{float(paris_temp) * 9.0 / 5.0 + freezing:.0f}")
print("Honolulu temp in 'C:", f"{(float(honolulu_temp) - freezing) * 5.0 / 9.0:.0f}")
print("Honolulu temp in 'F:", f"{float(honolulu_temp):.0f}")

# Part C
print("\nPart C\n" + '-' * 6)
price = '199.95'
discount_small = .05
discount_med = .10
discount_big = .15
print("Price with small discount:", f"{float(price) - float(price) * discount_small:.2f}")
print("Price with medium discount:", f"{float(price) - float(price) * discount_med:.2f}")
print("Price with big discount:", f"{float(price) - float(price) * discount_big:.2f}")

# Part D
flight1_dist = 305
flight1_time = 62
flight2_dist = 525
flight2_time = 91
print("\nPart D\n" + '-' * 6)
flight1_mph = flight1_dist / (flight1_time / 60)
print("Flight 1 speed:", f"{flight1_mph:.0f}", "mph;", f"{flight1_mph * 1.6:.0f}", "kph")
flight2_mph = flight2_dist / (flight2_time / 60)
print("Flight 2 speed:", f"{flight2_mph:.0f}", "mph;", f"{flight2_mph * 1.6:.0f}", "kph")
flight_av_mph = (flight1_dist + flight2_dist) / ((flight1_time + flight2_time) / 60)
print("Average flight speed:", f"{flight_av_mph:.0f}", "mph;", f"{flight_av_mph * 1.6:.0f}", "kph")

# Part E
area = 7.5
print("\nPart E\n" + '-' * 6)
print("Radius is:", f"{math.sqrt(area / math.pi):.3f}")
