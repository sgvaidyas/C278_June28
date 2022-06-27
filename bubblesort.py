l =[11,2,1,44,5]
n = len(l)
for i in range(n-1):
    for j in range(n-1-i):
        if l[j]>l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]

print(l)
