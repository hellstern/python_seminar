# Operators

# Aritmetiske operators
a = 10
b = 3

# Plus
print('a + b =', a+b)

# Minus
print('a - b =', a-b)

# Gange
print('a * b =', a*b)

# Division
print('a / b =', a/b)

# Modulus
print('a % b =', a%b)

# Exponent
print('a ** b =', a**b)


# Tildelings operators
# Lig med
a = 10
print("'a = 10' = ",a)

# Add AND
a = 10
a += 3 # samme som a = a + 3
print("'a += 3' = ", a)

# Subtract AND
a = 10
a -= 3 # samme som a = a - 3
print("'a -= 3' = ", a)

# Multiply AND
a = 10
a *= 3 # samme som a = a * 3
print("'a *= 3' = ", a)

# Divide AND
a = 10
a /= 3 # samme som a = a / 3
print("'a /= 3' = ", a)

# Modulus AND
a = 10
a %= 3 # samme som a = a % 3
print("'a %= 3' = ", a)


# Sammenlignings operators
a = 10
b = 3

# Større end
print('a > b is', a > b)

# Mindre end
print('a < b is', a < b)

# Ens
print('a == b is', a == b)

# Ikke ens
print('a != b is', a != b)

# Større end eller lig med
print('a >= b is', a >= b)

# Mindre end eller lig med
print('a <= b is', a <= b)

# Logiske operators
a = 10

# Giver TRUE
print(a > 6 and a < 20)

# Giver TRUE
print(a > 6 or a < 8)


# Identifikations operators
# is
a = ["Python", "JavaScript"]
b = ["Python", "JavaScript"]
c = a

# returns True since c is the same object as a
print(a is c)

# returns False since lists are mutable
print(a is b)

# Returns True because a is equal to b
print(a == b)

# is not
a = ["Python", "JavaScript"]
b = ["Python", "JavaScript"]
c = a

# returns False since c is the same object as a
print(a is not c)

# returns True since lists are mutable
print(a is not b)

# illustrates the difference between "is not" and "!=": it returns False because a is equal to b
print(a != b)


# "Medlemsskabs" operators
a = ["Python", "JavaScript"]

# returns False because the value is not in the list sequence; Python is case sensitive
print("Javascript" in a)

# returns True
print("Javascript" not in a)
