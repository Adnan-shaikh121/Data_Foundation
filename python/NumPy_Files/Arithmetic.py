import numpy as np

# scaler arithmatic scaler is algebric term 

array = np.array([1,2,3,4])
print(array + 1)
print(array - 1)
print(array * 2)
print(array / 2)
print(array **2) # ** is power of like square in this case
print(array **3) #**is power of like cube in this case

# vectorized match function

print(np.sqrt(array),"vctor")
secArray = np.array([1.01, 3.2, 2.22,6.33])
print(np.round(secArray))
print(np.ceil(secArray))
print(np.floor(secArray))

# the pie
print(np.pi)

# element wise arithmetic

print(array + secArray)
print(array -secArray)
print(array *secArray)
print(array /secArray)
print(array **secArray)

# comparison ooperator

Score = np.array([91, 89, 65, 70, 100])
print(Score ==100)
print(Score <=60)
print(Score ==70)
print(Score>90)
