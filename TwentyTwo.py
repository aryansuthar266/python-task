#Factorial

n = int(input("Num: "))
f = 1
for i in range(1,n+1):
    f *= i
print("Factorial =", f)
