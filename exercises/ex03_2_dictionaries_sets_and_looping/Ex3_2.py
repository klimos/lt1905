"""
Exercise 3.2 Dictionaries, Sets, and Looping
Ex3_2.py
"""

# Part A
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

print("\nPart A\n" + '-' * 6)
print('Airport codes and cities:')
for key in city_code_dict:
    print(key, '-', city_code_dict[key])


# Part B
codelist = ['HNL', 'ITO', 'LHR', 'LGA', 'GCM', 'MSY']
flightlist = ['HNL', 'HKG', '2022-01-03 16:00', '2022-01-03 20:00', 99.95, 4]

print("\nPart B\n" + '-' * 6)
keys = []
not_keys = []
for code in codelist:
    if code in city_code_dict:
        keys.append(code)
    else:
        not_keys.append(code)
print("With 'for' loop, codes in dictionary:", keys)
print("With 'for' loop, codes not in dictionary:", not_keys)
print('-' * 6)

keys = [code for code in codelist if code in city_code_dict]
not_keys = [code for code in codelist if code not in city_code_dict]
print("With list coprehension, codes in dictionary:", keys)
print("With list coprehension, codes not in dictionary:", not_keys)
print('-' * 6)

keys = list(set(codelist) & city_code_dict.keys())
not_keys = list(set(codelist) - city_code_dict.keys())
print("With set operation, codes in dictionary:", keys)
print("With set operation, codes not in dictionary:", not_keys)
print('-' * 6)

if flightlist[0] in city_code_dict and flightlist[1] in city_code_dict:
    print("Both departure airport", flightlist[0],
          "and arrival airpot", flightlist[1],
          "are in dictionary")
else:
    print("Either departure airport", flightlist[0],
          "or arrival airpot", flightlist[1],
          "is not in dictionary")


# Part C
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

print("\nPart C\n" + '-' * 6)
hnl_flights = [key for key in flightdict if flightdict[key][0] == 'HNL']
print("Flight numbers departing from 'HNL':", hnl_flights)

roundtrip_flights = [key for key in flightdict if flightdict[key][0] == flightdict[key][1]]
print("Roundtrip flight numbers:", hnl_flights)
print('-' * 6)

print("Flights sorted by number:")
flighnumber_list = list(flightdict.keys())
flighnumber_list.sort()

for flightnumber in flighnumber_list:
    print(flightnumber, flightdict[flightnumber])


# Part D
airports = (
    "HNL,Honolulu",
    "LHR,London/Heathrow",
    "ARN,Stockholm/Arlanda",
    "HKG,Hong Kong",
    "GCM,Grand Cayman BWI")

airport_list = ','.join(airports).split(',')
airport_codes = airport_list[0::2]
airport_cities = airport_list[1::2]
print("\nPart D\n" + '-' * 6)
print("Airport codes:", airport_codes)
print("Airport cities:", airport_cities)
