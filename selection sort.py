a1=[12,52,1,13,0]
for k in range(0,len(a1)):
    min = k
    for l in range(k+1,len(a1)):
        if a1[min] > a1[l]:
            min = l
    a1[k],a1[min]= a1[min],a1[k]

print(a1)