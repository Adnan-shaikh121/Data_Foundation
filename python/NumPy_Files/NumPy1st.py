import numpy as np

# N-dimentional 
array = np.array([1,2,3])
array = array * 3
print(array) 

# multidimentional
multidimentional = np.array ([[['a','b','c'],['a','b','c'],['a','b','c']],
                    [['a','b','c'],['a','b','c'],['a','b','c']],
                    [['a','b','c'],['a','b','c'],['a',' ','c']]])

print(multidimentional.shape)

# chain indexing
print(multidimentional[0][0][0])

# multidimentional indexing (faster than chain indexing)
print(multidimentional[0,0,2])
print(multidimentional[0,0,2])

# another example
print(multidimentional[0, 0, 0] + multidimentional [2, 1, 1] + multidimentional [2, 0, 1])