
def quickSort(array,array_change):
    LessWalls=[]
    MoreWalls=[]
    Wall=array[len(array)-1]
    array=array[0:len(array)-1]
    
    for current in array:
        if Wall >= current:
            array_change[0]+=1
            array_change[1]+=1
            LessWalls.append(current)
        else:
            MoreWalls.append(current)
            array_change[0]+=1
            array_change[1]+=1
    if len(LessWalls)>1:
        array_change[0]+=1
        LessWalls=quickSort(LessWalls,array_change)
    if len(MoreWalls)>1:
        array_change[0]+=1
        MoreWalls=quickSort(MoreWalls,array_change)
            
    array=LessWalls+[Wall]+MoreWalls
    #print array_change
    return array


def QuickSort(array,left,right):
    i=left
    j=right
    wall=array[(left+right)/2]
    while i<=j:
        while array[i]<wall:
            i+=1
        while array[j]>wall:
            j-=1
        if i<=j:
            temp= array[i]
            array[i]=array[j]
            array[j]=temp
            i+=1
            j-=1
    if left<j:
        array=QuickSort(array,left,j)
    if i<=right:
        array=QuickSort(array,i,right)
    return array

