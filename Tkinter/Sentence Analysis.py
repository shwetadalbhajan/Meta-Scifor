import calc

total_lines = 0
upper_count = 0
lower_count = 0
digit_count = 0
symbol_count = 0

# Open the file to read and analyze
with open("text", 'r') as file:
    for line in file:
        total_lines += 1
        for char in line:
            if char.isupper():
                upper_count += 1
            elif char.islower():
                lower_count += 1
            elif char.isdigit():
                digit_count += 1
            elif not char.isspace():
                symbol_count += 1

# Print the results
print("Total lines:",total_lines)
print("Uppercase letters:",upper_count)
print("Lowercase letters:",lower_count)
print("Digits:",digit_count)
print("Symbols:",symbol_count)
print()
print(calc.add(3,4))
print(calc.sub(3,4))
print(calc.mul(3,4))
print(calc.div(3,4))
print(calc.mod(3,4))
print(calc.inc(3))
print(calc.dec(3))