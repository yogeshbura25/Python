r = -18
set_data = {5, "TwentyFive", 75.4, r}

print(set_data)     #{75.4, 'TwentyFive', 5, -18}
print(type(set_data))     #<class 'set'>
print(len(set_data))     #4

#AddingItemsInSet
set_data.add("SetData")
print(set_data)      #{'TwentyFive', 5, 75.4, -18, 'SetData'}

#UpdatingItemsInSet
set_data.update(["Bharath", 75.5])
print(set_data)      #{'Bharath', 5, 75.4, 75.5, 'SetData', -18, 'TwentyFive'}
print(len(set_data)) #7

#Remove/Discard
set_data.remove("TwentyFive")
print(set_data)   #{'SetData', 5, 75.4, 75.5, -18, 'Bharath'}

#StringRepetition
print(set_data * 3) #In set Values stored in unique so no repetition


