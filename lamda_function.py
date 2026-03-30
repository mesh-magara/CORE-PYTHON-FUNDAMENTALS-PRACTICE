#writing a lamda function that squares up the numbers
square = lambda x : x * x 

print(square(2))
print(square(8))

#A PROGRAM THAT PRINTS A STAR PATTERN
for x in range(10):
    print('*' * x)

for x in range(10,0,-1):
    print('*' * x)

# Top part
for i in range(1, 6):
    print(" " * (5 - i) + "*" * (2 * i - 1))

# Bottom part
for i in range(4, 0, -1):
    print(" " * (5 - i) + "*" * (2 * i - 1))