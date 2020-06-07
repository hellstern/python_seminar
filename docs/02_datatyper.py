# Datatyper

print("Data types")
a = 10               # Integer
b = -9               # Integer
fl1 = 0.78           # Float
bl1 = True           # Boolean
st1 = "Hello World"  # String

# String
print(st1)
print(st1.upper())
print(st1.lower())

print(len(st1))

st2 ="from Python"

st3 = st1 + " " + st2
print(st3)

# Vis datatype
print("Positive Integer = ", a, " | ", type(a))
print("Negative Integer = ", b, " | ", type(b))
print("Float = ", fl1, " | ", type(fl1))
print("Boolean = ", bl1, " | ", type(bl1))
print("Float = ", st1, " | ", type(st1), " | ", len(st1))
print("st1[0] = ", st1[0])
print("st1[6:11] = ", st1[6:11])


# Type Conversion
print()
print("Type Conversion")
str1 = "15"
in1 = 10
fl1 = 10.8

print("str1 = ", str1, " | Type = ", type(str1))
print("in1 = ", in1, " | Type = ", type(in1))
print("fl1 = ", fl1, " | Type = ", type(fl1))

print("int(str1) = ", int(str1), " | Type = ", type(int(str1)))
print("float(str1) = ", float(str1), " | Type = ", type(float(str1)))

print("str(int1) = ", str(in1), " | Type = ", type(str(in1)))
print("str(fl1) = ", str(fl1), " | Type = ", type(str(fl1)))

print("round(fl1) = ", round(fl1))


# Numerical Operations
print()
print("Numerical Operations")
num1 = 10
num2 = 4

print("Plus - num1 + num2 = ", num1 + num2)
print("Minus - num1 - num2 = ", num1 + num2)
print("Gange - num1 * num2 = ", num1 * num2)
print("Division - num1 / num2 = ", num1 / num2)

num1 += 1
print(num1)

num2 += 10
print(num2)

num1 *= 10
print(num1)

num2 /= 7
print(num2, " | Type = ", type(num2))


# Data Structures
print()
print("Data Structures")

# List
print("List")
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list1[0])
print(list1[3:5])
print(list1[::2])
print(list1[1::2])
print(list1[-1])
print(list1[:-1])
print(list1[::-1])

# List Methods
list2 = [4,1,3,9,7]
list3 = ['a','ab', 'abc','ab', 'ab']

# Sort
print("Sortering")
print(list2, sep=", ")
print(list2.sort(), sep=", ")

print(list3)
print(list3.sort())

# Add
print()
print("Add")
print(list2)
list2.append(8)
print(list2)

# Insert
print()
print("Insert")
print(list2)
list2.insert(1, 2)
print(list2)

# Ændre
print()
print("Change")
list2[3] = 222
print(list2)

# Remove
print()
print("Remove")
print(list2)
list2.remove(9)
print(list2)

# Len / Antal
print()
print("Len")
print(list2.__len__())
print(len(list2))


# Join
print()
print("Join")
print(" ".join(list3))


# Loop List
print()
print("Loop List")
for x in range(len(list2)):
    print(list2[x])


# Tuple
print()
print("Tuple")