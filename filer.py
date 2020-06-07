# Filer

# Open fil
minfil = open("minfil.txt", "rt")

# Læs
print(minfil.read())

minfil.close()

# Skriv til - Overskriv
minfil = open("minfil.txt", "wt")
minfil.write("Tekst skrevet fra Python")

print(minfil)

# Skriv til - Tilføj
minfil = open("minfil.txt", "at")
minfil.write("Tekst der er tilføjet til filen")
minfil.close()

minfil = open("minfil.txt", "rt")
print(minfil)


# Opret en ny fil
nyfil = open("min_nye_fil.txt", "x")
