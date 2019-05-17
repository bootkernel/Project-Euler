# Project Euler Problem 1
x = 999

div3 = x / 3
div5 = x / 5
sum0 = 0
sum1 = 0

for i in range (0, 1000, 3):
    print(i)
    sum0 += i
print(sum0)

sum1 = 0
for k in range (0, 1000, 5):
    print(k)
    sum1 += k
print(sum1)

sum2 = 0
for j in range (0, 1000, 15):
    print(j)
    sum2 += j
print(sum2)

total = sum0 + sum1 - sum2
print "Answer:", total
