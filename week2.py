#empty list
my_list = []
#appending values
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#insertion
my_list.insert(1,15)
#Extending a list
my_list.extend([50,60,70])

#Remove last element
my_list.pop()
#Sort in ascending order
my_list.sort()

#finding the index of a 30
myindex=my_list.index(30)
print(myindex)