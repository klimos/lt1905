"""
Exercise 2.2 Strings and if.
Ex2_2_EndPoint.py
"""

# Part A
plane1 = 'Boeing767 6670'
plane2 = 'CRJ        950'

plane1_type = plane1[:9]
plane2_type = plane2[:3]

plane1_miles = plane1[10:]
plane2_miles = plane2[11:]

print("plane1's type is", plane1_type, 'it flies', plane1_miles, 'miles')
print("plane2's type is", plane2_type, 'it flies', plane2_miles, 'miles')

total_type = plane1_type + plane2_type
print('The concatenation of all plane types is', total_type)

total_miles = int(plane1_miles) + int(plane2_miles)
print('The total miles from all planes is', total_miles)

# Part B
plane1 = 'Boeing767,6670'
plane2 = 'CRJ,950'

comma = plane1.find(',')
plane1_type = plane1[:comma]
plane1_miles = plane1[comma + 1:]

comma = plane2.find(',')
plane2_type = plane2[:comma]
plane2_miles = plane2[comma + 1:]

print("plane1's type is", plane1_type, 'it flies', plane1_miles)
print("plane2's type is", plane2_type, 'it flies', plane2_miles)

# Part C

print('The all uppercase plane type is')
if plane1_type.isupper():
    print(plane1_type)

if plane2_type.isupper():
    print(plane2_type)

# Part D

print()
print()

airport1 = "HNL,Honolulu"
airport2 = "LHR,London/Heathrow"
airport3 = "ARN,Stockholm/Arlanda"
airport4 = "HKG,Hong Kong"
airport5 = "GCM,Grand Cayman BWI"
