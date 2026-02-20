import numpy as np

Numbers = np.array([[1,2,3,4,5,6,7,8,9,10]
                    # [1,2,3,4,5,6,7,8,9,10] broadcasting cannot done when not equal or 1
                    ])
SNumbers = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
 
print(Numbers.shape)
print(SNumbers.shape)

print(Numbers * SNumbers)