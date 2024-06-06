'''
#Square Each Item in a List
num = [1, 2, 3, 4, 5,6,7]
squared_numbers=[number**2 for number in num]
print(squared_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7]

square= []
for i in numbers:
    square.append(i**2)
print(square)



#Concatenate Two Lists in a Specific Order

list1 = ["Hello", "take"]
list2 = ["Dear", "Sir"]
concatenated_list = []

for item1 in list1:
    for item2 in list2:
        concatenated_list.append(item1+ "" +item2)
        
print(concatenated_list)


# Iterate through both lists simultaneously
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for item1, item2 in zip(list1, reversed(list2)):
    print(item1, item2)
'''