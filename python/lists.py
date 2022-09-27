# Lists 
# lists are mutable
numbers = [10,20,30,40]
animals = ['crunchy frog','ram bladder', 'lark vomit']
anyType = ['wonderful',555]
nested = ['spam',2.0,5,[10,50]]


#traverse list
for each in animals:
    print(each)
    
for each in range(len(animals)):
    print(animals[each])
    
for each in nested:
    print(each)
    
# cool operations in List
newNumbers = numbers * 2
print(newNumbers)

moreNested = nested + animals
print(moreNested)

print(numbers[0:2])  # slicing list


anyType.append(9.0)  # add new
print(anyType)

# ways to delete an item from the list
newList = numbers.pop(1)  #1
print(newList)

del numbers[1]     #2
print(numbers)

numbers.remove(40) #3
print(numbers)

#convert a string to array of characters
string = 'Objevtives'
listStr = list(string)
print(listStr)    #['O', 'b', 'j', 'e', 'v', 't', 'i', 'v', 'e', 's']
