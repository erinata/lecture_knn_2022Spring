import pandas


dataset = pandas.read_csv("abalone.data", header=None)

dataset.columns = ["Sex","Length","Diameter","Height","Whole","Shucked","Viscera","Shell","Rings"]

dataset = dataset.drop("Sex", axis=1)

print(dataset)

target = dataset.iloc[:,7].values
data = dataset.iloc[:,0:7].values

print(target)
print(data)


