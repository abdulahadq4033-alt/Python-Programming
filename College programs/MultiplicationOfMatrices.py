#24. Write a python program to perform multiplication of two square matrices.

X = [[12,7,3],
[4 ,5,6],
[7 ,8,9]]

Y = [[5,8,1],
[6,7,3],
[4,5,9]]

result = [[0,0,0],
[0,0,0],

[0,0,0]]
for k in result:
    print(k)

# Iterate through rows of X
for i in range(len(X)):
# Iterate through columns of Y
    for j in range(len(Y[0])):
# Iterate through rows of Y/columns of X
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]

for r in result:
    print(r)
