import random
def createRandomSortedList(num, start = 1, end = 500): 
    arr = [] 
    tmp = random.randint(start, end) 
      
    for x in range(num): 
          
        while tmp in arr: 
            tmp = random.randint(start, end) 
              
        arr.append(tmp) 
          
    arr.sort() 
      
    return arr

print(createRandomSortedList(10))
