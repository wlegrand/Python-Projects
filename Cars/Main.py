from Cars import Cars
from Garage import Garage

c1 = Cars("Lamborghini", "red", 1000, "Aventador")
c2 = Cars("Porsche", "blue", 400, "Panamera Turbo")
c3 = Cars("Mercedes-Benz", "black", 300, "classe E")

garage = Garage("Geneva", 3)

garage.add_car(c1)
garage.add_car(c2)
garage.add_car(c3)

print(garage.cars[0].brend, garage.cars[0].model, garage.cars[0].color, garage.cars[0].power)
print(garage.cars[1].brend, garage.cars[1].model, garage.cars[1].color, garage.cars[1].power)
print(garage.cars[2].brend, garage.cars[2].model, garage.cars[2].color, garage.cars[2].power)




print("The garage is in", garage.location, "and he have", garage.max_cars, "places")
