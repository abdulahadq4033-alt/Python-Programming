#23 A-. Write a python program to perform addition of two square matrices.

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

# iterate through rows

for i in range(len(X)):
# iterate through columns
    for j in range(len(Y)):
#for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]

for k in result:
    print(k)
