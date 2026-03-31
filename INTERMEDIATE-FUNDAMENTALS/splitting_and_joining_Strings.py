text = "apple, banana, cherry"

# Splitting the strings using commas
fruits = text.split(",")
print(f"Fruits : {fruits}") #returns a list of words

#you can also join the string back to a string
new_text = "-\n".join(fruits)
print(new_text)

