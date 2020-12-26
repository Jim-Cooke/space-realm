# star empire program
# import library with random function
# 
import random
import time
import math

player = ["XXX"]
turns = []
current_turn = 1
current_player = "XXX"

#my random function
def random_1 ():
    r = random.random()
    t = time.time()
    # print(r, " ", t)
    rs = r + t
    # print(rs)
    rs = rs - math.floor(rs)
    return rs


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


planet = [1]
for n in range (1, nop*wpp+1):
    planet.append(n)

class worlds :pass
for n in range (1, nop*wpp+1):
    planet[n] = worlds()
    if n <= nop:
        planet[n].owner = player[n]
    else:
        planet[n].owner = "XXX"
    planet[n].locx = int(random_1()*cube_side - cube_side/2)
    planet[n].locy = int(random_1()*cube_side - cube_side/2)
    planet[n].locz = int(random_1()*cube_side - cube_side/2)
    planet[n].res_prod = int(random_1()*2 + 1)
    planet[n].res = int(random_1()*2 + 1)
    if planet[n].owner != "XXX":
        planet[n].ap = int(random_1()*2 + 1)
        planet[n].pop = int(random_1()*2 + 1)
        planet[n].ind = int(random_1()*2 + 1)
        planet[n].ships = 5
    else:
        planet[n].ap = 0
        planet[n].pop = 0
        planet[n].ind = 0
        planet[n].ships = 0
    planet[n].ind_prod = min(planet[n].res, planet[n].pop, planet[n].ind)

#display worlds function
def display_wrld (worlds, num):
    print(" ")
    print("Wld  Ownr     X    Y    Z   Rp  Res A+P Pop Ind IP Sh")
    for n in range (1, num+1):
        pl_loc_line = '%4s %4s %4s' % (planet[n].locx, planet[n].locy, planet[n].locz)
        print(n, "  ", planet[n].owner, " ",pl_loc_line, " ", planet[n].res_prod, " ", planet[n].res, " ", planet[n].ap,
        " ", planet[n].pop, " ", planet[n].ind, " ", planet[n].ind_prod, " ", planet[n].ships) 

#call display worlds function
display_wrld(worlds, nop*wpp)

#fleets
fleet = [1]

#number of fleets    
nof = 1

class armada :pass
for n in range (0, nof):
    fleet[n] = armada()
    fleet[n].owner = "XXX"
    fleet[n].locx = 0
    fleet[n].locy = 0
    fleet[n].locz = 0
    fleet[n].dest_wrld = 0
    fleet[n].dest_x = 0
    fleet[n].dest_y = 0
    fleet[n].dest_z = 0
    fleet[n].ships = 0
    fleet[n].cargo = 0
    fleet[n].crg_type = "_"

#display fleets function
def display_flt (armada, nof):
    print(" ")
    print("Flt Ownr     X    Y    Z   Sh  Cargo")
    for n in range (0, nof):
        ft_loc_line = '%4s %4s %4s' % (fleet[n].locx, fleet[n].locy, fleet[n].locz)
        print(n, " ", fleet[n].owner, " ", ft_loc_line, " ", fleet[n].ships, " ", fleet[n].cargo, " ", fleet[n].crg_type)

#call display fleets function
display_flt(armada, nof)
    
