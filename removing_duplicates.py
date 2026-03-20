""" REMOVING DUPLICATES FROM A LIST """
fruits = ['mango','apple','pineapple','mango','cherry','apple','banana','pineapple','cherry']

# option one is to use the tuple or set
def remove_duplicate(arr):

    new_list  = set(arr)
    
    return list(new_list)

print("New list without the duplicates is : ",(remove_duplicate(fruits)))

#option two is to use an empty list
def removing_duplicate(arr):
    new_list  = []

    for item in arr:
        if item not in new_list:
            new_list.append(item)
        
    return new_list

print("New list without the duplicates is : ",(removing_duplicate(fruits)))
