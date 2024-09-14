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
            print(n, " ", fleet[n].owner, " ", ft_loc_line, " ", fleet[n].ships, " ", fleet[n].cargo, " ", fleet[n].crg_type, fleet[n].status, fleet[n].arr)

            
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



def distance(orig_x, orig_y, orig_z, dest_x, dest_y, dest_z):
    return math.sqrt((orig_x-dest_x)**2 + (orig_y-dest_y)**2 + (orig_z-dest_z)**2)

        
def travel_time(orig_x, orig_y, orig_z, dest_x, dest_y, dest_z):
    dist = distance(orig_x, orig_y, orig_z, dest_x, dest_y, dest_z)
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
                fleet.append(fl)
                fleet[fl] = armada()
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
        fleet[fl].dest_wrld = 0
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

# locations function
def locations(worlds, armada, pl, nof):
    # finds distances between worlds, fleets, locations
    # starting location
    loci = "x"
    while loci != "w" and loci != "f" and loci != "l":
        loci = input("Is the first location a world, fleet or location? Enter w, f or l")
        # location of a world
    if loci == "w":
        wi = 0
        while wi < 1 or wi > nop*wpp:
            wi = int(input("Enter world number"))
        xi = planet[wi].locx
        yi = planet[wi].locy
        zi = planet[wi].locz
        # location of a fleet
    if loci == "f":
        #print player's fleets
        print("Your Fleets")
        print("Number X Y Z")
        fl_counter = 0
        for i in range(0, nof):
            if fleet[i].owner == pl and fleet[i].status == "still":
                fl_counter = fl_counter + 1
                print(i, fleet[i].locx, fleet[i].locy, fleet[i].locz)
        if fl_counter == 0:
            print("You have no fleets")
            return
        else:
            fi = -1
            while fi < 0 or fi > nof-1 or fleet[i].owner != pl or fleet[i].status != "still":
                fi = input("Enter fleet number")
            xi = fleet[fi].locx
            yi = fleet[fi].locy
            zi = fleet[fi].locz
    # a location
    if loci == 'l':
        xi = int(input("Enter x co-ordinate of location"))
        yi = int(input("Enter y co-ordinate of location"))
        zi = int(input("Enter z co-ordinate of location"))
    # ending location
    locii = 'x'
    while locii != "w" and locii != "l":
        locii = input("Is the end location a world or location? Enter w or l")
    # location of a world
    if locii == "w":
        wi = 0
        while wi < 1 or wi > nop*wpp:
            wi = int(input("Enter world number"))
        xii = planet[wi].locx
        yii = planet[wi].locy
        zii = planet[wi].locz
    # a location
    if locii == 'l':
        xii = int(input("Enter x co-ordinate of location"))
        yii = int(input("Enter y co-ordinate of location"))
        zii = int(input("Enter z co-ordinate of location"))
#  calculate travel time
    tt = travel_time(xi, yi, zi, xii, yii, zii)
    print("Travel time is ", tt, "turns.")

        
               
    
#structure of game
#choose player, player takes turn
#   launching fleets puts events in table
#check for events
#    planet prod 
#    fleets land
#go back to choose player

end_game = "no"
while end_game != "yes":
    # advance time
    current_turn = current_turn + 1
    print("time advance")
    # fleets land
    for n in range (0, nof):
        # find fleets ending their flight
        if fleet[n].status == "infight" and fleet[n].arr < current_turn:
            # fleet stops at world or location
            if fleet[n].dest_wrld == 0:
                # stops at location
                fleet[n].locx = fleet[n].dest_x
                fleet[n].locy = fleet[n].dest_y
                fleet[n].locz = fleet[n].dest_z
                fleet[n].status = "still"
            else:
                # stops at world
                # is world owned by fleet's owner?
                bp = 0
                if planet[fleet[n].dest_wrld].owner != fleet[n].owner:
                    # planet owned by other player
                    if planet[fleet[n].dest_wrld].owner != "XXX":
                        # fight for planet
                        bp =  combat(fleet[n].ships, planet[fleet[n].dest_wrld].ships)
                        if bp > 0:
                            # invaders won battle
                            planet[fleet[n].dest_wrld].ships = bp
                        else:
                            # invaders lost
                            planet[fleet[n].dest_wrld].ships = bp * (-1)
                # if won battle or planet is unowned, or owned by fleet owner
                if bp >= 0:
                    #set ownership, unload cargo
                    planet[n].owner = fleet[n].owner
                    if fleet[n].crg_type == "ap":
                        planet[n].ap = planet[n].ap + fleet[n].cargo
                    if fleet[n].crg_type == "pop":
                        planet[n].pop = planet[n].pop + fleet[n].cargo
                    if fleet[n].crg_type == "ind":
                        planet[n].ind = planet[n].ind + fleet[n].cargo
                if bp == 0:
                    # there was no battle
                    planet[fleet[n].dest_wrld].ships = fleet[n].ships
                # fleet entry nulled out
                fleet[n].status = "null"
                fleet[n].ships = 0
                fleet[n].cargo = 0
                fleet[n].crg_type = "_"
    # planets produce
    for n6 in range (1, nop*wpp+1):
        if planet[n6].owner != "XXX":
            # animals and plants inrease?
            if planet[n6].ap * random_1() - planet[n6].ind * random_1() > 0:
                planet[n6].ap = planet[n6].ap + 1
                print("ap increase")
            # resource production changes?
            q6 = random_1()
            if q6 > 0.9:
                planet[n6].res_prod = planet[n6].res_prod + 1
            if q6 < 0.1:
                planet[n6].res_prod = planet[n6].res_prod - 1
            # resource production cannot be less than 1
            if planet[n6].res_prod < 1:
                planet[n6].res_prod = 1
            # resources increase
            planet[n6].res = planet[n6].res + planet[n6].res_prod
            print("resources increase")
            # population consumes resources, increases or decreases
            if planet[n6].res < planet[n6].pop:
                planet[n6].res = 0
                planet[n6].pop = planet[n6].pop - 1
            if planet[n6].res == planet[n6].pop:
                planet[n6].res = 0
            if planet[n6].res > planet[n6].pop:
               planet[n6].res = planet[n6].res - planet[n6].pop
               planet[n6].pop = planet[n6].pop + 1 + int(planet[n6].pop * random_1())
            # population cannot be les than 1
            if planet[n6].pop < 1:
                planet[n6].pop = 1
            planet[n6].ind_prod = min(planet[n6].res, planet[n6].pop, planet[n6].ind)
    # one planet moves
    print("planet moves")
    np = int(random_1() * nop) + 1
    nd = int(random_1() * 6)
    if nd == 0:
        planet[np].locx = planet[np].locx + 1
    elif nd == 1:
        planet[np].locx = planet[np].locx - 1
    elif nd == 2:
        planet[np].locy = planet[np].locy + 1
    elif nd == 3:
        planet[np].locy = planet[np].locy - 1
    elif nd == 4:
        planet[np].locz = planet[np].locz + 1
    elif nd == 5:
        planet[np].locz = planet[np].locz - 1
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
            print("Turn = ", current_turn)
            print("1.  End Turn")
            print("2.  Display worlds")
            print("3.  Display Fleets")
            print("4.  Build on worlds")
            print("5.  Send fleets")
            print("6.  Attack Fleet")
            print("7.  Travel time between locations")
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
                locations(worlds, armada, player[t_player], nof)
            #other choices call functions
            #test if planets are actually increasing resources, etc
                
       
                
             









    
