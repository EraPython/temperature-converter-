# Made by Arnav-

print("Temperature converter. Format = [<temperature><unit>-<unit it has to be converted]"
      ", Eg: 1243c-f")

raw_data = input("Enter the temperature: ")
raw_info = raw_data.split("-")

v_unit = raw_info[-1]
del raw_info[-1]

u_unit = str(raw_info[0][-1])
u_lit = [_ for _ in raw_info[0]]
del u_lit[-1]
u_temp = ""

for i in u_lit:
    u_temp += i


# Celsius to Fahrenheit
def ctof(x):
    return (float(x) * 9 / 5) + 32


# Fahrenheit to Celsius
def ftoc(x):
    return float(x) / (9/5) + 32


# Celsius to Kelvin
def ctok(x):
    return float(x) + 273


# Kelvin to Celsius
def ktoc(x):
    return float(x) - 273


# Fahrenheit to Kelvin
def ftok(x):
    return float(ftoc(x)) + 273


# Kelvin to Fahrenheit
def ktof(x):
    return float(ftoc(x)) - 273


# Fahrenheit to Celsius and vice-versa
if v_unit == "f" and u_unit == "c":
    print(ctof(u_temp))

if v_unit == "c" and u_unit == "f":
    print(ftoc(u_temp))

# Celsius to Kelvin and vice-versa
if v_unit == "c" and u_unit == "k":
    print(ctok(u_temp))

if v_unit == "k" and u_unit == "c":
    print(ktoc(u_temp))

# Fahrenheit to Kelvin and vice-versa
if v_unit == "f" and u_unit == "k":
    print(ftok(u_temp))

if v_unit == "k" and u_unit == "f":
    print(ktof(u_temp))
