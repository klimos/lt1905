"""
Exercise 5.1 Classes and Initialization
Ex5_1.py
"""

# Classes definition
class Trip:

    cariblist = ['GCM', 'CUR']
    hawaiilist = ['ITO', 'HNL']

    def __init__(self, departcity=None, arrivecity=None,
                 departdaytime=None, arrivedaytime=None):
        self.departcity = departcity
        self.arrivecity = arrivecity
        self.departdaytime = departdaytime
        self.arrivedaytime = arrivedaytime

    def is_round_trip(self):
        return self.departcity == self.arrivecity

    def is_hawaiian(self):
        return self.arrivecity in Trip.hawaiilist

    def is_caribbean(self):
        return self.arrivecity in Trip.cariblist

    def is_interisland(self):
        return self.departcity in Trip.hawaiilist and self.arrivecity in Trip.hawaiilist


class Aircraft:
    def __init__(self, code=None, name=None):
        self.code = code
        self.name = name


class Airport:
    def __init__(self, citycode=None, city=None):
        self.citycode = citycode
        self.city = city


#Part A
# Sample data for Trip
depcity = 'CUR'
arrcity = 'HNL'
depdt = '2022-01-03 09:00'
arrdt = '2022-01-03 16:00'
mytrip = Trip(departcity=depcity,
              arrivecity=arrcity,
              departdaytime=depdt,
              arrivedaytime=arrdt)

print("\nPart A\n" + '-' * 6)
print("My Trip is departing from '{0}' on {1} and arrives to '{2}' on {3}.".format(
    mytrip.departcity, mytrip.departdaytime, mytrip.arrivecity, mytrip.arrivedaytime))

print("Caribbean destinations:", Trip.cariblist)
print("Hawaii destinations:", Trip.hawaiilist)

print('-' * 6)
ans = 'is' if mytrip.is_round_trip() else 'is not'
print("The trip from", mytrip.departcity, "to", mytrip.arrivecity, ans, "a round trip.")


# Part B
# Create list of Trip objects, pass list as positional args to constructor
alltrips = [Trip(*['HNL', 'HKG', '2022-01-03 16:00', '2022-01-03 20:00']),
Trip(*['HNL', 'HNL', '2022-01-03 08:30', '2022-01-03 15:40']),
Trip(*['HKG', 'CDG', '2022-01-03 19:20', '2022-01-04 12:35']),
Trip(*['HKG', 'GCM', '2022-01-03 16:50', '2022-01-04 09:30']),
Trip(*['HNL', 'ITO', '2022-01-03 12:00', '2022-01-03 13:55'])]


def print_trip(trp):
    print('Trip from', trp.departcity, 'to', trp.arrivecity,
            'Departs at', trp.departdaytime,
            'and arrives at', trp.arrivedaytime)


print("\nPart B\n" + '-' * 6)
for trip in alltrips:
    print_trip(trip)
    if trip.is_round_trip():
        print("\tis a round trip")
    if trip.is_caribbean():
        print("\tis Caribbran")
    if trip.is_hawaiian():
        print("\tis Hawaiian")
    if trip.is_interisland():
        print("\tis an interisland trip")


# Part C
# Sample Data for Aircraft
code = 1
name = "Canadian Regional Jet"
myplane = Aircraft(code, name)
print("\nPart C\n" + '-' * 6)
print(f"My aircraft is {myplane.name} and has code '{myplane.code}'.")

# Sample Data for Airport
citycode = 'HNL'
city = "Honolulu"
myairport = Airport(citycode, city)
print(f"Airport in {myairport.city} has code '{myairport.citycode}'.")
