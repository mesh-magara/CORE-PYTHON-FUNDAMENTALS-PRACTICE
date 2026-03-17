#printing numbers from one to a hundred
even_number = []
odd_number = []
for number in range(1,100):
    if number % 2 == 0:
        even_number.append(number)
    else:
        odd_number.append(number)

print("Even-numbers are : ",even_number)
print(f"Odd-numbers are : {odd_number}")

def sum(numbers):
    sum = 0
    for number in numbers:
        sum = sum + number

    return sum

print('The sum of even numbers is : ',sum(even_number))

print('The sum of odd numbers is : ',sum(odd_number))



"""writing a python function that adds two numbers """
a = int(input("Enter your first number : "))
b = int(input("Enter your second number : "))

def sum_of_two_numbers(x,y):
    return x + y

print(f'The sum of {a} and {b} is : {sum_of_two_numbers(a,b)}')

