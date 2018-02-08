def insertion_sorting(array):
    for index in range(1,len(array)):
        sorting_part=array[0:index+1]
        unsorting_part=array[index+1:]
        temp=array[index]
        i=index-1
        while(((i>0 or i==0) and array[i]>temp)):
            sorting_part[i+1]=sorting_part[i]
            sorting_part[i]=temp
            i-=1
        array=sorting_part+unsorting_part
    return(array)

def bubble_sorting(array):
    indicator_of_change=1
    index_of_last_unsorted=len(array)
    while(indicator_of_change):
        indicator_of_change=0
        for index in range(0,index_of_last_unsorted-1):
            if (array[index]>array[index+1]):
                temp=array[index]
                array[index]=array[index+1]
                array[index+1]=temp
                indicator_of_change+=1
        index_of_last_unsorted-=1
    return array

def sorting_by_choice(array):
    sorting_array=[]
    while(len(array)>0):
        minimum = array[0]
        for index in range(1,len(array)):
            if minimum>array[index]:
                minimum=array[index]
        array.remove(minimum)
        sorting_array.append(minimum)
    return sorting_array
        
print(insertion_sorting([1,2,3,8,9,0,-1,-5,0]))
print(bubble_sorting([1,2,3,8,9,0,-1,-5,0]))
print(sorting_by_choice([1,2,3,8,9,0,-1,-5,0]))
