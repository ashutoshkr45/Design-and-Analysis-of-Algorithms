def Merge(a=[],b=[]):
    c = []
    i = 0
    j = 0
    
    while(i<len(a) and j<len(b)):
        if(a[i] < b[j]):
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    while(i<len(a)):
        c.append(a[i])
        i += 1

    while(j<len(b)):
        c.append(b[j])
        j += 1

    return c

# a = [5,8,10,19,21]
# b = [2,5,7,15]

# print("Merged Array is--",Merge(a,b))