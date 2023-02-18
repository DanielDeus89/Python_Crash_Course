# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the 
# first 10 cubes.

cubes = [i**3 for i in range(1,11)]

for i in cubes:
    print(i)