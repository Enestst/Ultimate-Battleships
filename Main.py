
# Ultimate Battleships

def print_ships_to_be_placed():
    print("Ships to be placed:", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Ships to be placed: ")


# elem expected to be a single list element of a primitive type.
def print_single_element(elem):
    print(str(elem), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write(str(elem) + " ")


def print_empty_line():
    print()
    if FILE_OUTPUT_FLAG:
        f.write("\n")


# n expected to be str or int.
def print_player_turn_to_place(n):
    print("It is Player {}'s turn to place their ships.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to place their ships.\n".format(n))


def print_to_place_ships():
    print("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) : \n")
        # There is a \n because we want the board to start printing on the next line.


def print_incorrect_input_format():
    print("Input is in incorrect format, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Input is in incorrect format, please try again.\n")


def print_incorrect_coordinates():
    print("Incorrect coordinates given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect coordinates given, please try again.\n")


def print_incorrect_ship_name():
    print("Incorrect ship name given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect ship name given, please try again.\n")


def print_incorrect_orientation():
    print("Incorrect orientation given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect orientation given, please try again.\n")


# ship expected to be str.
def print_ship_is_already_placed(ship):
    print(ship, "is already placed, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " is already placed, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_outside(ship):
    print(ship, "cannot be placed outside the board, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed outside the board, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_occupied(ship):
    print(ship, "cannot be placed to an already occupied space, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed to an already occupied space, please try again.\n")


def print_confirm_placement():
    print("Confirm placement Y/N :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Confirm placement Y/N : \n")


# n expected to be str or int.
def print_player_turn_to_strike(n):
    print("It is Player {}'s turn to strike.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to strike.\n".format(n))


def print_choose_target_coordinates():
    print("Choose target coordinates :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Choose target coordinates : ")


def print_miss():
    print("Miss.")
    if FILE_OUTPUT_FLAG:
        f.write("Miss.\n")


# n expected to be str or int.
def print_type_done_to_yield(n):
    print("Type done to yield your turn to player {} :".format(n), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Type done to yield your turn to player {} : \n".format(n))


def print_tile_already_struck():
    print("That tile has already been struck. Choose another target.")
    if FILE_OUTPUT_FLAG:
        f.write("That tile has already been struck. Choose another target.\n")


def print_hit():
    print("Hit!")
    if FILE_OUTPUT_FLAG:
        f.write("Hit!\n")


# n expected to be str or int.
def print_player_won(n):
    print("Player {} has won!".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("Player {} has won!\n".format(n))


def print_thanks_for_playing():
    print("Thanks for playing.")
    if FILE_OUTPUT_FLAG:
        f.write("Thanks for playing.\n")


# my_list expected to be a 3-dimensional list, formed from two 2-dimensional lists containing the boards of each player.
def print_3d_list(my_list):
    first_d = len(my_list[0])
    for row_ind in range(first_d):
        second_d = len(my_list[0][row_ind])
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[0][row_ind][col_ind], end=' ')
        print("\t\t\t", end='')
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[1][row_ind][col_ind], end=' ')
        print()
    print("", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\t\t", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\nPlayer 1\t\t\t\t\t\tPlayer 2")
    print()

    if FILE_OUTPUT_FLAG:
        first_d = len(my_list[0])
        for row_ind in range(first_d):
            second_d = len(my_list[0][row_ind])
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[0][row_ind][col_ind] + " ")
            f.write("\t\t\t")
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[1][row_ind][col_ind] + " ")
            f.write("\n")
        f.write("   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\t\t   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\nPlayer 1\t\t\t\t\t\tPlayer 2\n")
        f.write("\n")


def print_rules():
    print("Welcome to Ultimate Battleships")
    print("This is a game for 2 people, to be played on two 10x10 boards.")
    print("There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).")
    print("First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.")
    print("Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.")
    print("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.")
    print("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.")
    print("Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.")
    print("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.")
    print("The last player to have an unsunk ship wins.")
    print("Have fun!")
    print()

    if FILE_OUTPUT_FLAG:
        f.write("Welcome to Ultimate Battleships\n")
        f.write("This is a game for 2 people, to be played on two 10x10 boards.\n")
        f.write(
            "There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).\n")
        f.write(
            "First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.\n")
        f.write(
            "Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.\n")
        f.write("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.\n")
        f.write("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.\n")
        f.write(
            "Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.\n")
        f.write("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.\n")
        f.write("The last player to have an unsunk ship wins.\n")
        f.write("Have fun!\n")
        f.write("\n")


# Create the game
board_size = 10
f = open('UltimateBattleships.txt', 'w')
FILE_OUTPUT_FLAG = True  # You can change this to True to also output to a file so that you can check your outputs with diff.

print_rules()

# Remember to use list comprehensions at all possible times.
# If we see you populate a list that could be done with list comprehensions using for loops, append/extend/insert etc. you will lose points.

# Make sure to put comments in your code explaining your approach and the execution.

# We defined all the functions above for your use so that you can focus only on your code and not the formatting.
# You need to call them in your code to use them of course.

# If you have questions related to this homework, direct them to utku.bozdogan@boun.edu.tr please.

# Do not wait until the last day or two to start doing this homework, it requires serious effort.

try:  # The entire code is in this try block, if there ever is an error during execution, we can safely close the file.
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    # printing table for each player
    list1 = [['-' for i in range(10)] for i in range(10)]
    list2 = [['-' for i in range(10)] for i in range(10)]
    mylist = [list1, list2]
    list3 = [['-' for i in range(10)] for i in range(10)]
    list4 = [['-' for i in range(10)] for i in range(10)]
    mylist2 = [list3, list4]
    list5 = [['-' for i in range(10)] for i in range(10)]
    list6 = [['-' for i in range(10)] for i in range(10)]
    mylist3 = [list5, list6]
    print_3d_list(mylist)

    # create ship name list and dict.
    ship_dict = {'carrier': 5,
                 'battleship': 4,
                 'submarine': 3,
                 'cruiser': 3,
                 'destroyer': 2}
    shipnamelist = ['carrier', 'battleship', 'submarine', 'cruiser', 'destroyer']

    # creating ship lists
    shiplist1 = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
    shiplist12 = ['carrier', 'battleship', 'cruiser', 'submarine', 'destroyer']
    shiplist22 = ['carrier', 'battleship', 'cruiser', 'submarine', 'destroyer']
    # ship placement for player 1
    while len(shiplist12) > 0:
        for j in range(len(shiplist12)):
            shiplist12[j] = shiplist12[j].capitalize()
        print_ships_to_be_placed()
        print_single_element(' '.join(shiplist12))
        print_empty_line()
        for j in range(len(shiplist12)):
            shiplist12[j] = shiplist12[j].lower()
    
        print_player_turn_to_place(1)
        # taking infos from user
        print_to_place_ships()
        shipinfo = input().split()
    
        # checking errors from input
    
        try:
            shipinfo[1] = int(shipinfo[1])
            shipinfo[2] = int(shipinfo[2])
        except:
            print_incorrect_input_format()
            print_3d_list(mylist)
            continue
        # checking enough inputs error
        if len(shipinfo) != 4:
            print_incorrect_input_format()
            print_3d_list(mylist)
            continue
        # checking incorrect coordinates error
        if int(shipinfo[1]) not in range(1, 11):
            print_incorrect_coordinates()
            print_3d_list(mylist)
            continue
        if int(shipinfo[2]) not in range(1, 11):
            print_incorrect_coordinates()
            print_3d_list(mylist)
            continue
        # checking incorrect ship name error
        if shipinfo[0].lower() not in shipnamelist:
            print_incorrect_ship_name()
            print_3d_list(mylist)
            continue
        # checking incorrect orientation error
        if shipinfo[3].lower() not in ['v', 'h']:
            print_incorrect_orientation()
            print_3d_list(mylist)
            continue
    
        # error if ship already placed
        if shipinfo[0].lower() not in shiplist12:
            print_ship_is_already_placed(shipinfo[0].capitalize())
            print_3d_list(mylist)
            continue
        # error checking if ship will be plaed to outside to board
        if shipinfo[3].lower() == 'v':
            if int(shipinfo[2]) + ship_dict[shipinfo[0].lower()] > 11:
                print_ship_cannot_be_placed_outside(shipinfo[0].capitalize())
                print_3d_list(mylist)
                continue
        if shipinfo[3].lower() == 'h':
            if int(shipinfo[1]) + ship_dict[shipinfo[0].lower()] > 11:
                print_ship_cannot_be_placed_outside(shipinfo[0].capitalize())
                print_3d_list(mylist)
                continue
    
        # checking if ships place will be occupied
        if shipinfo[3].lower() == 'v':
            flag = 0
            for j in range(ship_dict[shipinfo[0].lower()]):
                if list1[int(shipinfo[2]) + j - 1][int(shipinfo[1]) - 1] == '#':
                    print_ship_cannot_be_placed_occupied(shipinfo[0].capitalize())
                    print_3d_list(mylist)
                    flag = 1
                    break
            if flag == 1:
                continue
        if shipinfo[3].lower() == 'h':
            flag = 0
            for j in range(ship_dict[shipinfo[0].lower()]):
                if list1[int(shipinfo[2]) - 1][int(shipinfo[1]) + j - 1] == '#':
                    print_ship_cannot_be_placed_occupied(shipinfo[0].capitalize())
                    print_3d_list(mylist)
                    flag = 1
                    break
            if flag == 1:
                continue
        shiplist12.remove(shipinfo[0].lower())
    
        # ship placement for player 1
        if shipinfo[3].lower() == 'h':
            for i in range(ship_dict[shipinfo[0].lower()]):
                list1[int(shipinfo[2]) - 1][int(shipinfo[1]) + i - 1] = '#'
        if shipinfo[3].lower() == 'v':
            for i in range(ship_dict[shipinfo[0].lower()]):
                list1[int(shipinfo[2]) + i - 1][int(shipinfo[1]) - 1] = '#'
        print_3d_list(mylist)
    
        # asking will player 1 confirm his/her ship placement
        if len(shiplist12) == 0:
            print_confirm_placement()
            confirm1 = input()
            while confirm1.upper() not in ['Y', 'N']:
                print_confirm_placement()
                confirm1 = input()
            if confirm1.upper() == "N":
                shiplist12 = ['carrier', 'battleship', 'cruiser', 'submarine', 'destroyer']
                list1 = [['-' for j in range(10)] for i in range(10)]
                mylist = [list1, list2]
                print_3d_list(mylist)
                continue
            else:
                print_3d_list(mylist2)

    # ship placement loop for player 2
    while len(shiplist22) > 0:
        # printing ships to be placed function
        for j in range(len(shiplist22)):
            shiplist22[j] = shiplist22[j].capitalize()
        print_ships_to_be_placed()
        print_single_element(' '.join(shiplist22))
        print_empty_line()
        for j in range(len(shiplist22)):
            shiplist22[j] = shiplist22[j].lower()
    
        print_player_turn_to_place(2)
    
        # taking infos for player 2
        print_to_place_ships()
        shipinfo = input().split()
        # checking errors for player 2
        try:
            shipinfo[1] = int(shipinfo[1])
            shipinfo[2] = int(shipinfo[2])
        except:
            print_incorrect_input_format()
            print_3d_list(mylist2)
            continue
    
        if len(shipinfo) != 4:
            print_incorrect_input_format()
            print_3d_list(mylist2)
            continue
        if int(shipinfo[1]) not in range(1, 11):
            print_incorrect_coordinates()
            print_3d_list(mylist2)
            continue
        if int(shipinfo[2]) not in range(1, 11):
            print_incorrect_coordinates()
            print_3d_list(mylist2)
            continue
        if shipinfo[0].lower() not in shipnamelist:
            print_incorrect_ship_name()
            print_3d_list(mylist2)
            continue
        if shipinfo[3].lower() not in ['v', 'h']:
            print_incorrect_orientation()
            print_3d_list(mylist2)
            continue
    
        if shipinfo[0].lower() not in shiplist22:
            print_ship_is_already_placed(shipinfo[0].capitalize())
            print_3d_list(mylist2)
            continue
        # checking can not be placed outside error
        if shipinfo[3].lower() == 'v':
            if int(shipinfo[2]) + ship_dict[shipinfo[0].lower()] > 11:
                print_ship_cannot_be_placed_outside(shipinfo[0].capitalize())
                print_3d_list(mylist2)
                continue
        if shipinfo[3].lower() == 'h':
            if int(shipinfo[1]) + ship_dict[shipinfo[0].lower()] > 11:
                print_ship_cannot_be_placed_outside(shipinfo[0].capitalize())
                print_3d_list(mylist2)
                continue
        # checking occupied error
        if shipinfo[3].lower() == 'v':
            flag = 0
            for j in range(ship_dict[shipinfo[0].lower()]):
                if list4[int(shipinfo[2]) + j - 1][int(shipinfo[1]) - 1] == '#':
                    print_ship_cannot_be_placed_occupied(shipinfo[0].capitalize())
                    print_3d_list(mylist2)
                    flag = 1
                    break
            if flag == 1:
                continue
        if shipinfo[3].lower() == 'h':
            flag = 0
            for j in range(ship_dict[shipinfo[0].lower()]):
                if list4[int(shipinfo[2]) - 1][int(shipinfo[1]) + j - 1] == '#':
                    print_ship_cannot_be_placed_occupied(shipinfo[0].capitalize())
                    print_3d_list(mylist2)
                    flag = 1
                    break
            if flag == 1:
                continue
        shiplist22.remove(shipinfo[0].lower())
    
        # ship placement for player 2
        if shipinfo[3].lower() == 'h':
            for i in range(ship_dict[shipinfo[0].lower()]):
                list4[int(shipinfo[2]) - 1][int(shipinfo[1]) + i - 1] = '#'
        if shipinfo[3].lower() == 'v':
            for i in range(ship_dict[shipinfo[0].lower()]):
                list4[int(shipinfo[2]) + i - 1][int(shipinfo[1]) - 1] = '#'
        print_3d_list(mylist2)
    
        # confirming ship placement of player 2
        if len(shiplist22) == 0:
            print_confirm_placement()
            confirm1 = input()
            while confirm1.upper() not in ['Y', 'N']:
                print_confirm_placement()
                confirm2 = input()
                if confirm2.upper() in ['Y', 'N']:
                    break
            if confirm1.upper() == "N":
                shiplist22 = ['carrier', 'battleship', 'cruiser', 'submarine', 'destroyer']
                list4 = [['-' for j in range(10)] for i in range(10)]
                mylist2 = [list3, list4]
                print_3d_list(mylist2)
                continue

    # HIT PART
    noh1 = 0
    noh2 = 0
    # hit queue. If p1 true turn for player 1. Else turn for player 2.
    p1 = True
    while noh1 < 17 or noh2 < 17:  # loop until any player will finish game
        if p1:
            print_3d_list(mylist)
            print_player_turn_to_strike(1)
            print_choose_target_coordinates()
            coors = input().split()  # taking inputs for coordinate part
        
            # checking errors for hit part
            if len(coors) != 2:
                print_incorrect_input_format()
            
                continue
            try:
                coors[0] = int(coors[0])
                coors[1] = int(coors[1])
            except:
                print_incorrect_input_format()
                p1 = True
                continue
        
            if int(coors[0]) not in range(1, 11):
                print_incorrect_coordinates()
            
                continue
            if int(coors[1]) not in range(1, 11):
                print_incorrect_coordinates()
                continue
            if list4[int(coors[1]) - 1][int(coors[0]) - 1] == 'O' or list4[int(coors[1]) - 1][
                int(coors[0]) - 1] == '!':
                print_tile_already_struck()
                continue
            # convert inputs to integer
            coors[0] = int(coors[0])
            coors[1] = int(coors[1])
            # shoot placement part
            if list4[coors[1] - 1][coors[0] - 1] == '-':  # checking miss part
                print_miss()
                list2[coors[1] - 1][coors[0] - 1] = 'O'
                list4[coors[1] - 1][coors[0] - 1] = 'O'
            
                print_type_done_to_yield(2)
                conff = input()
                # if player 1 miss, done part
                while conff.lower() != 'done':
                    print_type_done_to_yield(2)
                    conff = input()
                p1 = False
                continue
            elif list4[coors[1] - 1][coors[0] - 1] == '#':  # checking hit part
                print_hit()
                list2[coors[1] - 1][coors[0] - 1] = '!'
                list4[coors[1] - 1][coors[0] - 1] = '!'
                noh1 += 1
                if noh1 == 17:
                    break
                continue
    
    
    
        else: # hit turn for player 2
            print_3d_list(mylist2)
            print_player_turn_to_strike(2)
            print_choose_target_coordinates()
            # taking inputs
            coors = input().split()
            # checking errors for player 2
            if len(coors) != 2:
                print_incorrect_input_format()
            
                continue
        
            try:
                coors[0] = int(coors[0])
                coors[1] = int(coors[1])
            except:
                print_incorrect_input_format()
            
                continue
            # checking incorrect coordinates error
            if int(coors[0]) not in range(1, 11):
                print_incorrect_coordinates()
            
                continue
            if int(coors[1]) not in range(1, 11):
                print_incorrect_coordinates()
                continue
            # checking already struck error
            if list1[int(coors[1]) - 1][int(coors[0]) - 1] == 'O' or list1[int(coors[1]) - 1][int(coors[0]) - 1] == '!':
                print_tile_already_struck()
                continue
            # converting coordinates to integer
            coors[0] = int(coors[0])
            coors[1] = int(coors[1])
            if list1[coors[1] - 1][coors[0] - 1] == '-':
                print_miss()
                list3[coors[1] - 1][coors[0] - 1] = 'O'
                list1[coors[1] - 1][coors[0] - 1] = 'O'
            
                print_type_done_to_yield(1)
                conff = input()
                while conff.lower() != 'done':
                    print_type_done_to_yield(1)
                    conff = input()
                p1 = True
                continue
            elif list1[coors[1] - 1][coors[0] - 1] == '#':
                print_hit()
                list3[coors[1] - 1][coors[0] - 1] = '!'
                list1[coors[1] - 1][coors[0] - 1] = '!'
                noh2 += 1
                if noh2 == 17:
                    break
                continue

    if noh1 == 17:  # checking all shoots are done and game will be finished for player 1
        print_3d_list(mylist)
        print_player_won(1)
    elif noh2 == 17:  # checking all shoots are done and game will be finished for player 2
        print_3d_list(mylist2)
        print_player_won(2)
    # end of the game and printing thanks for playing function
    print_thanks_for_playing()

    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
except:
    f.close()

