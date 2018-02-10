'''
#version without recursion
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
                        summation(array)
        return array[3]
'''
        #The first two elements of the list are the last two numbers of the sequence,
        #the fourth element of the list is the number of the last element of the sequence,
        #the fourth element of the list is the entire sequence.
'''
def summation(array):
        temp=array[1]
        array[1]=temp+array[0]
        array[0]=temp
        array[2]+=1
        array[3].append(array[1])
        return([array])
'''
def fibonacci(number):
        if number == 1 or number == 2:
                return 1
        else:
                return fibonacci(number-1)+fibonacci(number-2)

print(fibonacci(10))

