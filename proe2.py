# Project Euler Problem 2
x = 1
y = 1
z = 0
ans = 0

while z < 4000000:
   z = (x + y)         
   if z % 2 == 0:
       ans += z

   x = y
   y = z
   
print(ans)