import pandas as pd

Row = 0
Column = 0

data_pd = pd.read_excel("myexcel01.xlsx", 
                     header=None, index_col=None, names=None)
data_np = pd.DataFrame.to_numpy(data_pd)

print(data_pd)
print(len(data_np))

for row in data_np:
    print(row[0],row[1])

print(data_np[Row][Column])