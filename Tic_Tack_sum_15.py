# -Name: Ibrahim Tarek Ibrahim Mohamed
# -Student_ID: 20211002
# -Course: Structured Programming -CS112-
# -This Code is Directed to Dr. Mohamed EL-Ramly and
# cannot be shared except by the owner's permission
# -Game: Tik-Tack-toe: Sum of 15
# -Type: raw code
#######################################################

used_nums, used_letters = [],[]     # an empty list to add used numbers and letters.
board = [       # the board
["a","b","c"],
["d","e","f"],
["g","h","i"]
]

## Displaying the board
def display_board():
    for row in (board):
        print(row)

## Taking player input
def get_input(player,num_state):

    message_number = f"Player {player}, Please enter {num_state} number between (0 to 9): "          # displayed message for number input
    message_position = f"Player {player}, Please enter positiion from (a to i): "     # displayed message for position input

    # loop for specific not used (numbers) input
    while True:
        try:
            get_number = int(input(message_number))     #get number from user
            if get_number not in used_nums:     #check if number already used
                if player == "One":     #PL.1 case
                    if get_number %2 != 0 and get_number < 10:      # Check if number is odd
                        break
                elif player == "Two":   #PL.2 case
                    if get_number %2 == 0 and get_number < 10:      #Check if number is even
                        break
        except BaseException:
            pass


    # loop for specific not used (position) input
    while True:
        try:
            get_position = input(message_position).lower().strip()      #get position from user
            if get_position not in used_letters:       # check if position used or not here
                if get_position in ["a","b","c","d","e","f","g","h","i"]:       # check if player position in board letters
                    break
        except BaseException:
            pass

    # assigning the number, position to a list variable 
    the_player_input = [get_number,get_position]
    return the_player_input

## Upadtes the values of the board
def update_display_board(the_player_input):

    # add input number in used_nums list, add input letter in used_letters
    used_nums.append(the_player_input[0])
    used_letters.append(the_player_input[-1])

    # Changing the value of the board with player input
    for row in board:
        for i in range(len(row)):       # a loop to change the specific number
            if row[i] == the_player_input[-1]:
                row[i] = the_player_input[0]
                break

## Possible winnig situations
def winning_situation():

    # all of these possibilities are vertical, horizontal and diagonally
    try:
        if board[0][0] + board[1][0] + board[2][0] == 15:
            return "win"
    except BaseException:
        pass
    try:
        if board[0][1] + board[1][1] + board[2][1] == 15:
            return "win"
    except BaseException:
        pass
    try:
        if board[0][2] + board[1][2] + board[2][2] == 15:
            return "win"
    except BaseException:
        pass
    try:
        if board[0][0] + board[0][1] + board[0][2] == 15:
            return "win"
    except BaseException:
        pass
    try:
        if board[1][0] + board[1][1] + board[1][2] == 15:
            return "win"
    except BaseException:
        pass
    try:
        if board[2][0] + board[2][1] + board[2][2] == 15:
            return "win"
    except BaseException:
        pass
    try:
        if board[0][0] + board[1][1] + board[2][2] == 15:
            return "win"
    except BaseException:
        pass
    try:
        if board[0][2] + board[1][1] + board[2][0] == 15:
            return "win"
    except BaseException:
        pass

## if game is draw
def finish_game():

    # Check if all numbers are used by summing nums from 1 to 9
    if sum(used_nums) == 45:
        return "Draw"

## Main Game
def game_main():
    
    while True:     # start a loop

        # PLAYER ONE...
        display_board()     #display the updated board.
        the_player_unput = get_input("One","odd")       #Get input from player one function call.
        update_display_board(the_player_unput)      #update the board function call.

        if winning_situation() == "win":        #see if there is a winner by its return value.
            display_board()     #display the updated board if player one is winner, then print player one wins.
            print("Player One Wins!")
            break       # break the loop when player one wins

        if finish_game() == "Draw": 
            display_board()     #display the updated board.
            print("Game Is Draw")     #if game is finished, print draw.
            break       #break the loop if draw


        # PLAYER TWO...
        display_board()     #display the updated board.
        the_player_unput = get_input("Two","even")      #get input from player two function call.
        update_display_board(the_player_unput)      #update the board function call.

        if winning_situation() == "win":      #see if there is a winner by its return value.
            display_board()     #display the updated board if player one is winner, then print player one wins.
            print("Player Two Wins!")
            break

## Start The Game 
game_main()