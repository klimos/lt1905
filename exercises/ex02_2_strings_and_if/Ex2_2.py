"""
Exercise 2.2 Strings and if.
Ex2_2.py
"""

# Part A
plane1 = 'Boeing767 6670'
plane2 = 'CRJ        950'

plane1_type = plane1[:10].strip()
plane1_range = int(plane1[-4:].strip())
plane2_type = plane2[:10].strip()
plane2_range = int(plane2[-4:].strip())

print("\nPart A\n" + '-' * 6)
print("{} has range of {} miles.".format(plane1_type, plane1_range))
print("{} has range of {} miles.".format(plane2_type, plane2_range))
print(f"Concatenation of the two planes is: '{plane1_type + plane2_type}'.")
print(f"The combined range is: {plane1_range + plane2_range} miles.")

# Part B
plane1 = 'Boeing767,6670'
plane2 = 'CRJ,950'

row = plane1.split(",")
print("\nPart B\n" + '-' * 6)
print("{plane} has range of {range} miles.".format(plane=row[0], range=row[1]))

row = plane2.split(",")
print("{plane} has range of {range} miles.".format(plane=row[0], range=row[1]))

# Part C
print("\nPart C\n" + '-' * 6)
if plane1_type.isupper():
    print(plane1_type, "is all uppercase.")
else:
    print(plane1_type, "is not all uppercase.")

if plane2_type.isupper():
    print(plane2_type, "is all uppercase.")
else:
    print(plane2_type, "is not all uppercase.")

if plane1_type[-1].isdigit():
    print(plane1_type, "ends with a digit.")
else:
    print(plane1_type, "does not end with a digit.")

if plane2_type[-1].isdigit():
    print(plane2_type, "ends with a digit.")
else:
    print(plane2_type, "does not end with a digit.")

if plane1_range > plane2_range:
    print(plane1_type, "has gerater range than", plane2_type + ".")
elif plane1_range < plane2_range:
    print(plane2_type, "has greater range than", plane1_type + ".")
else:
    print(plane1_type, "and", plane2_type, "have equal range.")

# Part D
print("\nPart D\n" + '-' * 6)
print("Python is Guido's invention")
print('''They say, "Python is Guido's invention."''')

# Part E
airport1 = "HNL,Honolulu"
airport2 = "LHR,London/Heathrow"
airport3 = "ARN,Stockholm/Arlanda"
airport4 = "HKG,Hong Kong"
airport5 = "GCM,Grand Cayman BWI"

print("\nPart E\n" + '-' * 6)

airport_codes = "\"" + airport1[:airport1.find(',')] + "\"," \
    + "\"" + airport2[:airport2.find(',')] + "\"," \
    + "\"" + airport3[:airport3.find(',')] + "\"," \
    + "\"" + airport4[:airport4.find(',')] + "\"," \
    + "\"" + airport5[:airport5.find(',')] + "\""
airport_codes_list = airport_codes.split(",")
print("List of airports: " + airport_codes_list[0] + ", "
      + airport_codes_list[1] + ", "
      + airport_codes_list[2] + ", "
      + airport_codes_list[3] + ", "
      + airport_codes_list[4])

cities = "\"" + airport1[airport1.find(',')+1:] + "\"," \
    + "\"" + airport2[airport2.find(',')+1:] + "\"," \
    + "\"" + airport3[airport3.find(',')+1:] + "\"," \
    + "\"" + airport4[airport4.find(',')+1:] + "\"," \
    + "\"" + airport5[airport5.find(',')+1:] + "\""
cities_list = cities.split(",")
print("List of cities: " + cities_list[0] + ", "
      + cities_list[1] + ", "
      + cities_list[2] + ", "
      + cities_list[3] + ", "
      + cities_list[4])
