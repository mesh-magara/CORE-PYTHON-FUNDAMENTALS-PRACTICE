"""reduce functions is used to do all the ites in the iterative cummulative """
#program that sums all the items in the list
from functools import reduce # you have to import from the function tools the given function

numbers = [10,20,30,40,50,60,70,80,90,100]

sum  = (reduce(lambda x,y : x +y , numbers))
print("sum = ", (sum))

multiply = reduce(lambda x,y : x * y, numbers)
print(f"product  : {multiply}")