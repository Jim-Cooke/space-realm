# star empire program
# import library with random function
import random
import time
import math

player = ["X  "]
turns = []

# object
class Worlds:
    def __init__(self, wrld_num, owner, loc_x, loc_y, loc_z, res_prd, res, ap, pop, ind,
                 ind_prd, ships)
    self.wrld_num = wrld_num
    self.owner = owner
    self.loc_x = loc_x
    self.loc_y = loc_y
    self.loc_z = loc_z
    self.res_prd = res_prd
    self.res = res
    self.ap = ap
    self.pop = pop
    self.ind = ind
    self.ind_prd = ind_prd
    self.ships = ships


#my random function
def random_1 ():
    r = random.random()
    t = time.time()
    # print(r, " ", t)
    rs = r + t
    # print(rs)
    rs = rs - math.floor(rs)
    return rs

# print(random_1())


# generate worlds
# prompt for user imput
nop = int(input("How many players?"))
#  print(nop)
wpp = int(input("How many worlds per player?"))

# enter player names
for n in range(1, nop + 1):
    print("Three-letter name of player ", n, "?")
    # name = input()
    player.append(input())
    turns.append(0)
    # print(player[n])
    
#  find size of cube containing worlds 
cube_side = (nop*wpp*27)**(1./3.)

# code to generate instances
# def create_instance(class_name,instance_name):
#    count = 0
#    while True:
#        name = instance_name + str(count)
#        globals()[name] = class_name()
#        count += 1
#        print('Class instance: {}'.format(name))
#        yield True
#
#generator_instance = create_instance(Foo,'instance_') 
#
#for i in range(5):
#    next(generator_instance)

# another example of creating instances                                
# Python3 code here creating class 
#class geeks:  
#    def __init__(self, name, roll):  
#        self.name = name  
#        self.roll = roll 
   
# creating list        
list = []  
  
# appending instances to list  
#list.append( geeks('Akash', 2) ) 
#list.append( geeks('Deependra', 40) ) 
#list.append( geeks('Reaper', 44) )

#generate owners
def gen_own (x):
    global player[]
    global nop
    if x <= nop:
        return player[x]
    else:
        return "X  "

#generate locations
def gen_loc ():
    global cube_side
    return int(random_1()*cube_side - cube_side/2)

#generate resource production
def gen_rprd ():
    return int(random_1()*2 + 1)

#generate resources
def gen_res ():
    return int(random_1()*2 + 1)

#generate animals-plants
def gen_ap (x):
    global owner[]
    if owner[x] != "X  ":
        return int(random_1()*2 + 1)
    else:
        return 0
    

for n in range(0, wpp*nop):
    list.append( Worlds(n, gen_own(n), gen_loc(), gen_loc(), gen_loc(), gen_rprd(), gen_res(), gen_ap(n),
                        gen_pop(n), gen_ind(n), gen_indprd(n), gen_ships(n) )
                                

#print("Wld  Ownr    X     Y     Z  Rp  Res  A+P  Pop  Ind  IP  Sh")
# generate worlds - non OOP method
for n in range(0, wpp*nop):
    if n <= nop:
        owner.append(player[n])
    else:
        owner.append("X  ")
    loc_x.append(int(random_1()*cube_side - cube_side/2))
    loc_y.append(int(random_1()*cube_side - cube_side/2))
    loc_z.append(int(random_1()*cube_side - cube_side/2))
    res_prod.append(int(random_1()*2 + 1))
    res.append(int(random_1()*2 + 1))
    if owner[n] != "X  ":
        ap.append(int(random_1()*2 + 1))
        pop.append(int(random_1()*2 + 1))
        ind.append(int(random_1()*2 + 1))
        ships.append(5)
    else:
        ap.append(0)
        pop.append(0)
        ind.append(0)
        ships.append(0)
    ind_prod.append(min(res[n], pop[n], ind[n ]))
    #print(n, "  ", owner[n], " ", "{0:3d} : {1:3d} : {2:3d}".format(loc_x[n], loc_y[n], loc_z[n]), " " , res_prod[n],
    #      " ", res[n], "  ", ap[n], "  ", pop[n], "  ", ind[n], "  ", ind_prod[n], " ", ships[n])

#main turn menu
quit = "no"
prev_p = int(nop * random_1())
turn = 1
while quit != "yes":
    # choose next player
    crrnt_p = int(nop * random_1())
    if crrnt_p == prev_p:
        #find player whose had least turns
        least_t = turn
        for i in range(0, nop):
            if turns[i] <= least_t AND i != prev_p:
            least_t = turns[i]
            crrnt_p = i
                
            


    
        
    


