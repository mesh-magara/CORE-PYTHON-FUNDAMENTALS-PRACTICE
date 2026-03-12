print("----------FACULTY OF SCIENCE ASPIRANTS-------------- ")
print("SELECT ONLY ONE OF THE ASPIRANTS")
print("""
       1.John
       2.Mary
       3.Ann
       4.Jacob
       5.Liam
      
""")

"""
choice =  input("Who do you want to vote for: ")

voted = choice.capitalize()
print(f"you voted for : {voted}")

"""
aspirants = {

    "John" : 0,
    "Mary" : 0,
    "Ann" : 0,
    "Jacob" : 0,
    "Liam" : 0
}
i = 0
while i < 4:
    choice  = input("choose one candidate : ")
    
    if choice.capitalize() not in aspirants:
        print("No such aspirant!!!!")
    else:
        voted = choice.capitalize()
    #Assigning the scores to individual names
    for aspirant,value in aspirants.items():
        if aspirant ==  voted:
            aspirants[aspirant] += 1
   
    i += 1 


print(f"{list(aspirants.items())}")

results = list(aspirants.items())

maximum_score = results[0][1]
for x in results:
   if x[1] > maximum_score:
       maximum_score = x[1]
       print(f"The winner is {x[0]} and won by {maximum_score}")
    
    

    

    



