# *************************** LISTS FUNCTIONS *******************************
evenNum = [16, 4, 6, 8, 10, 12, 2 , 13]
animalsPet = ["Cow","Rat","Cat","Goat","Goat"]
animalsWild = ["Lion", "Tiger" , "Elephant"]

print(evenNum)
print(animalsPet)
print(animalsWild)

#Extend Function = it is use to extend or merge two lists we will use.
animalsPet.extend(animalsWild)
print(animalsPet)

#Append Function = it is use to add a data in a list it will add data in  last
animalsPet.append("Rabbit")
print(animalsPet)

#Insert Function = it is use to insert data in any position by passing parameter of Index position where you want to add data in list
animalsWild.insert(2, "Jackal")
print(animalsWild)

#Remove Function = It is use to remove any element from data set list
evenNum.remove(13)
print(evenNum)

#Clear function = It is use to clear all the elements from data set  list
evenNum.clear()
print(evenNum)

#Pop function = It is use to remove last element from the data set list
animalsPet.pop()
print(animalsPet)

#index function inside print command tells about at which index searched data  is stored
print(animalsPet.index("Goat"))

#count function used to count the number of repeating elements inside the list
print(animalsPet.count("Goat"))
 
#sort function is used to sort data in assending order/alphabetical order
animalsPet.sort()
print(animalsPet)

evenNum = [16, 4, 6, 8, 10, 12, 2 , 13]
evenNum.sort()
print(evenNum)

#Reverse Function  it is use to reverse the data element listing
evenNum.reverse()
print(evenNum)

#Copy function it is used to create a clone/copy of the data from list

animals = animalsWild.copy()
print(animals)
