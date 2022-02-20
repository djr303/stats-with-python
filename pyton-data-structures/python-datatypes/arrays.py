import numpy as np

myList = [1,2,3]
myList2 = [4,5,6]

myArray = np.array(myList)
myArray2 = np.array(myList2)

myArray3 = myArray + myArray2

print(myArray3)

myProduct = myArray.dot(myArray2)

print(myProd)