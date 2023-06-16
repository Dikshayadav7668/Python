cars=100
space_in_cars=4.0
drivers=30
passengers=90
car_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_cars
average_passenger_per_car=passengers/drivers

print("There Are",cars,"cars available")
print("There are only",drivers,"drivers availbale")
print("There will be",car_not_driven,"empty cars")
print("We can transport",carpool_capacity,"people today")
print("We have",passengers,"carpool today")
print("We need to put about",average_passenger_per_car,"in each car")