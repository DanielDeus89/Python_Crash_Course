# 4-12. More Loops: All versions of foods.py in this section have avoided using 
# for loops when printing to save space. Choose a version of foods.py, and 
# write two for loops to print each list of foods.

myFoods = ['pizza','falafel','carrot','cake']

myFoods.append('cannoli')

friendsFood = myFoods[:]
friendsFood.append('dog')


print("My favorite foods are:")
print(myFoods)
for i in myFoods:
    print(i)

print("\nMy friend's favorite foods are:")
print(friendsFood)
for i in friendsFood:
    print(i)