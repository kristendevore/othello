#76958230 Kristen DeVore Lab 12:30 - 1:50

class GameState:
    def __init__(self):
        self._rows = 0
        self._columns = 0
        self._game_board = []
        self._turn = ''
        self._b_tiles = []
        self._w_tiles = []
        self._valid_white_tiles = []
        self._valid_black_tiles = []
        self._possible_moves_for_turn = []
        self._bool = ''
        self._black_directions_for_tiles = []
        self._white = 'W'
        self._black = 'B'
        self._empty = '.'
        self._valid_directions_for_move = []
        self._row_move = 0
        self._column_move = 0
        self._black_moves_dictionary = {}
        self._white_moves_dictionary = {}
        self._flippable_coordinates = []
        self._black_tiles_total = 0
        self._white_tiles_total = 0
        self._winner_type = ''
        

        
 #       self._move_column = 0
 #       self._move_row = 0 
    def read_rows(self) -> int:
        '''reads rows from input
        '''
        while True:
            new_input = int(input())

            if new_input <= 16:
                if new_input % 2 == 0:
                    self._rows = new_input
                    return self._rows
                else:
                    pass
            else:
                pass
    def read_columns(self) -> int:
        '''reads columns from input
        '''
        while True:
            new_input = int(input())

            if new_input <= 16:
                if new_input % 2 == 0:
                    self._columns = new_input
                    return new_input
                else:
                    pass
            else:
                pass
    def create_board(self, rows, columns) -> [[str]]:
        '''creates the board for the object
        '''
        rows = self._rows
        columns = self._columns
        for row in range(rows):
            self._game_board.append([])
            for column in range(columns):
                self._game_board[-1].append('.')
            

        return self._game_board

    def set_up_board_from_input(self)-> [[str]]:
        '''sets up board from user input however they wish to input the board
        '''
        # change to rows, userinput as other parameters
        rows = self._rows
        new = []
        final = []
        
        while rows != 0:
            for item in range(rows):
                user_input = input()
                new.append(user_input.strip())
                
            for i in new:
                final.append(i.split())
                
            rows = rows - 1
            self._game_board = final

            return self._game_board
    
     
   
    def find_tile_spots(self) -> list:
        '''finds all black and white tiles on board
        '''
        gameboard = self._game_board
        list_of_b_tiles = []
        list_of_w_tiles = []
        
        for row in range(len(gameboard)):
            column = 0 
            for col in gameboard[row]:
                if col == self._black:
                    list_of_b_tiles.append((row, column)) #board_spot
                elif col == self._white:
                    list_of_w_tiles.append((row, column))
                column += 1
        self._b_tiles = list_of_b_tiles
        self._w_tiles = list_of_w_tiles
        return list_of_b_tiles, list_of_w_tiles


            

    def check_tile_if_turn_white(self, tile: tuple) -> list:
        '''if the turn is white, checks all white tiles to see where valid moves can be made,
            returns list of valid places on board W player can put a piece
        '''
        list_of_directions = [(0,1), (0, -1), (1,0), (-1,0), (1,1), (-1, -1), (1, -1), (-1, 1)]
        valid_white_tiles = []
        white_tiles_for_directions = []
        for direction in list_of_directions:
            row = tile[0] + direction[0]
            column = tile[1] + direction[1]
            while row in range(self._rows) and column in range(self._columns):
                
                if self._game_board[row][column] == self._white:
                    pass
                
                elif self._game_board[row][column] == self._empty:
                    break


                elif self._game_board[row][column] == self._black:
        
                    if row + direction[0] in range(self._rows):
                        if column + direction[1] in range(self._columns):
                            if self._game_board[row +direction[0]][column+ direction[1]] == self._empty:
                                new_variable = row+direction[0], column +direction[1]
                                second_variable = direction[0], direction[1]
                                self._white_moves_dictionary[new_variable] = second_variable
                       
                                valid_white_tiles.append((row+direction[0],column+direction[1]))
                                
                                
                row += direction[0]
                column += direction[1]
        self._valid_white_tiles = valid_white_tiles
        return valid_white_tiles

    
                
    def check_tile_if_turn_black(self, tile:tuple) -> list:
        '''if the turn is black, checks all black tiles to see where valid moves can be made,
            returns list of valid places on board B player can put a piece
        '''

        list_of_directions = [(0,1), (0, -1), (1,0), (-1,0), (1,1), (-1, -1), (1, -1), (-1, 1)]
        valid_black_tiles = []
