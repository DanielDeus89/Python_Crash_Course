
motorcycles = ["Honda", "Honda", "Yamaha",  "Suzuki", "Harley-Davidson", "Ducati", "Kawasaki", "BMW"]

print(motorcycles)

motorcycles[0]= 'ducati'
print(motorcycles)


motorcycles.append('ducati')
print(motorcycles)

#inserting

motorcycles.insert(0, 'Harley')
print(motorcycles)

#removing
del motorcycles[2]
print(motorcycles)

#pop last
popped_motor = motorcycles.pop()
print(popped_motor)
print(motorcycles)

#popping from any position 
first_owned = motorcycles.pop(-1)
print(first_owned)
print(motorcycles)

motorcycles.remove('Harley')
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)