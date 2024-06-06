#Print indices through string
list=[123,23,'123456789',1,23]

for i in range(len(list)):
    if isinstance(list[i],str):
        continue
    print(list[i])   
    

    