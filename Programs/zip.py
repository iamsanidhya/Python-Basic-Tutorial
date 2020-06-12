list1 = [1,2,3,4,5]
list2 = ['one', 'two', 'three', 'four', 'five']
kist3 = [6,5,4,3,2]
zipped =list(zip(list1,list2,kist3))
print(zipped)


unzipped = list(zip(*zipped))
print(unzipped)

