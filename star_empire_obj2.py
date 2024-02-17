# star empire program
# import library with random function
# 
import random
import time
import math

player = ["XXX"]
turns = [0]
current_turn = 1
t_player = 0

#my random function
def random_1():
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


#fleets
fleet = [1]

#number of fleets    
nof = 1

class armada :pass
fleet[0] = armada()
fleet[0].owner = "XXX"
fleet[0].locx = 0
fleet[0].locy = 0
fleet[0].locz = 0
fleet[0].dest_wrld = 0
fleet[0].dest_x = 0
fleet[0].dest_y = 0
fleet[0].dest_z = 0
fleet[0].ships = 0
fleet[0].cargo = 0
fleet[0].crg_type = "_"
#crg_type - ap, pop, ind
fleet[0].status = "null"
# status - null, inflight, still
fleet[0].arr = 0
# arr - arrival time


#local fleets function - 
#returns true if player has fleet in location x y z
def local_fleet(armada, lf_player, nof, x, y, z):
    fl = 0
    while fl < nof:
        if fleet[fl].owner == lf_player:
            if x == fleet[fl].locx and y == fleet[fl].locy and z == fleet[fl].locz:
                return True
        fl=fl+1

#local planets function - 
#returns true if current player has a planet in same location x y z
def local_planet(worlds, n_of_w, lp_player, x, y, z):
    for p in range (1, n_of_w+1):
        if planet[p].owner == lp_player:
            if x == planet[p].locx and y == planet[p].locy and z == planet[p].locz:
                return True

#display fleets function - display fleet if you own it, it is at one of your planets, or at one of your fleets
def display_flt(armada, worlds, nof, num, df_player):
    print(" ")
    print("Flt Ownr     X    Y    Z   Sh  Cargo")
    for n in range (0, nof):
        ft_loc_line = '%4s %4s %4s' % (fleet[n].locx, fleet[n].locy, fleet[n].locz)
        if df_player == fleet[n].owner or local_fleet(armada, df_player, nof, fleet[n].locx, fleet[n].locy, fleet[n].locz) or \
        local_planet(worlds, num, df_player, fleet[n].locx, fleet[n].locy, fleet[n].locz): 
            print(n, " ", fleet[n].owner, " ", ft_loc_line, " ", fleet[n].ships, " ", fleet[n].cargo, " ", fleet[n].crg_type)

            
#display worlds function
# you can see a world if it is in the same location as one of your worlds or fleets
def display_wrld(armada, worlds, num, dw_player, nof):
    print(" ")
    print("Wld  Ownr     X    Y    Z   Rp  Res A+P Pop Ind IP Sh")
    for n in range (1, num+1):
        #
        #print (n)
        #
        pl_loc_line = '%4s %4s %4s' % (planet[n].locx, planet[n].locy, planet[n].locz)
        #print(n, "  ", planet[n].owner, " ",pl_loc_line, " ", planet[n].res_prod, " ", planet[n].res, " ", planet[n].ap,\
        #" ", planet[n].pop, " ", planet[n].ind, " ", planet[n].ind_prod, " ", planet[n].ships)
        pr_kn_wo_prd = '%3s %3s %3s %3s' % (planet[n].res_prod, planet[n].res, planet[n].ap, planet[n].pop)
        pr_kn_wo_ind = '%3s %3s %3s' % (planet[n].ind, planet[n].ind_prod, planet[n].ships)
        if planet[n].owner == dw_player or local_fleet(armada, dw_player, nof, planet[n].locx, planet[n].locy, planet[n].locz) or \
        local_planet(worlds, num, dw_player, planet[n].locx, planet[n].locy, planet[n].locz):
            print(n, "  ", planet[n].owner, " ",pl_loc_line, pr_kn_wo_prd, pr_kn_wo_ind)
        else:
            print(n, "  ", planet[n].owner, " ",pl_loc_line)

#build on worlds function
def build(worlds, num, player):
    p = int(input("Which world?"))
    if planet[p].owner == player:
        #  build things
        print("What to build?")
        print("1.  Ships")
        print("2.  Industries")
        print("3.  Animals + Plants")
        th = int(input())
        n = int(input("How many?"))
        if n > planet[p].ind_prod:
            print("Not enough industrial production.")
        else:
            planet[p].ind_prod = planet[p].ind_prod - n
            planet[p].res = planet[p].res - n
            # print("choice=", th)
            if th == 1:
                planet[p].ships = planet[p].ships + n
            if th == 2:
                planet[p].ind = planet[p].ind + n
            if th == 3:
                planet[p].ap = planet[p].ap + n
    else:
        print("You don't own that planet")

        
def travel_time(orig_x, orig_y, orig_z, dest_x, dest_y, dest_z):
    dist = math.sqrt((orig_x-dest_x)**2 + (orig_y-dest_y)**2 + (orig_z-dest_z)**2)
    return 2 * math.sqrt(dist)

