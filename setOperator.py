#set Operator 

set_a = {4, 2, 8, 25, 18}
set_b = {1, 2, 18} 

#Union 
#It combines the unique elemets from two sets into a new set.
union_set = set_a | set_b
print(union_set)     #{1, 2, 18, 4, 8, 25}

#Intersection
#It returns a new set that contains the common elements between two sets.
intersection_set = set_a & set_b
print(intersection_set)     #{2, 18}

#Difference
#It returns a new set that contains the elements that are in first set but not in the second set.
difference_set = set_a - set_b
print(difference_set)     #{8, 25, 4}

#Symmetric Difference
#It returns a new set that contains the elements that are in either of the sets, but not in both.
symmetric_difference_set = set_a ^ set_b
print(symmetric_difference_set)     #{1, 4, 8, 25}

#SetComparisons
#To Compare two sets

#Subset
#It returns True if all elements of the first set are present in the seconds set.
sub_set = set_b.issubset(set_a)
print(sub_set)                    #False

#SuperSet
#It returns True if all elements of the second set are present in the first set.
super_set = set_a.issuperset(set_b)
print(super_set)                  #False
 
#DisjoinsSet
#It returns True if the two sets have no common elements, Otherwise False.
disjoint_set = set_a.isdisjoint(set_b)
print(disjoint_set)               #False