
def set_operation(s1=None,s2=None):
    #handle default arguments
    set1 = s1 if s1 is not None else set()
    set2 = s2 if s2 is not None else set()

    # Intersection here
    the_intersection = set1.intersection(set2)
    
    #Union here
    the_union = set1.union(set2)

    #Differences here
    the_difference_set1_set2 = set1.difference(set2)
    the_difference_set2_set1 = set2.difference(set1)


    return {
        'the intersection' :the_intersection,
        'the union':the_union,
        'set1_set2':the_difference_set1_set2,
        'set2_set1':the_difference_set2_set1
    }


##static input
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}


##Dynamic input from users
set1 = set(input("Enter set1 items separated by spaces:").split())
set2 = set(input("Enter set2 items separated by spaces:").split())


#calling function
result_of_set_operation = set_operation(set1,set2)

print(f"The intersection between sets: {result_of_set_operation['the intersection']}")
print(f"The union between sets: {result_of_set_operation['the union']}")
print(f"The difference between set1_set2: {result_of_set_operation['set1_set2']}")
print(f"The difference between set2_set1: {result_of_set_operation['set2_set1']}")