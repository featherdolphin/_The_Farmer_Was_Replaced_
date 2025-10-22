#clear()
maxSize = get_world_size()
T = Entities.Tree
S = Entities.Sunflower
C = Entities.Carrot
K = Entities.Cactus
P = Entities.Pumpkin
G = Entities.Grass

harvestList = [
[G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G],#00
[G,G,K,G,K,G,K,G,K,G,K,G,K,G,K,G,K,G,K,G,K,G,K,G,K,G,K,G,K,G,K,G],#01
[G,K,G,K,G,K,G,K,G,K,G,K,G,K,G,K,G,K,G,K,G,K,G,K,G,K,G,K,G,K,G,G],#02
[G,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,G],#03
[G,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,G],#04
[G,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,G],#05
[G,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,G],#06
[G,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,G],#07
[G,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,G],#08
[G,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,C,K,G],#09
[G,T,T,T,T,S,T,S,T,S,T,S,T,S,T,S,T,S,T,T,S,T,S,T,S,T,S,T,T,T,T,G],#10
[G,T,T,T,T,S,T,S,T,S,T,S,T,S,T,S,T,S,T,T,S,T,S,T,S,T,S,T,T,T,T,G],#11
[G,T,T,T,T,S,T,S,T,S,T,S,T,S,T,S,T,S,T,T,S,T,S,T,S,T,S,T,T,T,T,G],#12
[G,T,T,T,T,S,T,S,T,S,T,S,T,S,T,S,T,S,T,T,S,T,S,T,S,T,S,T,T,T,T,G],#13
[G,T,T,T,T,S,T,S,T,S,T,S,T,S,T,S,T,S,T,T,S,T,S,T,S,T,S,T,T,T,T,G],#14
[G,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,G],#15
[G,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,G],#16
[G,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,G],#17
[G,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,G],#18
[G,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,G],#19
[G,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,G],#20
[G,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,G],#21
[G,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,G],#22
[G,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,G],#23
[G,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,S,G],#24
[G,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,G],#25
[G,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,G],#26
[G,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,G],#27
[G,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,P,G],#28
[G,T,K,T,K,T,K,T,K,T,K,T,K,T,K,T,K,T,K,T,K,T,K,T,K,T,K,T,K,T,K,G],#29
[G,K,T,K,T,K,T,K,T,K,T,K,T,K,T,K,T,K,T,K,T,K,T,K,T,K,T,K,T,K,T,G],#30
[G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G],#31
] 
tillRequiredPlant = [S,C,P,K]
pumkinCount = [0,0,0,0]
maxPumkinCount = 7
def harvestCarrotAndBush():
    global pumkinCount
    global maxPumkinCount
    x,y = get_pos_x(),get_pos_y()
    currentPlant = harvestList[x][y]
    
    if get_entity_type() != P:
        harvest()
    elif can_harvest():
        if y<=30:
            if x>14:
                pumkinCount[0] += 1
            else:
                pumkinCount[1] += 1
        else:
            if x>14:
                pumkinCount[2] += 1
            else:
                pumkinCount[3] += 1
            
        if y<=30:
            if x>14 and pumkinCount[0] == maxPumkinCount:
                harvest()
                pumkinCount[0] = 0
            elif pumkinCount[1] == maxPumkinCount:
                harvest()
                pumkinCount[1] = 0
        elif y<=30:
            if x>14 and pumkinCount[2] == maxPumkinCount:
                harvest()
                pumkinCount[2] = 0
            elif pumkinCount[3] == maxPumkinCount:
                harvest()
                pumkinCount[3] = 0
                
    if currentPlant in tillRequiredPlant and get_ground_type() == Grounds.Grassland:
        till()
    if currentPlant != G and get_entity_type() != P:
        plant(currentPlant)
        use_item(Items.Water)
        #use_item(Items.Fertilizer)
        
def moveZigZag(size):
    global pumkinCount
    for row in range(size):
        if get_pos_x() % 2 == 0:
            for col in range(size):
                harvestCarrotAndBush()
                if(get_pos_y() < size-1):
                    move(North)
                
                if(col == size-1):
                    move(East)
                    
        else:
            for col in range(size):
                harvestCarrotAndBush()
                if(get_pos_y() >= 1):
                    move(South)
                if(col == size-1):
                    move(East)
    
    pumkinCount = [0,0,0,0]
    harvestCarrotAndBush()

while True:
    moveZigZag(maxSize)
