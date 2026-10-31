from sklearn.datasets import load_iris
import numpy as np
iris=load_iris()
x=iris.data
y=iris.target
print("Iris Features :", iris.feature_names)
print("Iris Species/Target :", iris.target_names)
print("Count of total data samples:",len(x))
print("count of features:", x.shape[1])
unique_values, counts =np.unique(y, return_counts=True)
for label,count in zip(unique_values, counts):
    print(iris.target_names[label]," : ", count)
