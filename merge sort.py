def Mergesort(array_right):
    if len(array_right) <= 1:
        return array_right
    mid = len(array_right) // 2
    array_left = array_right[:mid]
    array_right = array_right[mid:]
    
    left_sorted = Mergesort(array_left)
    right_sorted = Mergesort(array_right)
    
    Array = []
    i, j = 0, 0
    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] < right_sorted[j]:
            Array.append(left_sorted[i])
            i += 1
        else:
            Array.append(right_sorted[j])
            j += 1
    Array += left_sorted[i:]
    Array += right_sorted[j:]
    return Array

a = [23,7,0,10,8,1,2,3]
print(Mergesort(a))