def which_fleet(guy, armada, nof):
#must own fleet and it must be at rest
    fleet_ok = "no"    
    while fleet_ok != "yes":
        fl = int(input("What fleet to use? Enter -1 to not select any fleet"))
        fleet_ok = "yes"
        if fl >= nof or fl < 0:
            fleet_ok = "no"
        if fl == -1:
            return
        if fleet[fl].owner != guy or fleet[fl].status != "still":
            fleet_ok = "no"
            print("That fleet is not available")
    return fl

#send_fleet function
def send_fleet(worlds, planets, guy, armada, nof, current_turn):
    # fl is fleet number and d_pl is destination planet s_pl start planet
    # send existing fleet or create new one?
    ch = "x"
    while ch != "e" and ch != "n":
        ch = input("Enter e for existing fleet or n for new fleet")
    #existing fleet
    if ch == "e":   
        # make sure fleet exists and is owned by player and is still
        # which fleet?
        fl = which_fleet(guy, armada, nof)
        # if fleet not selected drop out of function
        if fl == -1:
            return
    #new fleet
    # find or create fleet table entry
    if ch == "n":  
        fl = 0
        while fl <= nof:
            if fl == nof:
            # all fleet entries were used
                fleet.append[fl]
                nof = nof + 1
                break
            if fleet[fl].status == "null":
                break
            fl = fl +1
        # create fleet
        fleet[fl].owner = guy
        s_pl = int(input("what planet to start from?"))
        while planet[s_pl].owner != guy:
            s_pl = int(input("what planet to start from? Enter -1 to not select a planet"))
            if s_pl == -1:
                return
        #if planet not selected drop out of function
        #fleet location is location of starting planet
        fleet[fl].locx = planet[s_pl].locx
        fleet[fl].locy = planet[s_pl].locy
        fleet[fl].locz = planet[s_pl].locz
        # ships
        while True:
            fleet[fl].ships = int(input("How many ships?"))
            if fleet[fl].ships > 0 and fleet[fl].ships <= planet[s_pl].ships:
                break
        planet[s_pl].ships = planet[s_pl].ships - fleet[fl].ships
        if planet[s_pl].ships == 0:
            planet[s_pl].owner = "XXX"
            print("You no longer own planet ", a_pl)
        #cargo
        #whether to carry cargo or not
        fleet[fl].crg_type = "_"
        fleet[fl].cargo = 0
        cargo_yn = "x"
        while cargo_yn != "y" and cargo_yn != "n":
            cargo_yn = input("Will there be cargo? Enter y or n")
        # find cargo type and amount
        while cargo_yn == "y":
            # cargo type
            while fleet[fl].crg_type != "ap" and fleet[fl].crg_type != "pop" and fleet[fl].crg_type != "ind":
                fleet[fl].crg_type = input("Enter cargo type: ap, pop, ind")
            #cargo amt
            fleet[fl].cargo = int(input("Amount of cargo?"))
            if fleet[fl].cargo == 0:
                fleet[fl].crg_type = "_"
                break
            if fleet[fl].cargo < 0:
                print("Incorrect amount")
                continue
            # enough?                
            if fleet[fl].crg_type == "ap":
                if fleet[fl].cargo <= planet[s_pl].ap:
                    planet[s_pl].ap =  planet[s_pl].ap - fleet[fl].cargo
                    break
                else:
                    print("Not enough on the planet")
                    continue              
            if fleet[fl].crg_type == "pop":
                if fleet[fl].cargo <= planet[s_pl].pop:
                    planet[s_pl].pop =  planet[s_pl].pop - fleet[fl].cargo
                    break
                else:
                    print("Not enough on the planet")
                    continue                         
            if fleet[fl].crg_type == "ind":                     
                if fleet[fl].cargo <= planet[s_pl].ind:
                    planet[s_pl].ind =  planet[s_pl].ind - fleet[fl].cargo
                    break
                else:
                    print("Not enough on the planet")
                    continue
    #destination
    # planet or location?
    dest = "x"
    while dest != "p" and dest != "l":
        dest = input("Is destination a planet or a location? p or l")
    if dest == "p":
        #create entry for planet
        d_pl = -1
        while d_pl < 1 or d_pl > nop*wpp:
            d_pl = int(input("Enter destination planet"))
        fleet[fl].dest_wrld = d_pl
        fleet[fl].dest_x = planet[d_pl].locx
        fleet[fl].dest_y = planet[d_pl].locy
        fleet[fl].dest_z = planet[d_pl].locz
    if dest == "l":
    #create entry for location
        fleet[fl].dest_x = int(input("Enter destination x co-ordinate"))
        fleet[fl].dest_y = int(input("Enter destination y co-ordinate"))
        fleet[fl].dest_z = int(input("Enter destination z co-ordinate"))     
    #calculate arrival time
    tt = travel_time(fleet[fl].locx, fleet[fl].locy, fleet[fl].locz, fleet[fl].dest_x, fleet[fl].dest_y, fleet[fl].dest_z)
    fleet[fl].arr = current_turn + tt
    # fleet status
    fleet[fl].status = "inflight"

