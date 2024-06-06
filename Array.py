
'''
from math import inf

#iterate through an array of integers
a=["1","2","3","4","5","6","7","8","9","10"]
length=len(a)
for i in range(0,len(a)):
  print(a[i])

#largest element among elemetn of array
arr=[1,2,3,4,5,6,7,334,576,4403]
array_length=len(arr) # type: ignore
largest_element = float(-inf)
for i in range(array_length): # type: ignore
    element =arr[i] # type: ignore
    if element>largest_element:
        largest_element=element
        print(largest_element)


#summing array element
arr = [1,2,3,4,5,6,7,8,9,10];     
sum = 0;       
for i in range(0, len(arr)):    
   sum = sum + arr[i];        
print("Sum of all the elements of an array: " + str(sum))

#Array reversal
numbers = [1,3,5,7,9,11,13,15,17,19]
numbers.reverse()
print('Reversed List:',numbers)


a=[2,3,4,5,8,1,9,6]
for i in range(len(a)-1,-1,-1):
  print(a[::-1])



#Concationate two lists
list1 =["M","na","i","Sin"]
list2 =["y","me","s","dhu"]

for i in list1:
  print(i)
  for i,j in zip(list1,list2):
    print(i+j)


for i in range(len(list1)):
  list=list1[i]+list2[i]
print(list)


for i in range(len(list1)):
  final_value = list1[i]+list2[i]
  if "name" in final_value:
    list1[i]=list1[i]+list2[i]
print(list1)

list1 = ["M", "ca"]
list2 = ["y", "ts"]
concatenated_list = []
for i in range(len(list1)):
    concatenated_list=list1[i]+list2[i]
print(concatenated_list)
'''
