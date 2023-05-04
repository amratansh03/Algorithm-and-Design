a = {10,6,0,3,5,2,9,1}
s = len(a)
p=a[s-1]
for i in range(s):
    if p<a[i]: 
       p2 = a[i]
    for j in range(s):
        if p>a[j]:
           p3 = a[j]    
    a[i],a[j] = a[j],a[i]
print(a)