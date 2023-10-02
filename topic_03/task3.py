car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car1={
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})

print(car)
del car["color"]
print(car)
car1.clear()
print(car1)
x=car.keys()
print(x)
x=car.values()
print(x)
x=car.items()
print(x)
