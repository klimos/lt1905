"""
Exercise 4.1 Creating and Calling Functions
Ex4_1.py
"""

# Data for the exercise
# Please do not modify these dictionaries

# Data description of city_code_dict
#    Airport Code : Airport Name
city_code_dict = {
    'HNL': 'Honolulu',
    'ITO': 'Hilo',
    'LHR': 'London/Heathrow',
    'ARN': 'Stockholm/Arlanda',
    'HKG': 'Hong Kong',
    'YYZ': 'Toronto',
    'CDG': 'Paris/Charles de Gaulle',
    'NRT': 'Tokyo/Narita',
    'GCM': 'Grand Cayman BWI',
    'CUR': 'Curacao Netherland Antilles'}

# Data description of flightdict
# flightnum : [ departcity, arrivecity, departdaytime,
#                arrivedaytime, cost, code ]
flightdict = {
    102: ['HNL', 'HKG', '2022-01-03 16:00', '2022-01-03 20:00', 99.95, 4],
    132: ['HNL', 'HNL', '2022-01-03 08:30', '2022-01-03 15:40', 59.0, 2],
    276: ['HKG', 'CDG', '2022-01-03 19:20', '2022-01-04 12:35', 233.99, 2],
    303: ['HKG', 'ARN', '2022-01-03 16:50', '2022-01-04 13:30', 233.99, 2],
    498: ['NRT', 'ITO', '2022-01-03 12:00', '2022-01-03 20:55', 159.99, 2],
    390: ['CUR', 'CUR', '2022-01-03 09:00', '2022-01-03 16:30', 599.95, 3],
    465: ['NRT', 'YYZ', '2022-01-03 20:15', '2022-01-04 09:45', 59.0, 3],
    1305: ['ITO', 'ARN', '2022-01-03 18:50', '2022-01-04 10:00', 125.0, 2],
    375: ['HKG', 'HNL', '2022-01-03 09:10', '2022-01-03 16:30', 299.99, 4],
    444: ['NRT', 'LHR', '2022-01-03 23:15', '2022-01-04 13:20', 125.0, 3],
    1572: ['HNL', 'HNL', '2022-01-03 09:40', '2022-01-03 16:10', 125.0, 2]}


# Part A
# Function definitions
def list_all_cities():
    print("List of all cities:")
    for key in city_code_dict:
        print(key, '-', city_code_dict[key])


def flights_per_city(city):
    print("Flights from " + city_code_dict[city] + ":")
    for key in flightdict:
        if city == flightdict[key][0]:
            print("Flight no.", key, "details:", flightdict[key])
    print("-" * 10)


def flights_per_cities(departure, arrival):
    return [key for key in flightdict
            if flightdict[key][0] == departure
            and flightdict[key][1] == arrival]


def discount(price, disc):
    return price - price * disc


def discount_printer(prices, discounts):
    price_list = list(zip(prices, discounts))
    for price_pair in price_list:
        print("Original price: {0}; after discount: {1}".format(
              f"{price_pair[0]:.2f}", f"{discount(price_pair[0], price_pair[1]):.2f}"))


# Part B
# Function calls
list_all_cities()
print("-" * 10)

searchcity = 'HNL'
flights_per_city(searchcity)
searchcity = 'CUR'
flights_per_city(searchcity)
searchcity = 'ITO'
flights_per_city(searchcity)

departcity = 'NRT'
arrivecity = 'ITO'
print("Flights from '" + departcity + "' to '" + arrivecity + "':",
      flights_per_cities(departcity, arrivecity))

departcity = 'HKG'
arrivecity = 'HNL'
print("Flights from '" + departcity + "' to '" + arrivecity + "':",
      flights_per_cities(arrival=arrivecity, departure=departcity))
print("-" * 10)

price_list = [(100, 0.05), (299, 0.15), (399.95, 0.10)]
print("Iterating through price_list:")
for price_pair in price_list:
    print("Original price: {0}; after discount: {1}".format(
        f"{price_pair[0]:.2f}", f"{discount(price_pair[0], price_pair[1]):.2f}"))
print("-" * 10)

pricelist = [100, 299, 399.95]
disclist = [0.05, 0.15, 0.10]
print("Calling discount_printer() function:")
discount_printer(pricelist, disclist)