#        black_tiles_for_directions = []
        list_of_items_for_flip = []
#        directions_for_tiles = [] 
        
        for direction in list_of_directions:
            
            row = tile[0] + direction[0]
            column = tile[1] + direction[1]
            while row in range(self._rows) and column in range(self._columns):
                if self._game_board[row][column] == self._black:
                     pass

                elif self._game_board[row][column] == self._empty:
                    break
    
                
                elif self._game_board[row][column] == self._white:
                    if row + direction[0] in range(self._rows):
                        if column + direction[1] in range(self._columns):
                            if self._game_board[row +direction[0]][column+ direction[1]] == self._empty:
                                new_variable = row+direction[0], column +direction[1]
                                second_variable = direction[0], direction[1]
                                self._black_moves_dictionary[new_variable] = second_variable
 #                               self._black_moves_dictionary.update(
                                
       
                                
                       
                                valid_black_tiles.append((row+direction[0],column+direction[1]))
#                                black_tiles_for_directions.append((row+direction[0], column+direction[1]))
 #                               list_of_directions.append((direction[0], direction[1]))

                                                                    
                row += direction[0]
                column += direction[1]
        self._valid_black_tiles = valid_black_tiles
#        self._black_directions_for_tiles = black_tiles_for_directions
 #       print("DICTIONARY")
        #print(self._black_moves_dictionary)
                                                                                                                           
        return valid_black_tiles

                
    
 
    def see_value(self) -> list:
        '''iterates through list of b tiles and w tiles depending on the turn, returns list of all possible moves after
        iterating through all the tiles
        '''
        possible_moves_for_turn = []
        if self._turn == self._black:
            tiles = self._b_tiles
            for tile in tiles:
                possible_moves_for_turn.append(self.check_tile_if_turn_black(tile))
            self._possible_moves_for_turn = possible_moves_for_turn
            return possible_moves_for_turn
        elif self._turn == self._white:
            tiles = self._w_tiles
            for tile in tiles:
                possible_moves_for_turn.append(self.check_tile_if_turn_white(tile))
            self._possible_moves_for_turn = possible_moves_for_turn
            return possible_moves_for_turn
        
    def return_list_for_bool_function(self) -> list:
        '''unpacks list of list of tuples so next function can return bool to see
        if the user input is a valid move
        '''
        list_of_moves = self._possible_moves_for_turn
        final_moves = []
        for moves in list_of_moves:
            final_moves += moves
        self._possible_moves_for_turn = final_moves
        return final_moves
            
    def return_bool_for_move(self, row: int, column:int) -> bool:
        '''if move is valid, return True. if move is invalid, return False
        '''
        self.return_list_for_bool_function()
        new_move = (row-1, column-1)
        list_of_moves = self._possible_moves_for_turn
        if new_move in list_of_moves:
            self._bool =  True
            self._row_move = row-1
            self._column_move = column-1

            return self._bool
        else:
            self._bool = False
            return self._bool
    

    def flippable_coordinates(self) -> [tuple]:
        '''returns list of flippable coordinates
        '''
        list_of_directions = [(0,1), (0, -1), (1,0), (-1,0), (1,1), (-1, -1), (1, -1), (-1, 1)]

        for direction in list_of_directions:
         
            row = self._row_move
            column = self._column_move
            row = row - direction[0]
            column = column - direction[1]
            flag =False
            listy =[]

            while row in range(self._rows) and column in range(self._columns):

                if self._game_board[row][column] == self._empty:
                    flag = True
                    break
                elif self._game_board[row][column] != self._turn:
                    new = row, column
                    listy.append(new)
                    row -= direction[0]
                    column -=direction[1]
                    if not (row in range(self._rows) and column in range(self._columns)):
                        flag=True
                
 
                else:
                    break
            if flag==False:
                self._flippable_coordinates.extend(listy)

                
   #     print("WE IN THIS")
 #       print(self._flippable_coordinates)

    def reset_flip_coordinates(self) -> list:
        '''resets flip coordinates
        '''
        self._flippable_coordinates = []
        return self._flippable_coordinates

