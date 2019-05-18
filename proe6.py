n = 10

for k in range(1, 101):
    SquareSum = n*(n+1)/2
    SquareS = SquareSum ** 2
print(SquareS)

for i in range(1, 101):
    SquareSum = (n*(n+1)*(2*n+1))/6
print(SquareSum)


diff = SquareS - SquareSum
int(diff)
print(diff)