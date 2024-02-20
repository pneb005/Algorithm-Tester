
def selectionSort(names):
    temp = names
    smallest = 0
    for i in range(len(temp)-1):
        if temp[i]<temp[smallest]:
            smallest = i
    
    for i in range(len(temp)):
        for x in range(len(temp)):
            if temp[i]<temp[x]:
                temp[i], temp[x] = temp[x], temp[i]
    
    return temp

temp = selectionSort(names)
        