import string
lines=0
upper=0
lower=0
digits=0
symbols=0
words=0
letter_a=0

file=open("demo.txt",'r')

for line in file:
    lines=lines+1
    if line.startswith('a'):
        letter_a=letter_a+1
    for char in line:
        if char.isupper():
            upper=upper+1
        elif char.islower():
            lower=lower+1
        elif char.isspace():
            words=words+1
        elif char.isdigit():
            digits=digits+1
        elif not char.isalpha():
            symbols=symbols+1

print("Number of lines:",lines)
print("Number of words:",words)
print("Number of Uppercase:",upper)
print("Number of Lowercase:",lower)
print("Number of digits:",digits)
print("Number of symbols:",symbols)
print("Lines starting with 'A':",letter_a)
