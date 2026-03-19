def maximum_number(a,b,c):
    if a > b :
        if a > c:
            print(f"{a} is the largest number")
        else:
            print(f"{c} is the largest number")
        
    else:
        if b > c:
            print(f"{b} is the largest number")   
        else:
            print(f"{c} is the largest number")

def max_number(a,b,c):
    numbers = [a,b,c]

    maxim_number = numbers[0]
    
    for number in numbers:
        if number > maxim_number:
            maxim_number = number
    
    return maxim_number

a  = int(input("Enter your first number : "))
b = int(input("Enter your second number : "))
c = int(input("Enter the third number : "))

maximum_number(a,b,c)
print("The maximum value is : ", max_number(a,b,c))

def factorial(n):
    total_factorial = 1

    for i in range(n,1,-1):
        if i == 0 or i == 1:
            total_factorial = 1
        else:
            total_factorial *= i
        
    return total_factorial

print(factorial(1))




def multiplication_table(number):
    print(f"---The multiplication table for {number} --------- ")
    for i in range (0,10):
        print(f" {number} * {i} = {number * i}")
    
multiplication_table(4)