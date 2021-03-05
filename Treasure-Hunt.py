#########################
#########################
# THE START OF MY CODE  #
#########################
#########################
import os
import random # Importing the ability to randomise
import time # Importing the ability to manipulae the time in the code
txp = 0 # The x postiion (variable name)
typ = 0 # The y postiion (variable name)
seq = [0,1,2,3,4,5,6,7]# A list of the numbers 0-7
tx = []# Treasure x  /  list for storing chest's X co-ordinates
ty = []# Treasure y  /  list for storing chest's Y co-ordinates
bx = []# Bandits x  /  list for storing Bandits's X co-ordinates
by = []# Bandits y  /  list for storing Bandits's Y co-ordinates
pxc = []# Players x co-ordinates
pyc = []# Players y co-ordinates
c = 10 # Number of chests
b = 5 # Number of bandits
totalmapcoins = 300
Grid = [[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "]]
# An 8x8 list of lists
GridCB = [[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "]]
# An 8x8 list of lists
def Map(b,c):
    ############################################################################ 
    # A ascii grid for the player to spawn, with list co-ordinates
    # And the number of chest's and bandits printed on the edges
    ############################################################################
    print('\n╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗')
    print('║',Grid[7][0],"║",Grid[7][1],"║",Grid[7][2],"║",Grid[7][3],"║",Grid[7][4],"║",Grid[7][5],"║",Grid[7][6],"║",Grid[7][7],"║")
    print('╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣ ╔═══════════════╗')
    print('║',Grid[6][0],"║",Grid[6][1],"║",Grid[6][2],"║",Grid[6][3],"║",Grid[6][4],"║",Grid[6][5],"║",Grid[6][6],"║",Grid[6][7],"║", '║ Chests =', c,'  ║')
    print('╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣ ╠═══════════════╣')
    print('║',Grid[5][0],"║",Grid[5][1],"║",Grid[5][2],"║",Grid[5][3],"║",Grid[5][4],"║",Grid[5][5],"║",Grid[5][6],"║",Grid[5][7],"║", '║ Bandits =', b,'  ║')
    print('╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣ ╠═══════════════╩════════╗')
    print('║',Grid[4][0],"║",Grid[4][1],"║",Grid[4][2],"║",Grid[4][3],"║",Grid[4][4],"║",Grid[4][5],"║",Grid[4][6],"║",Grid[4][7],"║", '║ Total Map Coins =', totalmapcoins,' ║')
    print('╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣ ╚════════════════════════╝')
    print('║',Grid[3][0],"║",Grid[3][1],"║",Grid[3][2],"║",Grid[3][3],"║",Grid[3][4],"║",Grid[3][5],"║",Grid[3][6],"║",Grid[3][7],"║")
    print('╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣')
    print('║',Grid[2][0],"║",Grid[2][1],"║",Grid[2][2],"║",Grid[2][3],"║",Grid[2][4],"║",Grid[2][5],"║",Grid[2][6],"║",Grid[2][7],"║")
    print('╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣')
    print('║',Grid[1][0],"║",Grid[1][1],"║",Grid[1][2],"║",Grid[1][3],"║",Grid[1][4],"║",Grid[1][5],"║",Grid[1][6],"║",Grid[1][7],"║")
    print('╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣')
    print('║',Grid[0][0],"║",Grid[0][1],"║",Grid[0][2],"║",Grid[0][3],"║",Grid[0][4],"║",Grid[0][5],"║",Grid[0][6],"║",Grid[0][7],"║")
    print('╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝\n')

def MapCB():
    ################################################################################## 
    # The same Thing with a different co-ordinates, but to spawn chests and bandits
    ##################################################################################
    print('\n---------------------------------')
    print('║',GridCB[7][0],"║",GridCB[7][1],"║",GridCB[7][2],"║",GridCB[7][3],"║",GridCB[7][4],"║",GridCB[7][5],"║",GridCB[7][6],"║",GridCB[7][7],"║")
    print('---------------------------------')
    print('║',GridCB[6][0],"║",GridCB[6][1],"║",GridCB[6][2],"║",GridCB[6][3],"║",GridCB[6][4],"║",GridCB[6][5],"║",GridCB[6][6],"║",GridCB[6][7],"║")
    print('---------------------------------')
    print('║',GridCB[5][0],"║",GridCB[5][1],"║",GridCB[5][2],"║",GridCB[5][3],"║",GridCB[5][4],"║",GridCB[5][5],"║",GridCB[5][6],"║",GridCB[5][7],"║")
    print('---------------------------------')
    print('║',GridCB[4][0],"║",GridCB[4][1],"║",GridCB[4][2],"║",GridCB[4][3],"║",GridCB[4][4],"║",GridCB[4][5],"║",GridCB[4][6],"║",GridCB[4][7],"║")
    print('---------------------------------')
    print('║',GridCB[3][0],"║",GridCB[3][1],"║",GridCB[3][2],"║",GridCB[3][3],"║",GridCB[3][4],"║",GridCB[3][5],"║",GridCB[3][6],"║",GridCB[3][7],"║")
    print('---------------------------------')
    print('║',GridCB[2][0],"║",GridCB[2][1],"║",GridCB[2][2],"║",GridCB[2][3],"║",GridCB[2][4],"║",GridCB[2][5],"║",GridCB[2][6],"║",GridCB[2][7],"║")
    print('---------------------------------')
    print('║',GridCB[1][0],"║",GridCB[1][1],"║",GridCB[1][2],"║",GridCB[1][3],"║",GridCB[1][4],"║",GridCB[1][5],"║",GridCB[1][6],"║",GridCB[1][7],"║")
    print('---------------------------------')
    print('║',GridCB[0][0],"║",GridCB[0][1],"║",GridCB[0][2],"║",GridCB[0][3],"║",GridCB[0][4],"║",GridCB[0][5],"║",GridCB[0][6],"║",GridCB[0][7],"║")
    print('---------------------------------\n')

def gridreset(Grid):
    ########################## 
    # Makes all of the Players Grid co-ordinates blank
    ########################## 
    for d in range(7):
        for e in range(7):
            Grid[d][e] = ' '

def gridreset2():
    ########################## 
    # Makes all of the Chest and Bandits Grid co-ordinates blank
    ########################## 
    for d in range(7):
        for e in range(7):
            GridCB[d][e] = ' '

def UserInt(message):
    ########################## 
    # A function that loops
    # A try and except for any intiger input, with a custom message
    ########################## 
    while True:
        try:
            UserinputInt = int(input(message))
            return UserinputInt
        except:
            print("This input is not valid, try again\n")
        
def Gameplay(playericon):
    global UorD
    global RorL
    global height
    global width
    height = 8
    width = 8
    ##########################    
    # txp and typ start at 0
    # Then Grid[txp(aka 0)][typ(aka 0)] is set o blank but the player doesn't see this until he Grid is reprinted
    # UorD is a str input, this is the matched with all of these if statement
    # if one of these if statements is true then it will add a certain number to the variable 'txp'
    # Next is the same code for left and righ movement and the number is added to the variable 'typ'
    # Then The variables are put into Grid positions
    # E.G if txp and typ = 3 then Grid[3][3], the playericon is printed onto these new co-ordinates
    # Then the Grid is printed and the txp and typ variables are updated so on the next turn, they will equal what they did on the turn prior
    ##########################
    global txp #globalising the x position
    global typ #globalising the y position
    Grid[txp][typ] = ' '
    while True:
        UorD = str(input('How far up or down would you like to move\ne.g u1 = up 1 space and d1 = down 1 space: '))           
        if txp < height:
            if UorD == 'u0':
                txp += 0   #the x position (variable name)
                break
            elif UorD == 'u1':
                txp += 1
                height -= txp
                break
            elif UorD == 'u2':
                txp += 2
                height -= txp
                break
            elif UorD == 'u3':
                txp += 3
                break
            elif UorD == 'u4':
                txp += 4
                height -= txp
                break
            elif UorD == 'u5':
                txp += 5
                height -= txp
                break
            elif UorD == 'u6':
                txp += 6
                height -= txp
                break
            elif UorD == 'u7':
                txp += 7
                height -= txp
                break
            if UorD == 'd0':
                txp += 0
                height -= txp
                break
            elif UorD == 'd1':
                txp -= 1
                height += txp
                break
            elif UorD == 'd2':
                txp -= 2
                height += txp
                break
            elif UorD == 'd3':
                txp -= 3
                height += txp
                break
            elif UorD == 'd4':
                txp -= 4
                height += txp
                break
            elif UorD == 'd5':
                txp -= 5
                height += txp
                break
            elif UorD == 'd6':
                txp -= 6
                height += txp
                break
            elif UorD == 'd7':
                txp -= 7
                height += txp
                break
            else:
                print("\nThis input is not valid, try again\n")
        else:
            print('INVALID')
    while True:
        RorL = str(input('\nHow far right or left would you like to move\ne.g r1 = right 1 space and l1 = left 1 space: '))
        if typ < width:
            if RorL == 'r0':
                typ += 0
                width -= typ
                break
            elif RorL == 'r1':
                typ += 1
                width -= typ
                break
            elif RorL == 'r2':
                typ += 2
                width -= typ
                break
            elif RorL == 'r3':
                typ += 3
                width -= typ
                break
            elif RorL == 'r4':
                typ += 4
                width -= typ
                break
            elif RorL == 'r5':
                typ += 5
                width -= typ
                break
            elif RorL == 'r6':
                typ += 6
                width -= typ
                break
            elif RorL == 'r7':
                typ += 7
                width -= typ
                break
            elif RorL == 'l0':
                typ += 0
                width -= typ
                break
            elif RorL == 'l1':
                typ -= 1
                width += typ
                break
            elif RorL == 'l2':
                typ -= 2
                width += typ
                break
            elif RorL == 'l3':
                typ -= 3
                width += typ
                break
            elif RorL == 'l4':
                typ -= 4
                width += typ
                break
            elif RorL == 'l5':
                typ -= 5
                width += typ
                break
            elif RorL == 'l6':
                typ -= 6
                width += typ
                break
            elif RorL == 'l7':
                typ -= 7
                width += typ
                break
            else:
                print("\nThis input is not valid, try again\n")
        else:
            print('INVALID')
    Grid[txp][typ] = playericon
    Map(b,c)
    return txp, typ
def AImove():
    AIx = 7
    AIy = 7
    Grid[AIx][AIy] = ' '
    AIx = random.choice(seq)
    AIy = random.choice(seq)
    Grid[AIx][AIy] = enemy
    
def chests():
    ############################################################################################################################################################
    # Enters for loop
    # A boolean variable is created and set to False
    # While this equals False
    # 2 random numbers are selected from my list of number 0-7 and are assigned to two different variables (CCx and CCy)
    # These are then placed as Grid co-ordinates E.G GridCB[CCx][CCy] (this is all done on the Chest and bandits grid)
    # Then if this co-ordinate is blank, then make sure that it isn't the players start co-ordinate (aka 0,0) and then print a 'T' onto these co-ordinates
    # Then add the first variable to the list 'tx' and the second to 'ty' (these represent the co-ordinates of the Chest stored into 2 seperate lists)
    # Then return the boolean variable as True an the Loop starts all over again
    # It loops for 10 times as that is how many Chest are in the Game
    ############################################################################################################################################################
    for chests in range(10):
        ValidCrd = False
        while ValidCrd == False:
            CCx = random.choice(seq)#Chest co-ordinate x (variable name)
            CCy = random.choice(seq)#Chest co-ordinate y (variable name)
            if GridCB[CCx][CCy] == " ":
                GridCB[0][0] != 'T'
                GridCB[CCx][CCy] = 'T'
                tx.append(CCx)
                ty.append(CCy)
                ValidCrd = True

def welcome():
    ####################################################################################################
    # A Fucntion that probably wasn't necessary but it prints a welcom statement to the player
    ####################################################################################################
    
    print('Welcome to the Treasure Hunt Game\nFind coins, avoid Bandits and Have Fun')
def landOnE(totalmapcoins, currentcoinsE, playericon,tx,ty,bx,by, landed, landed1, landed2, landed3, landed4, landed5, landed6, landed7, landed8, landed9,b,c,currency):# land on function
    #######################################################################################################################################################################
    # Calling all these variables into the function
    #######################################################################################################################################################################
    # First thing that happens is that the function check if the variable 'landed' or 'landed1' or etc is equal or greater than 3
    # If so, Then the first Grid co-ordinates in the chest co-ordinate lists is changed from a 'T' to a 'B'
    # Then it checks to see if you have landed on the new bandit
    # If so it tells you you have landed on a Bandit and sets your chosen currency to 0
    #######################################################################################################################################################################
    # If none of this was True e.g Landed wasn't equal or greater than 3, Then the function moves on
    # This check to compare the co-ordinates of the Chest with the co-ordinates of the player
    # If the co-ordinates of the chest are the same as the player, then...
    # You increase the 'Landed' Variable by 1, Add 10 to the current coins
    # Then print a line which tells the player they gained 10 of their chosen currency
    #######################################################################################################################################################################
    # Then right at the end of this section, it checks to see if landed is equal or greater to 3 again
    # If so, then c (which represents the number of chest) is decreased by 1, as the chest has been used 3 times and is now a Bandit
    # And then b (which represent the number of Bandits) is increased by 1
    #######################################################################################################################################################################
    # This is then repeated a further 9 times to check these things for all of the chest, the only things that changes is:
    # The variable 'Landed' is changed each time to 'Landed1' and 'Landed2' and then you get the point
    #######################################################################################################################################################################
    # After all the chest's are checked
    # The Bandit co-ordintes are also compared to the players co-ordinates (similarly to the way it was done with the chests)
    # Except I am using the bandit co-ordinate lists
    # All the co-ordinates are checked (this is done on one line)
    # (The only reason this wasn't done for the chests is because for each chest, I have to check whether it has been landed on 3 Times)
    # Next if the co-ordinates match, The plyers chosen currency is set to zero
    # Then a line is printed to tell the player that they have landed on a bandit
    #######################################################################################################################################################################
    # The last part of this function is returning all of the variables so that if the currency is equal to 10, it is updated within the function
    # Then further down the code, I make sure these variables equal the function so that the numbers are updated across the code then re-pumped back into the function
    # If all of these things are False, the function ends and then is repeated in the while loop down further in the code
    #######################################################################################################################################################################
    if landed >= 3:
        GridCB[tx[0]][ty[0]] = 'B'
    elif Grid[tx[0]][ty[0]] == enemy:
        landed += 1
        currentcoinsE += 10
        totalmapcoins -= 10
        print('Oh no, the enemy landed on a chest, they GAIN 10',currency,'!!')
        if landed >= 3:
            c -= 1
            b += 1
    if landed1 >= 3:
        GridCB[tx[1]][ty[1]] = 'B'
    elif Grid[tx[1]][ty[1]] == enemy:
        landed1 += 1
        currentcoinsE += 10
        totalmapcoins -= 10
        print('Oh no, the enemy landed on a chest, they GAIN 10',currency,'!!')
        if landed1 >= 3:
            c -= 1
            b += 1
    if landed2 >= 3:
        GridCB[tx[2]][ty[2]] = 'B'     
    elif Grid[tx[2]][ty[2]] == enemy:
        landed2 += 1
        currentcoinsE += 10
        totalmapcoins -= 10
        print('Oh no, the enemy landed on a chest, they GAIN 10',currency,'!!')
        if landed2 >= 3:
            c -= 1
            b += 1
    if landed3 >= 3:
        GridCB[tx[3]][ty[3]] = 'B'
    elif Grid[tx[3]][ty[3]] == enemy:
        landed3 += 1
        currentcoinsE += 10
        totalmapcoins -= 10
        print('Oh no, the enemy landed on a chest, they GAIN 10',currency,'!!')
        if landed3 >= 3:
            c -= 1
            b += 1
    if landed3 >= 3:
        GridCB[tx[4]][ty[4]] = 'B'
    elif Grid[tx[4]][ty[4]] == enemy:
        landed4 += 1
        currentcoinsE += 10
        totalmapcoins -= 10
        print('Oh no, the enemy landed on a chest, they GAIN 10',currency,'!!')
        if landed4 >= 3:
            c -= 1
            b += 1
    if landed5 >= 3:
        GridCB[tx[5]][ty[5]] = 'B'   
    elif Grid[tx[5]][ty[5]] == enemy:
        landed5 += 1
        currentcoinsE += 10
        totalmapcoins -= 10
        print('Oh no, the enemy landed on a chest, they GAIN 10',currency,'!!')
        if landed5 >= 3:
            c -= 1
            b += 1
    if landed6 >= 3:
        GridCB[tx[6]][ty[6]] = 'B'
    elif Grid[tx[6]][ty[6]] == enemy:
        landed6 += 1
        currentcoinsE += 10
        totalmapcoins -= 10
        print('Oh no, the enemy landed on a chest, they GAIN 10',currency,'!!')
        if landed6 >= 3:
            c -= 1
            b += 1
    if landed7 >= 3:
        GridCB[tx[7]][ty[7]] = 'B'
    elif Grid[tx[7]][ty[7]] == enemy:
        landed7 += 1
        currentcoinsE += 10
        totalmapcoins -= 10
        print('Oh no, the enemy landed on a chest, they GAIN 10',currency,'!!')
        if landed7 >= 3:
            c -= 1
            b += 1
    if landed8 >= 3:
        GridCB[tx[8]][ty[8]] = 'B'
    elif Grid[tx[8]][ty[8]] == enemy:
        landed8 += 1
        currentcoinsE += 10
        totalmapcoins -= 10
        print('Oh no, the enemy landed on a chest, they GAIN 10',currency,'!!')
        if landed8 >= 3:
            c -= 1
            b += 1
    if landed9 >= 3:
        GridCB[tx[9]][ty[9]] = 'B'
    elif Grid[tx[9]][ty[9]] == enemy:
        landed9 += 1
        currentcoinsE += 10
        totalmapcoins -= 10
        print('Oh no, the enemy landed on a chest, they GAIN 10',currency,'!!')
        if landed9 >= 3:
            c -= 1
            b += 1
    for e in range(b):
        for f in range(b):
            if GridCB[e][f] == 'B' and Grid[e][f] == enemy:
                currentcoinsE = 0
                print('Yay Your enemy lost ALL their',currency)
    return totalmapcoins,b,c,currentcoins, landed, landed1, landed2, landed3, landed4, landed5, landed6, landed7, landed8, landed9        

def landOn(totalmapcoins, currentcoins, playericon,tx,ty,bx,by, landed, landed1, landed2, landed3, landed4, landed5, landed6, landed7, landed8, landed9,b,c,currency):# land on function
    #######################################################################################################################################################################
    # Calling all these variables into the function
    #######################################################################################################################################################################
    # First thing that happens is that the function check if the variable 'landed' or 'landed1' or etc is equal or greater than 3
    # If so, Then the first Grid co-ordinates in the chest co-ordinate lists is changed from a 'T' to a 'B'
    # Then it checks to see if you have landed on the new bandit
    # If so it tells you you have landed on a Bandit and sets your chosen currency to 0
    #######################################################################################################################################################################
    # If none of this was True e.g Landed wasn't equal or greater than 3, Then the function moves on
    # This check to compare the co-ordinates of the Chest with the co-ordinates of the player
    # If the co-ordinates of the chest are the same as the player, then...
    # You increase the 'Landed' Variable by 1, Add 10 to the current coins
    # Then print a line which tells the player they gained 10 of their chosen currency
    #######################################################################################################################################################################
    # Then right at the end of this section, it checks to see if landed is equal or greater to 3 again
    # If so, then c (which represents the number of chest) is decreased by 1, as the chest has been used 3 times and is now a Bandit
    # And then b (which represent the number of Bandits) is increased by 1
    #######################################################################################################################################################################
    # This is then repeated a further 9 times to check these things for all of the chest, the only things that changes is:
    # The variable 'Landed' is changed each time to 'Landed1' and 'Landed2' and then you get the point
    #######################################################################################################################################################################
    # After all the chest's are checked
    # The Bandit co-ordintes are also compared to the players co-ordinates (similarly to the way it was done with the chests)
    # Except I am using the bandit co-ordinate lists
    # All the co-ordinates are checked (this is done on one line)
    # (The only reason this wasn't done for the chests is because for each chest, I have to check whether it has been landed on 3 Times)
    # Next if the co-ordinates match, The plyers chosen currency is set to zero
    # Then a line is printed to tell the player that they have landed on a bandit
    #######################################################################################################################################################################
    # The last part of this function is returning all of the variables so that if the currency is equal to 10, it is updated within the function
    # Then further down the code, I make sure these variables equal the function so that the numbers are updated across the code then re-pumped back into the function
    # If all of these things are False, the function ends and then is repeated in the while loop down further in the code
    #######################################################################################################################################################################
    if landed >= 3:
        GridCB[tx[0]][ty[0]] = 'B'
    elif Grid[tx[0]][ty[0]] == playericon:
        landed += 1
        currentcoins += 10
        totalmapcoins -= 10
        print('You landed on a chest, you GAIN 10',currency,'!!')
        if landed >= 3:
            c -= 1
            b += 1
    if landed1 >= 3:
        GridCB[tx[1]][ty[1]] = 'B'
    elif Grid[tx[1]][ty[1]] == playericon:
        landed1 += 1
        currentcoins += 10
        totalmapcoins -= 10
        print('You landed on a chest, you GAIN 10',currency,'!!')
        if landed1 >= 3:
            c -= 1
            b += 1
    if landed2 >= 3:
        GridCB[tx[2]][ty[2]] = 'B'     
    elif Grid[tx[2]][ty[2]] == playericon:
        landed2 += 1
        currentcoins += 10
        totalmapcoins -= 10
        print('You landed on a chest, you GAIN 10',currency,'!!')
        if landed2 >= 3:
            c -= 1
            b += 1
    if landed3 >= 3:
        GridCB[tx[3]][ty[3]] = 'B'
    elif Grid[tx[3]][ty[3]] == playericon:
        landed3 += 1
        currentcoins += 10
        totalmapcoins -= 10
        print('You landed on a chest, you GAIN 10',currency,'!!')
        if landed3 >= 3:
            c -= 1
            b += 1
    if landed3 >= 3:
        GridCB[tx[4]][ty[4]] = 'B'
    elif Grid[tx[4]][ty[4]] == playericon:
        landed4 += 1
        currentcoins += 10
        totalmapcoins -= 10
        print('You landed on a chest, you GAIN 10',currency,'!!')
        if landed4 >= 3:
            c -= 1
            b += 1
    if landed5 >= 3:
        GridCB[tx[5]][ty[5]] = 'B'   
    elif Grid[tx[5]][ty[5]] == playericon:
        landed5 += 1
        currentcoins += 10
        totalmapcoins -= 10
        print('You landed on a chest, you GAIN 10',currency,'!!')
        if landed5 >= 3:
            c -= 1
            b += 1
    if landed6 >= 3:
        GridCB[tx[6]][ty[6]] = 'B'
    elif Grid[tx[6]][ty[6]] == playericon:
        landed6 += 1
        currentcoins += 10
        totalmapcoins -= 10
        print('You landed on a chest, you GAIN 10',currency,'!!')
        if landed6 >= 3:
            c -= 1
            b += 1
    if landed7 >= 3:
        GridCB[tx[7]][ty[7]] = 'B'
    elif Grid[tx[7]][ty[7]] == playericon:
        landed7 += 1
        currentcoins += 10
        totalmapcoins -= 10
        print('You landed on a chest, you GAIN 10',currency,'!!')
        if landed7 >= 3:
            c -= 1
            b += 1
    if landed8 >= 3:
        GridCB[tx[8]][ty[8]] = 'B'
    elif Grid[tx[8]][ty[8]] == playericon:
        landed8 += 1
        currentcoins += 10
        totalmapcoins -= 10
        print('You landed on a chest, you GAIN 10',currency,'!!')
        if landed8 >= 3:
            c -= 1
            b += 1
    if landed9 >= 3:
        GridCB[tx[9]][ty[9]] = 'B'
    elif Grid[tx[9]][ty[9]] == playericon:
        landed9 += 1
        currentcoins += 10
        totalmapcoins -= 10
        print('You landed on a chest, you GAIN 10',currency,'!!')
        if landed9 >= 3:
            c -= 1
            b += 1
    for e in range(b):
        for f in range(b):
            if GridCB[e][f] == 'B' and Grid[e][f] == playericon:
                currentcoins = 0
                print('Oh no you landed on a Bandit, you lose ALL your',currency)
    return totalmapcoins,b,c,currentcoins, landed, landed1, landed2, landed3, landed4, landed5, landed6, landed7, landed8, landed9

def bandits():
    ###########################################################################
    # This section of Code is idential to the Chest code except...
    # Variable names
    # When the space is blank it prints a 'B' instead of a 'T'
    # The co-ordinates are stored in different lists
    # And it only loops around 5 times as that is how many Bandits there are
    ###########################################################################
    for bandits in range(5):
        ValidCoord = False
        while ValidCoord == False:
            BCx = random.choice(seq)#Bandit co-ordinate x (variable name)
            BCy = random.choice(seq)#Bandit co-ordinate y (variable name)
            if GridCB[BCx][BCy] == " ":
                GridCB[0][0] != 'B'
                GridCB[BCx][BCy] = 'B'
                bx.append(BCx)
                by.append(BCy)
                ValidCoord = True
def ValidH():
    if txp >= height:
        print('Invalid move')
        return False
    else:
        return True
def ValidW():
    if typ >= width:
        print('Invalid move')
        return False
    else:
        return True
def rules():
    #############################################################################################################################
    # This function is just an easy way to condense my rules so i don't have to print them each time I want to display my rules
    # It is also formulated so that the rules print out in a neat way and within a nice Ascii box
    #############################################################################################################################
    print('\n╔═════════════════════════════════════════════════════════════════════════════╗')
    print('║1) You can move within the Grid, it will not let you move out of it          ║')
    print('║2) The symbol you choose is your Player Icon.                                ║')
    print('║3) The movement system is simple.                                            ║\n║  -u1 = Your player will increase 1 space vertically and the same for down.  ║\n║  -r1 = Your player will increase 1 space to the Right and...                ║\n║   visa versa for the Left movement.                                         ║')
    print('║4) If you land on a chest (there are 10 chest)                               ║\n║  -you gain 10 of your chosen currency and chest will stay there for 3 tries;║\n║   e.g you can get 30 of your chosen                                         ║\n║   currency out of a chest, then it becomes a bandit                         ║')
    print('║5) If you land on a Bandit (there are 5 bandits)                             ║\n║  -you will lose ALL of your chosen currency.                                ║')
    print('║6) If you gain 100 of your chosen currency, You will WIN THE GAME!!!         ║')
    print('╚═════════════════════════════════════════════════════════════════════════════╝\n')
def clearscreen():
    ####################################################################################################
    # Enters a for loop
    # Print a new line 25 times in the loop to give the effect of the python shell clearing
    # Then it ends
    ####################################################################################################
    for x in range(25):
        print('\n')
enemy = 'E'
playericon = '' # playericon starts as a blank string
currentcoinsE = 0
currentcoins = 0# The users coins
########################################################
# All the variables required in my 'Landon' function
landed = 0
landed1 = 0
landed2 = 0
landed3 = 0
landed4 = 0
landed5 = 0
landed6 = 0
landed7 = 0
landed8 = 0
landed9 = 0
########################################################
s = "s"
currency = '' # currency starts as a blank string
#########################################################
# A menu I created using ascii assigned to a variable
themainmenu = "Welcome to the Treasure Hunt Game\nFind coins, avoid Bandits and Have Fun\n\
╔═══════════════════════════╗\n\
║ 1, Play The Treasure Hunt ║\n\
╠═══════════════════════════╣\n\
║ 2, ---------------------- ║\n\
╠═══════════════════════════╣\n\
║ 5, AI                     ║\n\
╠═══════════════════════════╣\n\
║ 9, Quit the Program       ║\n\
╚═══════════════════════════╝\n\
Choose an Option: "
#########################################################################
# ENTER WHILE LOOP
# THE MAIN WHILE LOOP
# Because this is the area that all the functions are called in
# This is my main game
#########################################################################
while True:
    #########################################################################
    # Asking the user for an intiger input
    # Assigns it to the variable 'Menu'
    # If it matches one of the intigers i have chosen, something happens
    # If not then it tells the player and re-prints the menu
    Menu = UserInt(themainmenu)
    #########################################################################
    if Menu == 1:
        #############################################################################################################################
        # This is my main game section
        #############################################################################################################################
        # EXTRA NOTE:
        # All of the things I have described with brackets beside the word, means I have 'called' the function
        # Which means I have basically taken all of the code within the chosen 'def' statement above and put it here
        # It is an easier way of coding rather than printing all of the code above within the final game code, it just simplifies it
        # END OF EXTRA NOTE
        #############################################################################################################################
        gridreset(Grid) # Reset all Grid co-ordinates to blank
        gridreset2()
        clearscreen() # Prints lots of new lines
        print('Welcome to TREASURE HUNT!!!\n') # Welcoming the Player to the treasure hunt
        rules() # Prints out the rules of the game
        #############################################################################################################################
        # Enter while loop
        # Ask the user for a string input that will represent there player
        # if it isn't 1 element in length or it's blank it will tell the player this is invalid and loop back around
        # if it is 1 element in length and isn't blank, you break out of the loop and the code continues
        #############################################################################################################################
        while True:
            playericon = str(input('What do you want your Player to look like(single digit and no space): '))
            if len(playericon) > 1 or playericon == '':
                print("This input is not valid, try again\n")
            else:
                break
        #############################################################################################################################
        # For the currency it works the same, ish
        # it enters the loop and ask for a string input, except there isn't a wrong answer this time
        # all it does is check to see if the work has an 's' at the end, it it does then it breaks out of the loop
        # if it doesn't then it adds one for you (I previously assinged the string input 's' to a variable called s
        # E.G currency = currency plus the variable s (aka the letter 's'), then this also breaks out of the loop
        # allowing the code to continue
        #############################################################################################################################
        while True:
            currency = str(input('\nWhat do you want to collect, e.g V-bucks, dollars,etc. Take your pick: '))
            if currency[len(currency) - 1] != s:
                currency = (currency + s)
                break
            else:
                break
        coinswin = 100 # assigns the intiger 100 to a variable called 'coinswin'
        Grid[0][0] = playericon # placing the player icon in the bottom left of the Grid (in this case it's 0,0)
        chests() # Spawns chest on seperate Grid
        bandits() # Spawns Bandits on seperate Grid
        Map(b,c)  # Prints player Grid
        while True:
            ###########################################################################
            # Checks to see if a chest has been landed on 3 times
            # Then checks to see if the player is currently landed on a bandit or chest
            # If so it performs it actions
            # If not then it continues
            ###########################################################################
            totalmapcoins, b,c,currentcoins, landed, landed1, landed2, landed3, landed4, landed5, landed6, landed7, landed8, landed9 = landOn(totalmapcoins, currentcoins, playericon,tx,ty,bx,by, landed, landed1, landed2, landed3, landed4, landed5, landed6, landed7, landed8, landed9,b,c,currency)
            print(currency,'=', currentcoins,'\n') # Prints there chosen currency and how much of it they have
            win = currentcoins # Asigning the players current amount of coins to a variable called 'win'
            lose = totalmapcoins
            if lose <= 90 or c == 0:
                gridreset(Grid) # Then again set all Grid co-ordinates to blank
                gridreset2()
                print('\nSorry, you lost, there is not enough',currency,'to win !!!\n') # Tell the player they lost because there isn't enough currency to win
                print('Ending Game...\n')
                ####################################################################################################
                # Basically resetting all the varibales to what they were at the start of the code
                ####################################################################################################
                playericon = ''
                currentcoins = 0
                landed = 0
                landed1 = 0
                landed2 = 0
                landed3 = 0
                landed4 = 0
                landed5 = 0
                landed6 = 0
                landed7 = 0
                landed8 = 0
                landed9 = 0
                s = "s"
                currency = ''
                tx = []
                ty = []
                bx = []
                by = []
                # Stall the program for 1 second
                time.sleep(1)
                clearscreen() # Print lots of new lines
                break # Break out of loop, so in turn returning to the main menu
            if win == coinswin: # If win (aka the playes coins/currency) is equal to coinswin (aka 100) or if c (the number of chest) is equla to 0 (so there arn't any chest left)
                gridreset(Grid) # Then again set all Grid co-ordinates to blank
                gridreset2()
                print('\nHorray you won, you avoided the bandits and Gained 100',currency,'!!!\n') # Tell the player they won by collecting 100 currency
                print('Ending Game...\n')
                ####################################################################################################
                # Basically resetting all the varibales to what they were at the start of the code
                ####################################################################################################
                playericon = ''
                currentcoins = 0
                landed = 0
                landed1 = 0
                landed2 = 0
                landed3 = 0
                landed4 = 0
                landed5 = 0
                landed6 = 0
                landed7 = 0
                landed8 = 0
                landed9 = 0
                s = "s"
                currency = ''
                tx = []
                ty = []
                bx = []
                by = []
                # Stall the program for 1 second
                time.sleep(1)
                clearscreen() # Print lots of new lines
                break # Break out of loop, so in turn returning to the main menu
            #############################################################################################################################
            # Then it the player hasn't won, aka it the if statement isn't true
            # Then the players movement system function is displyaed to the player, and the game continues round the loop
            # Each time it loops checking to see if the user has won or landed on a Chest of Bandit
            #############################################################################################################################
            txp, typ = Gameplay(playericon) 
            
    elif Menu == 2:
        #############################################################################################################################
        # This part is the developer part of the code
        # This idnetical to the normal game except...
        # The Chest and Bandit co-ordinate lists are printed after the Chest and Bandits are spawned
        # At the start and on each turn, the extra Grid with the Chest and Bandits is printed and displayed to the player
        #############################################################################################################################
        gridreset(Grid)
        gridreset2()
        clearscreen()
        print('Welcome to TREASURE HUNT!!!\n')
        rules()
        while True:
            playericon = str(input('What do you want your Player to look like(single digit and no space): '))
            if len(playericon) > 1 or playericon == '':
                print('Why you so stupid')
            else:
                break
        while True:
            currency = str(input('\nWhat do you want to collect, e.g V-bucks, dollars,etc. Take your pick: '))
            if currency[len(currency) - 1] != s:
                currency = (currency + s)
                break
            else:
                break
        coinswin = 100
        Grid[0][0] = playericon
        GridCB[0][0] = 'P'
        chests()
        bandits()
        print('T',tx,ty)
        print('B',bx,by)
        Map(b,c)
        MapCB()
        while True:
            totalmapcoins, b,c,currentcoins, landed, landed1, landed2, landed3, landed4, landed5, landed6, landed7, landed8, landed9 = landOn(totalmapcoins, currentcoins, playericon,tx,ty,bx,by, landed, landed1, landed2, landed3, landed4, landed5, landed6, landed7, landed8, landed9,b,c,currency)
            print(currency,'=', currentcoins,'\n')
            winDev = currentcoins
            lose = totalmapcoins
            if lose <= 90 or c == 0:
                gridreset(Grid) # Then again set all Grid co-ordinates to blank
                gridreset2()
                print('\nSorry, you lost, there is not enough',currency,'to win !!!\n') # Tell the player they lost because there isn't enough currency to win
                print('Ending Game...\n')
                ####################################################################################################
                # Basically resetting all the varibales to what they were at the start of the code
                ####################################################################################################
                playericon = ''
                currentcoins = 0
                landed = 0
                landed1 = 0
                landed2 = 0
                landed3 = 0
                landed4 = 0
                landed5 = 0
                landed6 = 0
                landed7 = 0
                landed8 = 0
                landed9 = 0
                s = "s"
                currency = ''
                tx = []
                ty = []
                bx = []
                by = []
                # Stall the program for 1 second
                time.sleep(1)
                clearscreen() # Print lots of new lines
                break # Break out of loop, so in turn returning to the main menu
            if winDev == coinswin:
                gridreset(Grid)
                gridreset2()
                print('\nHorray you won, you avoided the bandits and Gained 100',currency,'!!!\n')
                print('Ending Game...\n')
                playericon = ''
                currentcoins = 0
                landed = 0
                landed1 = 0
                landed2 = 0
                landed3 = 0
                landed4 = 0
                landed5 = 0
                landed6 = 0
                landed7 = 0
                landed8 = 0
                landed9 = 0
                s = "s"
                currency = ''
                tx = []
                ty = []
                bx = []
                by = []
                time.sleep(1)
                clearscreen()
                break
            
            txp, typ = Gameplay(playericon)
            MapCB()
    elif Menu == 3:
        #############################################################################################
        # This is my hidden area of the code I used through my coding process to test thing out
        # At the moment as my code is finished, It isn't in use
        # So all I do is tell he player it isn't in usem stall the program for 1 second
        # Print lots of new lines and that bit of code ends, the menu is re-printed
        #############################################################################################
        print('Test Phase currently not in service')
        time.sleep(1)
        clearscreen()
    elif Menu == 5:
        #############################################################################################################################
        # This is my main game section
        #############################################################################################################################
        # EXTRA NOTE:
        # All of the things I have described with brackets beside the word, means I have 'called' the function
        # Which means I have basically taken all of the code within the chosen 'def' statement above and put it here
        # It is an easier way of coding rather than printing all of the code above within the final game code, it just simplifies it
        # END OF EXTRA NOTE
        #############################################################################################################################
        gridreset(Grid) # Reset all Grid co-ordinates to blank
        gridreset2()
        clearscreen() # Prints lots of new lines
        print('Welcome to TREASURE HUNT AI!!!\n') # Welcoming the Player to the treasure hunt
        rules() # Prints out the rules of the game
        #############################################################################################################################
        # Enter while loop
        # Ask the user for a string input that will represent there player
        # if it isn't 1 element in length or it's blank it will tell the player this is invalid and loop back around
        # if it is 1 element in length and isn't blank, you break out of the loop and the code continues
        #############################################################################################################################
        while True:
            playericon = str(input('What do you want your Player to look like(single digit and no space): '))
            if len(playericon) > 1 or playericon == '':
                print("This input is not valid, try again\n")
            else:
                break
        #############################################################################################################################
        # For the currency it works the same, ish
        # it enters the loop and ask for a string input, except there isn't a wrong answer this time
        # all it does is check to see if the work has an 's' at the end, it it does then it breaks out of the loop
        # if it doesn't then it adds one for you (I previously assinged the string input 's' to a variable called s
        # E.G currency = currency plus the variable s (aka the letter 's'), then this also breaks out of the loop
        # allowing the code to continue
        #############################################################################################################################
        while True:
            currency = str(input('\nWhat do you want to collect, e.g V-bucks, dollars,etc. Take your pick: '))
            if currency[len(currency) - 1] != s:
                currency = (currency + s)
                break
            else:
                break
        print('The AI is going to try to beat you')
        coinswin = 100 # assigns the intiger 100 to a variable called 'coinswin'
        Grid[0][0] = playericon # placing the player icon in the bottom left of the Grid (in this case it's 0,0)
        Grid[7][7] = enemy
        chests() # Spawns chest on seperate Grid
        bandits() # Spawns Bandits on seperate Grid
        Map(b,c)  # Prints player Grid
        while True:
            ###########################################################################
            # Checks to see if a chest has been landed on 3 times
            # Then checks to see if the player is currently landed on a bandit or chest
            # If so it performs it actions
            # If not then it continues
            ###########################################################################
            totalmapcoins, b,c,currentcoinsE, landed, landed1, landed2, landed3, landed4, landed5, landed6, landed7, landed8, landed9 = landOnE(totalmapcoins, currentcoinsE, playericon,tx,ty,bx,by, landed, landed1, landed2, landed3, landed4, landed5, landed6, landed7, landed8, landed9,b,c,currency)
            totalmapcoins, b,c,currentcoins, landed, landed1, landed2, landed3, landed4, landed5, landed6, landed7, landed8, landed9 = landOn(totalmapcoins, currentcoins, playericon,tx,ty,bx,by, landed, landed1, landed2, landed3, landed4, landed5, landed6, landed7, landed8, landed9,b,c,currency)
            print('Your',currency,'=', currentcoins,'\n')# Prints there chosen currency and how much of it they have
            print('AI',currency,'=', currentcoins,'\n')
            win = currentcoins # Asigning the players current amount of coins to a variable called 'win'
            lose = totalmapcoins
            if lose <= 90 or c == 0:
                gridreset(Grid) # Then again set all Grid co-ordinates to blank
                gridreset2()
                print('\nSorry, you lost, there is not enough',currency,'to win !!!\n') # Tell the player they lost because there isn't enough currency to win
                print('Ending Game...\n')
                ####################################################################################################
                # Basically resetting all the varibales to what they were at the start of the code
                ####################################################################################################
                playericon = ''
                currentcoins = 0
                landed = 0
                landed1 = 0
                landed2 = 0
                landed3 = 0
                landed4 = 0
                landed5 = 0
                landed6 = 0
                landed7 = 0
                landed8 = 0
                landed9 = 0
                s = "s"
                currency = ''
                tx = []
                ty = []
                bx = []
                by = []
                # Stall the program for 1 second
                time.sleep(1)
                clearscreen() # Print lots of new lines
                break # Break out of loop, so in turn returning to the main menu
            if win == coinswin: # If win (aka the playes coins/currency) is equal to coinswin (aka 100) or if c (the number of chest) is equla to 0 (so there arn't any chest left)
                gridreset(Grid) # Then again set all Grid co-ordinates to blank
                gridreset2()
                print('\nHorray you won, you avoided the bandits and Gained 100',currency,'!!!\n') # Tell the player they won by collecting 100 currency
                print('Ending Game...\n')
                ####################################################################################################
                # Basically resetting all the varibales to what they were at the start of the code
                ####################################################################################################
                playericon = ''
                currentcoins = 0
                landed = 0
                landed1 = 0
                landed2 = 0
                landed3 = 0
                landed4 = 0
                landed5 = 0
                landed6 = 0
                landed7 = 0
                landed8 = 0
                landed9 = 0
                s = "s"
                currency = ''
                tx = []
                ty = []
                bx = []
                by = []
                # Stall the program for 1 second
                time.sleep(1)
                clearscreen() # Print lots of new lines
                break # Break out of loop, so in turn returning to the main menu
            #############################################################################################################################
            # Then it the player hasn't won, aka it the if statement isn't true
            # Then the players movement system function is displyaed to the player, and the game continues round the loop
            # Each time it loops checking to see if the user has won or landed on a Chest of Bandit
            #############################################################################################################################
            txp, typ = Gameplay(playericon)
            AImove()
    elif Menu == 9:
        ##################################################
        # This is my quit the game section
        ##################################################
            print('Quitting program...') # Inform the user the program is quitting
            time.sleep(1) # Stall the program for 1 second
            clearscreen() # Print lots of new lines
            exit() #This is something built into Python that closes the Shell
            break # Break out the main while loop, there is no code left now so the program is terminated by Python

#########################
#########################
#  THE END OF MY CODE   #
#########################
#########################
    
