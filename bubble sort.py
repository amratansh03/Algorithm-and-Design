a2 = [9,5,6,7,8,1]
for m in range(len(a2)):
    for n in range(len(a2)):
        if a2[m]< a2[n]:
            a2[n], a2[m] = a2[m],a2[n]
print(a2)