#firing function
def firing(firer, target, limit):
    # firer shoots up to their number or limit or until target forces eliminated
    n = 1
    while n <= firer and n <= limit:
        if random_1() > 0.5:
            target = target - 1
        if target <= 0:
            break
        n = n + 1
    return target
                       

#combat function
def combat(atts, defs):
# if attackers win returns number of surviving attackers
# if defenders win returns negative value of surviving defenders
    limit = 1
    while True:
        # defenders fire
        atts = firing(defs, atts, limit)
        if atts <= 0:
            return (-1) * defs
        limit = limit * 2
        # attackers fire
        defs = firing(atts, defs, limit)
        if defs <= 0:
            return atts
        limit = limit * 2
    

#attack function
def attack(guy, armada, nof):
    #which fleet
    a_fl = which_fleet(guy, armada, nof)
    # if fleet not selected drop out of function
    if a_fl == -1:
        return
    print("If you wish to attack a planet, send your fleet to it")
    # find if there is a fleet in the same location as your fleet
    print("Fleets you may attack:")
    n_fleets = 0
    for n in range (0, nof):
        if fleet[n].locx == fleet[a_fl].locx and fleet[n].locy == fleet[a_fl].locy and fleet[n].locz == fleet[a_fl].locz and \
        fleet[n].status == "still" and fleet[n].owner != guy:
            print("fleet ", n, " ", fleet[n].ships, " ships")
            n_fleets = n_fleets + 1
    if n_fleets == 0:
        print("There are no fleets to attack")
        return
    else:
        # there are valid fleets, choose one
        fleet_ok = "no"    
        while fleet_ok != "yes":
            fl = int(input("What fleet to attack? Enter -1 to not attack"))
            if fl >= nof or fl < 0:
                fleet_ok = "no"
            if fl == -1:
                return
            if fleet[d_fl].locx == fleet[a_fl].locx and fleet[d_fl].locy == fleet[a_fl].locy and fleet[d_fl].locz == fleet[a_fl].locz and \
            fleet[d_fl].status == "still" and fleet[d_fl].owner != guy:
                fleet_ok = "yes"
            if fleet_ok == "no":
                print("That fleet is not available")
        # call combat function
        c_outcome = combat(fleet[a_fl].ships, fleet[d_fl].ships)
        if c_outcome > 0:
            fleet[a_fl].ships = c_outcome
            fleet[d_fl].status = "null"
            print("The attacker won!")
        if c_outcome < 0:
            fleet[d_fl].ships = c_outcome * (-1)
            fleet[a_fl].status = "mull"
            print("The defender won!")           

# distances function
def distances(worlds, armada):
    # finds distances between worlds, fleets, locations
    
                          
#events
event = [1]
for n in range (1, nop*wpp+1):
    event.append(n)

#number of events
noe = nop*wpp

#events - planet production "prod", fleet arrives "arr"
#time = -1 means unused event
# planet or fleet number
class turns :pass
#seed event table with planet production events
for n in range (1, noe+1):
    event[n] = turns()
    event[n].time = 1 + 2*random_1()
    event[n].type = "prod"
    event[n].number = n
    
#structure of game
#choose player, player takes turn
#   launching fleets puts events in table
#move clock ahead random time 0-2 turns
#check for events
#    planet prod spawns new prod event 1 turn later
#    fleets land
#go back to choose player

end_game = "no"
while end_game != "yes":
    #choose new player
    pl = 1 + int(nop * random_1())
    if pl != t_player:
        t_player = pl
    else:
        least_turns = current_turn + 1
        least_pl = 1
        for n in range (1, nop+1):
            if turns[n] < least_turns:
                least_turns = turns[n]
                least_pl = n
        t_player = least_pl
    # menu
    ch = 0
    while ch != 1 and ch != 2:
        print("Player", player[t_player], "take your turn.")
        print("1.  End Game")
        print("2.  Take your turn")
        ch = int(input("Enter a number"))
        print(ch)
    if ch == 1:
        end_game = 'yes'
    else:
        ch2 = 0
        while ch2 != 1:
            print("1.  End Turn")
            print("2.  Display worlds")
            print("3.  Display Fleets")
            print("4.  Build on worlds")
            print("5.  Send fleets")
            print("6.  Attack Fleet")
            print("7.  Distances to worlds")
            ch2 = int(input("Enter a number"))
            if ch2 == 2:
                display_wrld(armada, worlds, nop*wpp, player[t_player], nof)
            if ch2 == 3:
                display_flt(armada, worlds, nof, nop*wpp, player[t_player])
            if ch2 == 4:
                build(worlds, nop*wpp, player[t_player])
            if ch2 == 5:
                send_fleet(worlds, nop*wpp, player[t_player], armada, nof, current_turn)
            if ch2 == 6:
                attack(player[t_tplayer], armada, nof)
            if ch2 == 7:
                distances(worlds, armada)
            #other choices call functions
        #check event table, process events
             









    
