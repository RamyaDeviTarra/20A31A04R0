# write a program tha accepts the string from the user redidplays the same string after removing the vowels
name = str(input("enter the value"))
A=['a', 'e', 'i', 'o', 'u']
for i in range(len(name)):
    if name[i] in A:
        name = name.replace(name[i], " ")
print(name)
