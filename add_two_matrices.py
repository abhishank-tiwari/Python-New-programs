#Adding two matrices

x = [[12 , 7 , 3],
     [9, 8 ,6],
     [7, 8 , 6]]

y = [ [8,7,9],
      [11,7,3],
      [9,10,2]]

result = [ [0,0,0],
           [0,0,0],
           [0,0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j] = x[i][j] + y[i][j]

print(result)