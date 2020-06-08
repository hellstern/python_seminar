# IF / ELSE
print("If / ELSE")
print()
antal = 26
if(antal < 10):
  print("Under området")
elif(antal >= 10 and antal < 30 ):
  print("I området")
else:
  print("Over område")

# For Loop
print("FOR LOOP")
print()
list1 = [1,2,3,4,5,6,7,8,9,10]
antal = 0
print("list1 = ", list1)
print()
for list_item in list1:
  print("list1[",antal,"] = ", list_item)
  antal +=1

# print Hello World
str1 = "Hello World!"
print(str1)
for c in str1:
    print(c)

# Frugt :-)

frugter = ["æble", "banan", "kirsebær", "pære", "elefant", "kiwi"]
print("Tilgængelig frugter = ", frugter)
for frugt in frugter:
 if(frugt == "elefant"):
   print("Jeg kan ikke spise", frugt)
   # break
   continue
 else:
   print("Jeg kan spise", frugt)


# While Loop
print()
print("While Loop")
count = 0
while count < 5:
    print(count)
    count += 1




