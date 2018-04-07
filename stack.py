import random
# first part
class Array:
    def __init__(self):
        self._head=0
        self._tail=0
        self._array = []
        for i in range(0,10):
            (self._array).append('NULL')
    def show(self):
        print(self._array)
    def push(self,element):
        if(element[0]==0):
            if (self._head + self._tail)<10:
                self._array[self._head]= element[1]
                self._head+=1
            else:
                print('Stack overflow')
        else:
            if (self._head + self._tail)<10:                
                self._array[9-self._tail]= element[1]
                self._tail +=1
            else:
                print('Stack overflow')
    def pop(self,key):
        if(key==0):
            if(self._head>0):
                self._array[self._head-1]='NULL'
                self._head-=1
            else:
                print('Stack is empty')
        else:
            if(self._tail>0):
                #print(self._tail)
                self._array[(10-self._tail)]='NULL'
                self._tail-=1
            else:
                print('Stack is empty')
    def temp(self):
        print(str(self._head)+'---'+str(self._tail))
# second part
class steck:
    def __init__(self):
        self._dictionary={}
        self._number=0
    def push(self,element):
        if self._number > 0:
            '''
            key = int(random.uniform(-250,250)
            while((self._dictionary).has_key(key))
                key = int(random.uniform(-250,250)
            '''
            temp = self._dictionary['START']
            while((temp[1])in(self._dictionary).keys()):
                  temp = self._dictionary[temp[1]]
            key = int(random.uniform(-250,250))
            while(key in (self._dictionary).keys()):
                key = int(random.uniform(-250,250))
            self._dictionary[temp[1]]=[element,key]
            self._number+=1
        else:
            key = int(random.uniform(-250,250))
            self._dictionary['START']=[element,key]
            self._number+=1
    def show(self):
            print(self._dictionary)
    def print_as_list(self):

        key = 'START'
        while(key in (self._dictionary).keys()):

            print(str((self._dictionary[key])[0]))
            key = (self._dictionary[key])[1]
        if self._number ==0:
            print('Steck is empty')
    def pop(self):
        key = 'START'
        if self._number>1:
            for i in range(1,self._number):
                key = (self._dictionary[key])[1]
            temp = (self._dictionary)[key]
            del (self._dictionary)[key]
            self._number-=1
            return temp[0]
        elif self._number == 1:
            temp = (self._dictionary)[key]
            del (self._dictionary)['START']
            self._number-=1
            return temp[0]

# first part
'''
arr = Array()
arr.show()
arr.push([0,0])
arr.push([1,'ha-ha-ha'])
arr.show()
arr.push([0,4])

for i in range(0,8):
    arr.push([0,4])

#arr.temp()
arr.show()
for i in range(0,10):
    arr.pop(0)

arr.show()
for i in range(0,10):
    arr.push([1,'ha-ha-ha'])

arr.show()
for i in range(0,10):
    arr.pop(1)

arr.show()
'''
# second part

stack = steck()

string = "52*2+6/2-1/"

for i in string:
    if i == '-':
        stack.push(-stack.pop()+stack.pop())
    elif i == '+':
        stack.push(stack.pop()+stack.pop())
    elif i =='*':
        stack.push(stack.pop()*stack.pop())

    elif i == '/':
        temp1 = stack.pop()
        temp2 = stack.pop()
        stack.push(temp2/temp1)

    else:
        stack.push(int(i))

stack.print_as_list()
