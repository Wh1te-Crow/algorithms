def fibonacci(number):
        if (number==1):
                return [1]
        elif (number==2):
                return [1,1]
        elif ((number<0)or(number==0)):
                return "error number"
        else:
                array=[1,1,2,[1,1]]
                for index in range(2,number):
                        summa(array)
        return array[3]
'''
        The first two elements of the list are the last two numbers of the sequence,
        the fourth element of the list is the number of the last element of the sequence,
        the fourth element of the list is the entire sequence.
'''
def summa(array):
        temp=array[1]
        array[1]=temp+array[0]
        array[0]=temp
        array[2]+=1
        array[3].append(array[1])
        return([array])

print(fibonacci(3))
print(fibonacci(-10))
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(10))

