import random

def gen_keys(array):
    temp_key = int(random.uniform(-250,250))
    while ( temp_key in array ):
        temp_key = int(random.uniform(-250,250))
    return temp_key

class Tree():
    def __init__(self):
        self._body = {}
        self._body['root']={}
        key_left = gen_keys((self._body).keys())
        (self._body['root'])['left']=key_left
        key_right = gen_keys((self._body).keys())
        (self._body['root'])['right']=key_right
        self._body[key_left],self._body[key_right]={},{}
        (self._body['root'])['data'] = 'NULL'
        (self._body[key_left])['data'],(self._body[key_right])['data']='NULL','NULL'
        
        
    def add(self,element):
        if (self._body['root'])['data'] == 'NULL':
            (self._body['root'])['data'] = element
        else:
            temp='root'
            temp_hair='root'
            while( not (self._body[temp_hair])['data'] == 'NULL'):
                temp = temp_hair
                if (self._body[temp_hair])['data']>element:
                    temp_hair=(self._body[temp_hair])['left']
                else:
                    temp_hair=(self._body[temp_hair])['right']
            key_left = gen_keys((self._body).keys())
            self._body[temp_hair]={}
            (self._body[temp_hair])['parent'] = temp
            (self._body[temp_hair])['left']=key_left
            key_right = gen_keys((self._body).keys())
            (self._body[temp_hair])['right']=key_right
            self._body[key_left],self._body[key_right]={},{}
            (self._body[key_left])['data'],(self._body[key_right])['data']='NULL','NULL'
            (self._body[temp_hair])['data']=element

    def show(self):
        arr={}
        def print_tree(key,level,arr):
            if(not self._body[key]['data'] == 'NULL'):
                if not level in arr.keys():
                    arr[level]=[]
                arr[level]+=[(self._body[key]['data'])]
                print_tree(self._body[key]['left'],level+1,arr)
                print_tree(self._body[key]['right'],level+1,arr)
            else:
                if not level in arr.keys():
                    arr[level]=[]
                arr[level]+=['NULL']
        print_tree('root',0,arr)
        maximum = 0
        for index in arr.keys():
            if index > maximum:
                maximum = index    
        
        for index in range(0,maximum+1):
            for temp in range(0,len(arr[index])):
                              if arr[index][temp] == 'NULL' and (index+1) in arr.keys():
                                  arr[index+1]=arr[index+1][:temp+1]+['NULL','NULL']+arr[index+1][temp+1:]
            Temp=""
            for temp in arr[index]:
                Temp+=" "+str(temp)
            arr[index]=Temp
        const = len(arr[maximum])
        for index in range(0,maximum):
            Temp_len=const-len(arr[index])
            arr[index]=Temp_len//2*" "+arr[index]+Temp_len//2*" "
            print(arr[index])

            
    def number_of_words(self,element):
        number = {}
        number[element]=0
        def temp(element,number,key):
            if(not self._body[key]['data'] == 'NULL'):
                if(self._body[key]['data'][0] == element):
                    number[element]+=1
                temp(element,number,self._body[key]['left'])
                temp(element,number,self._body[key]['right'])                
            
        temp(element,number,'root')
        print("number:"+str(number[element]))

    def tree_without(self,element):
        clean_tree={}
        clean_tree[element]=[]
        def temp(element,clean_tree,key):
            if(not self._body[key]['data'] == 'NULL'):
                if( not self._body[key]['data'] == element):
                    clean_tree[element]+=[self._body[key]['data']]
                temp(element,clean_tree,self._body[key]['left'])
                temp(element,clean_tree,self._body[key]['right'])
        temp(element,clean_tree,'root')
        return clean_tree[element]  


tree = Tree()
with open("data_tree.txt") as file:
    array = [row.strip() for row in file]
for temp in array:
    tree.add(temp)

tree.show()
tree.number_of_words('g')
New_arr_for_tree=tree.tree_without('mama')

del tree
tree = Tree()
for temp in New_arr_for_tree:
    tree.add(temp)
tree.show()
