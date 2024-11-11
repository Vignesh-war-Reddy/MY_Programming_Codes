
n = int(input("enter a num"))

for i in range(2,n+1):
    if n%i == 0:
        break
if i == n:
    print("prime ")
else:
    print("not prim ")