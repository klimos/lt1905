"""
Exercise 3.1 Collections and Slicing
Ex3_1.py
"""

# Part A
codelist = ['HNL', 'ITO', 'LHR', 'LGA', 'GCM', 'MSY', 'LAX']
flightlist = ['HNL', 'HKG', '2022-01-03 16:00', '2022-01-03 20:00', 99.95, 4]

# departcity = flightlist[0]
# arrivecity = flightlist[1]
# departdaytime = flightlist[2]
# arrivedaytime = flightlist[3]
# cost = flightlist[4]
# code = flightlist[5]

print("\nPart A\n" + '-' * 6)
print(codelist[0])
print(codelist[1])
print(codelist[-2])
print(codelist[-1])

departcity, arrivecity, departdaytime, arrivedaytime, cost, code = flightlist
print("Departure from:", departcity, "at:", departdaytime)
print("Arrival to:", arrivecity, "at:", arrivedaytime)


# Part B
print("\nPart B\n" + '-' * 6)
print("Original list:", codelist)
codelist.reverse()
print("Reversed list:", codelist)
codelist.sort()
print("Sorted list:", codelist)


# Part C
print("\nPart C\n" + '-' * 6)
aptlist = codelist
aptlist.pop()
print("Shared list references:")
print("aptlist:", aptlist)
print("codelist:", codelist)
if aptlist is codelist:
    print("List aptlist and codelist are shared.")
else:
    print("List aptlist and codelist are not shared.")
print("-" * 6)

print("Copied lists:")
aptlist = list(codelist)
aptlist.pop()
print("aptlist:", aptlist)
print("codelist:", codelist)
if aptlist is codelist:
    print("List aptlist and codelist are shared.")
else:
    print("List aptlist and codelist are not shared.")
print("-" * 6)

print("Sliced copy:")
aptlist = codelist[:]
print("aptlist:", aptlist)
print("codelist:", codelist)
print("aptlist and codelist equal?", aptlist == codelist)
print("aptlist and codelist same?", aptlist is codelist)


# Part D
print("\nPart D\n" + '-' * 6)
print("Adding elements:")
codelist.insert(0, 'ABC')
codelist.append('XYZ')
print(codelist)
print("-" * 6)

print("Tuples:")
codetuple = tuple(codelist)
print(codetuple)
print("List and tuple lengths equal?", len(codelist) == len(codetuple))
print("List and tuple the same?", codelist == codetuple)
print("-" * 6)

print("Reverse sorting of a tuple:")
codetuple = tuple(sorted(codetuple, reverse=True))
print(codetuple)
