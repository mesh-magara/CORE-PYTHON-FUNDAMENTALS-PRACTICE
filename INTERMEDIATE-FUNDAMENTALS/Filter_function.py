"""declare a string or arrays """

numbers = []
for i in range(1,30):
    numbers.append(i)

""" 
  Filter function is used to extract elememts from an iterable for which the function returns true
  syntax:

     filter(function,iterable)

"""

#use the filter function to find even numbers 
evenr = lambda evens : evens % 2 == 0
evens = list(filter(evenr, numbers))
print(f"EVEN NUMBERS : {evens}")\

result = filter(lambda x : x > 10, numbers)
print(list(result))

        
#example of a filter function that returns strings that start with letter 'A'
names = ['Alice','Bob','Andrew','john','Ann','Ben','Annastacia']

res = filter(lambda name: name.startswith("A"), names)
print(list(res))

#example of filtering odd numbers from a list
odd = filter(lambda x : x % 2 == 1, numbers)
print(list(odd))

#an example to return numbers that are greate than 5
greater_than5 = filter(lambda y : y > 15, numbers)
print(list(greater_than5))

#an example to find the list of strings that have lenght greater than 5
words = ['apple','cat','banana','graper','watermelon']

wrds = filter(lambda word: len(word) >= 5, words)
print(list(wrds))

def _5and3(n):
    return (n % 3 == 0) and (n % 5 == 0) #the function will return true if the numbers is divisible by both 3 and 5

numbers2 = []
for number in range(1,100):
    numbers2.append(number)

divisibleby3and5 = filter(_5and3,numbers2)
print(list(divisibleby3and5))

#A program that takes a list of student marks and only return the marks that are above average
marks = [20,43,83,94,32,47,58,59,93,99,86,74,56]

def above_average(n):
    return (n >= 50)

passed = filter(above_average,marks)
print(list(passed))

#a program that filter the palindrome words

wds = ['madam','radar','car','level','world','python']
def pallindrome_checker(word):
    reversed_word = "".join(reversed(word))

    return reversed_word == word #will return true if the reversed word is equal to the original word

palindrome_words = filter(pallindrome_checker,wds)
print(list(palindrome_words))

score  = []
for number in range(1000,10000,500):
    score.append(number)

def divisible_by_15_and_20(num):
    return num % 15 == 0 and num % 20 == 0

numbers_divisible_by_both_15_and_20 = filter(divisible_by_15_and_20,score)
print(list(numbers_divisible_by_both_15_and_20))


