def moveTower(height,fromPole,toPole,withPole,array):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole,array)
        moveDisk(fromPole,toPole,array)
        moveTower(height-1,withPole,toPole,fromPole,array)

def moveDisk(fp,tp,array):
    array[['A','B','C'].index(fp)]-=1
    array[['A','B','C'].index(tp)]+=1
    print "moving disk from",fp,"to",tp,array


moveTower(6,"A","C","B",[6,0,0])
    
