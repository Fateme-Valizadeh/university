import math

lat1,lon1 = eval(input("Enter the latitude and longitude of the first point (in degrees): "))
lat2,lon2 = eval(input("Enter the latitude and longitude of the second point (in degrees): "))


lat1,lon1,lat2,lon2 = map(math.radians, [lat1,lon1,lat2,lon2])
radius = 6371.01

d = radius * math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2))


print("The distance between the two points is", d, "km.")