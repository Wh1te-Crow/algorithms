def moveTower(height,fromPole,toPole,withPole,array):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole,array)
        moveDisk(fromPole,toPole,array)
        moveTower(height-1,withPole,toPole,fromPole,array)

def moveDisk(fp,tp,array):
    if (fp=="A"):
        array[0]-=1
    elif (fp=="B"):
        array[1]-=1
    else:
        array[2]-=1
    if (tp=="A"):
        array[0]+=1
    elif (tp=="B"):
        array[1]+=1
    else:
        array[2]+=1    
    print("moving disk from",fp,"to",tp,array)


moveTower(5,"A","C","B",[5,0,0])
    