##
    def flip_board(self) -> [[str]]:
        '''flips coordinates
        '''
        for coordinate in self._flippable_coordinates:
            row = coordinate[0]
            col = coordinate[1]
           # print(row, col)
            self._game_board[row][col] = self._turn
            #print(self._game_board)
        return self._game_board

     
    def move_by_user(self) -> [[str]]:
        '''puts user input on board if bool is true
        '''
        row = self._row_move
        column = self._column_move

        if self._bool == True:
            self._game_board[row][column] = self._turn
            
            
            return self._game_board
  

    def count_tiles_for_interface(self) -> None:
        '''counts tiles
        '''
        self._black_tiles_total = 0
        self._white_tiles_total = 0

        for row in self._game_board:
            for col in row:
                if col == self._black:
                    self._black_tiles_total += 1
                elif col == self._white:
                    self._white_tiles_total += 1
            
        print("B: " + str(self._black_tiles_total) + " W: " + str(self._white_tiles_total))
        
        
                    

    def opposite_turn(self) -> str:
        '''returns opposite turn
        '''
        if self._turn == self._black:
            return self._white
        elif self._turn == self._white:
            return self._black
    def give_turn(self, turn:str) -> str:
        '''gives turn of who starts off
        '''
        self._turn = turn
        return self._turn
    def return_turn(self) -> str:
        '''returns turn
        '''
        return self._turn
    def switch_turn(self) -> str:
        '''switches turn
        '''
        turn = self._turn
        if self._bool == True:
            if turn == 'B':
                self._turn = 'W'
            elif turn == 'W':
                self._turn = 'B'

    def opposite_next_turn(self) -> str:
        '''opposite turn for another purpose
        '''
        if self._turn == 'B':
            self._turn = 'W'
        elif self._turn == 'W':
            self._turn = 'B'
    def end_game_state(self) -> None:
        '''ends game
        '''

        if self._black_tiles_total > self._white_tiles_total:
            print("WINNER: BLACK")
        elif self._black_tiles_total < self._white_tiles_total:
            print("WINNER: WHITE")
        elif self._black_tiles_total == self._white_tiles_total:
            print("WINNER: NONE")
            
    def reverse_end_game_state(self) -> None:
        '''opposite of end game state
        '''
        if self._black_tiles_total > self._white_tiles_total:
            print("WINNER: WHITE")
        elif self._black_tiles_total < self._white_tiles_total:
            print("WINNER: BLACK")
        elif self._black_tiles_total == self._white_tiles_total:
            print("WINNER: NONE")
    def assign_winner_type(self, user_input: str) -> str:
        '''assigns winner type
        '''
        self._winner_type = user_input
        return self._winner_type

    def declare_winner(self) -> str:
        '''declares winner
        '''
        if self._winner_type == '>':
            self.end_game_state()
        elif self._winner_type == '<':
            self.reverse_end_game_state()

    def switch_turn_if_player_has_no_moves(self) -> bool:
        '''switches turn if player has no moves
        '''
        self.find_tile_spots()
        self.see_value()

        for item in self._possible_moves_for_turn:
        
            if item != []:
                return True
      
    
        return False
            


    def end_game(self) -> bool:
        '''end game
        '''
        if self._possible_moves_for_turn == []:
            self.switch_turn()
            self.find_tile_spots()
            self.see_value()
            if self._possible_moves_for_turn == []:
                self.declare_winner()
                return False
