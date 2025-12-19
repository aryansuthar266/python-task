# Maximum of 3 (No Nested IF / No Logical OR)

a,b,c = map(int,input("Enter 3 nums: ").split())
maxi = a
if b > maxi: maxi = b
if c > maxi: maxi = c
print("Max =", maxi)