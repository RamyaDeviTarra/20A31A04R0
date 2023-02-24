#write a program to combine a list of cubes for given number
cubes = []
for  i in range(11):
    cubes.append(i**3)
print(cubes)
#2nd way
c = [i**3 for i in range(11)];
print(c)
