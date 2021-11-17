import random
def desk():
    desk=[]
    ranks =['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
    suits =['H','D','S','C']
    for rank in ranks:
        for suit in suits:
            desk.append([rank,suit])
    random.shuffle(desk)
    return(desk)
    
desk=desk() 
hand=desk[0:5]
print(hand)


  




