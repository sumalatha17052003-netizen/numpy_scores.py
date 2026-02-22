import numpy as np 
scores=np.array([[85,90,68,98],
                 [67,67,78,45],
                 [67,87,89,86],
                 [78,89,98,78],
                 [56,78,90,67]])
import pandas as pd
df=pd.DataFrame(scores,columns=["subject1","subject2","subject3","subject4"],index=["std1","std2","std3","std4","std5"])
print(df)
print(df.loc['std3','subject2'])
print(df.loc[['std4','std5']])
print(df.loc['std1':'std3','subject2':'subject3'])
import numpy as np 
scores=np.array([[85,90,68,98],
                 [67,67,78,45],
                 [67,87,89,86],
                 [78,89,91,78],
                 [56,78,90,67]])
print(scores.mean(axis=0))
import numpy as np

# Example student scores (rows = students, columns = subjects)
scores = np.array([[85,90,68,98],
                 [67,67,78,45],
                 [67,87,89,86],
                 [78,89,91,78],
                 [56,78,90,67]
    
])

curve = np.array([5, 3, 7, 2])
curved_scores = scores + curve
print(curved_scores)
print(curved_scores.mean(axis=0))
normalized_scores = ((curved_scores.T - curved_scores.min(1)) /
                     (curved_scores.max(1) - curved_scores.min(1))).T
print(normalized_scores)
print(normalized_scores.argmax(axis=1))
print(normalized_scores.argmin(axis=0))



