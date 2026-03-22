import math

def check_prime(number):
    #check first if the number is  2 or 3 0r 5
    if number == 2 or number == 3 or number == 5:
        print(f'{number} is  a prime number????')
    
    #check if the number is divisible by both 2,3 or 5
    elif number % 2 == 0 or number  % 3 == 0 or number % 5 == 0:
       print(f"{number} is not a prime number???")

    #if not use the squareroot of the number
    else:
      i = 2
      while i < math.sqrt(number):
        if number % i == 0:
            print("The number is not a prime number")
        else:
            print(f"{number} is a prime number 🥲 ")
            break
        
        i = i + 1
    
x = int(input("Enter your number to check: "))


check_prime(x)
        