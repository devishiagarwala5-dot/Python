board={
    "1" : "  ","2" : "  ","3" : "  ","4" : "  ","5":"  ","6": "  ","7":"  ","8":"  ","9":"  "
    }
def win_check(board):
    if board["1"] == board["2"] == board["3"] == current_player+" ":
        print("winning first horizontal line by player ",current_player)      
        return True
    
def print_board():
    print(board["1"]+"|"+board["2"]+"|"+board["3"])
    print("--+--+--")
    print(board["4"]+"|"+board["5"]+"|"+board["6"])
    print("--+--+--")
    print(board["7"]+"|"+board["8"]+"|"+board["9"])
current_player="X"
ai="O"
game_on=True
counter=0
while game_on:
    print_board()
    counter=counter+1
    if counter>9:
        break
    print(f"{current_player} turn")
    pos=input("Which positíon do you want to go to between 1 to 9?")
    if board[pos]=="  ":
        board[pos]=current_player
        if current_player=='X':
            current_player='O'
        else:
            current_player='X'
    else:
        print("The chosen position is already occupied, please go to another one")