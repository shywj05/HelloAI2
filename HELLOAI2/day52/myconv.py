import numpy as np

arr = []

arr.append([0,1,1,0])
arr.append([0,1,1,0])
arr.append([0,1,1,0])
arr.append([0,1,1,0])

arr_n = np.array(arr)

filter = [[1,1],
          [1,1]]

filter_n = np.array(filter)

out_n = np.zeros((2,2))

for i in range(2):
    for j in range(2):
        sum = 0
        s1 = arr_n[i*2][j*2]     * filter_n[0][0]
        s2 = arr_n[i*2][j*2+1]   * filter_n[0][1]
        s3 = arr_n[i*2+1][j*2]   * filter_n[1][0]
        s4 = arr_n[i*2+1][j*2+1] * filter_n[1][1]
        sum = (s1 + s2 + s3 + s4) / 4
        out_n[i][j] = sum
print(out_n)
        




