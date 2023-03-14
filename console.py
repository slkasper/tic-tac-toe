
#probably shouldn't use this file anymore.
# I used it to write this out as a script before refacturing

class Square:
    def __init__(self) -> None:
        #stores a value 
        self.symbol = None # x or o
        # method to check if empty

    def fill(self, symbol):
        if self.is_empty():
            self.symbol = symbol    

    def is_empty(self)->bool:
        #returns True if square is empty
        return self.symbol is None
    
    def __repr__(self) -> str:
        if not self.is_empty():
            return self.symbol
        else:
            return ' '
        
class Player:
    def __init__(self, id:int) -> None:
        #has turns
        #self.turns = turns
        #has id (player1 or player2)
        self.id = id
        self.symbol = None

    def set_symbol(self, input:str)->None:
        _input = input.upper()
        if _input == 'X' or _input == 'O':
            self.symbol = _input
        else:
            print('Not a valid entry. Try again. Please choose X or O')


class Board:
    def __init__(self) -> None:
        #stores the squares
        #check if all squares are full
        self.coord = [
            [Square(),Square(),Square()],
            [Square(),Square(),Square()],
            [Square(),Square(),Square()]
            ]
        
    def get_square_by_pos(self, pos: int) -> Square:
        map = {1: (0,0), 2: (0,1), 3: (0,2),
         4: (1,0), 5: (1,1), 6: (1,2),
         7: (2,0), 8: (2,1), 9: (2,2)
        }
        i,j = map[pos]
        return self.coord[i][j]

        
    def current_display(self)->None:
        # print the squares to the screen
        # show squares by position
        print(self.coord[0], self.coord[1], self.coord[2], sep="\n")

    def position_display(self)->None:
        print(
            [1,2,3],
            [4,5,6],
            [7,8,9], sep="\n"
        )
        
#         """
#  1 | 2 | 3
# -----------
#  1 | 2 | 3
# -----------
#  1 | 2 | 3
#         """

    def game_over(self, player:Player) -> bool:
        if self.is_win(player):
            print(f'{player} wins!!!')
            return True
        elif self.is_tie(player):
            print('Tie')
            return True
        return False
        

    def is_win(self, player: Player) -> bool:
        symbol = player.symbol
        cs = self.coord

        if (cs[0][0].symbol == cs[0][1].symbol == cs[0][2].symbol == symbol) or \
           (cs[1][0].symbol == cs[1][1].symbol == cs[1][2].symbol == symbol) or \
           (cs[2][0].symbol == cs[2][1].symbol == cs[2][2].symbol == symbol) or \
           (cs[0][0].symbol == cs[1][0].symbol == cs[2][0].symbol == symbol) or \
           (cs[0][1].symbol == cs[1][1].symbol == cs[2][1].symbol == symbol) or \
           (cs[0][2].symbol == cs[1][2].symbol == cs[2][2].symbol == symbol) or \
           (cs[0][0].symbol == cs[1][1].symbol == cs[2][2].symbol == symbol) or \
           (cs[0][2].symbol == cs[1][1].symbol == cs[2][0].symbol == symbol):
            return True
        else:
            return False

    def is_tie(self, player: Player) -> bool:
        x = [self.get_square_by_pos(n) for n in range(1,10) if self.get_square_by_pos(n).is_empty()]
        if not x:
            return True
        else:
            return False


class Game:
    def __init__(self) -> None:
        #needs players
        #needs a board
        #Game(player1,player2)
        pass



class Turn:
    def __init__(self, player1, player2) -> None:
        self.num = 0
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1

    def add_turn(self):
        self.num += 1
    
    def switch_player(self)->Player:
        self.add_turn()
        if self.current_player == player1:
            self.current_player = player2
        else:
            self.current_player = player1
        



if __name__ == "__main__":

    # ===============================================================
    # initialize the game
    # ===============================================================
    # what do you need to play a game?
    # board
    b = Board()
    # (and players below)

    # ===============================================================
    # initialize the players
    # ===============================================================
    # prompt to get user name
    # user inputs name
    # name gets stored in User? or Player?
    #prompt user to choose, X or O
# def enter_players(): # -> bool, Player, Player: # TODO WTF IS THIS
#     """returns true if players enter valid X,O values else false"""
    # ===============================================================
    #HACK comment out for faster testing - THIS WORKS!!!
    player1 = Player(1)
    player2 = Player(2)
    print('Which do you want to play, X or O')
    choice = input().upper()
    player1.set_symbol(choice)
    if choice == 'X':
        player2.set_symbol('O')
    elif choice == 'O':
        player2.set_symbol('X')
    else:
        False, player1, player2
    # # return True, player1, player2
    #     print("SOMETHING WENT WRONG... NEED TO DO THIS AGAIN!!!")
    # ===============================================================

    # player1, player2 = Player(1), Player(2)
    # player1.set_symbol("X")
    # player2.set_symbol("O")


    # valid = False
    # while not valid:
    #     valid, player1, player2 = enter_players()

    #TEST - if not X or O, it doesn't actually rerun until you put in the 
    # right value.  FIX
  
    #state that player 2 will be opposite choice
    #choices get stored in player.symbol
    print(f'Player 1 chose {player1.symbol}. ')
    print(f'Player 2 will be {player2.symbol}.')

    # HACK debugging
    #print(player1.__dict__)
    #print(player2.__dict__)
    # TEST NOTE: x,X,o,O,foo,1,' x', 'X ',

    # ===============================================================
    # play a turn (game-loop) THIS IS WORKING!!!
    # ===============================================================
    # TODO figure out whose turn it is... i.e. who is the current_player
    turn = Turn(player1, player2)

    gameover = False
    while not gameover:
        current_player = turn.current_player
        #display initial state of the board
        b.current_display()
        # prompt user/player1 to pick a square
        move_ok = False
        while move_ok == False:
            print(f'Player {current_player.id} pick a square.' )
            b.position_display()

            # * take choice, map to current_board_state
            pos_choice = int(input())
            current_square = b.get_square_by_pos(pos_choice)
            if current_square.is_empty():
                move_ok = True
            else:
                print('Square already taken. Please choose again.')

        current_square.fill(current_player.symbol)
        gameover = b.game_over(player=current_player)
        turn.switch_player()
    
