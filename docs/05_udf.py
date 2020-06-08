# Functions
def generate_number_list(upper_limit):
    index = 0
    output_list = []  # Tom Liste
    while (index < upper_limit):
        output_list.append(index)
        index += 1
    return output_list


print(generate_number_list(5))
print(generate_number_list(10))


# Named Argument vs Positional Argument
def generate_number_list(start_index, upper_limit):
    index = start_index
    output_list = []  # Empty List
    while (index < upper_limit):
        output_list.append(index)
        index += 1
    return output_list


print("Positional Arguments = ", generate_number_list(1, 11))
print("Named Arguments = ", generate_number_list(upper_limit=10, start_index=2))


# Default Arguments
def generate_number_list(start_index, upper_limit, increment=1):
    index = start_index
    output_list = []  # Empty List
    while (index < upper_limit):
        output_list.append(index)
        index = index + increment
    return output_list


print("Default Value for Increment = ", generate_number_list(0, 11))
print("Non-Default Value for Increment = ", generate_number_list(0, 11, 2))

#  Celsius to Fahrenheit
def fah_cel(Fahrenheit):
    Fahrenheit = float(Fahrenheit)
    celsius = (Fahrenheit - 32) * (5/9)
    return celsius

print(fah_cel(212))  # 212 F = 100 C
print(fah_cel(32))   # 32 F = 0 C


#  Fahrenheit to Celsius
def cel_fah(Celsius):
    Celsius = float(Celsius)
    Fahrenheit = (Celsius * (9/5)) + 32
    return Fahrenheit

print(cel_fah(100))
print(cel_fah(0))


