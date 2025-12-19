# Greatest of 3 (Nested IF)

a,b,c = map(int,input("Enter 3 numbers: ").split())
if a>b:
    if a>c: print("Greatest =",a)
    else: print("Greatest =",c)
else:
    if b>c: print("Greatest =",b)
    else: print("Greatest =",c)

