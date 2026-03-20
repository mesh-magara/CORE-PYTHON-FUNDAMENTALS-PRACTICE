"""A PROGRAM THAT COUNTS THE FREQUENCY OF CHARACTERS """

word = "I love programming python language"
name = "meshack magara"
def frequency_checker(words):
    # remove ALL whitespace before counting
    new_word = words.replace(" ", "")

    freq_count = {}

    for character in new_word:
        if character not in freq_count:
            freq_count[character] = 1
        else:
            freq_count[character] += 1

    return freq_count

print(frequency_checker(word))
print(frequency_checker(name))

