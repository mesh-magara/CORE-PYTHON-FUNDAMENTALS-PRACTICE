# counting and returning vowels that are in  string
vowels = ['a','e','i','o','u']

word = 'welcome to the world of programming where evverything is just sweet'
new_word = word.strip()

vowels_in_words = []
for character in new_word:
    if character in vowels:
        vowels_in_words.append(character)

print("Vowels that are in the word are : ",set(vowels_in_words))

#  python progran that returns a reversed string and checks if palindrome
def reverse_palindrome(word):
    reversed_word = "".join(reversed(word))

    if reversed_word == word:
        print(f'{word} is a palindrome word')
    else:
        print(f"{word} is not a palindrome word")
    
    print(f"reversed word is : {reversed_word}")




reverse_palindrome('level')