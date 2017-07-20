#76958230 Kristen DeVore Lab 12:30-1:50
import gamelogic

def first_turn() -> str:
    '''intakes first turn
    '''
    user_input = input()
    return user_input

def make_board_readable(game_board: [[str]]) -> None:
    '''makes board readable
    '''
    
    for row in game_board:
        new_str = ''
        for col in row:
            new_str += col + ' '
        print(new_str)

def intake_winner_state() -> str:
    '''reads winner state
    '''
    winner_input = input()
    return winner_input






if __name__ == '__main__':
    print("FULL")

    game_state =  gamelogic.GameState()
    rows_insert = game_state.read_rows()
    columns_insert = game_state.read_columns()
    game_state.create_board(rows_insert, columns_insert)
    game_state.give_turn(first_turn())
    winner_input = intake_winner_state()
    board_setup = game_state.set_up_board_from_input()
    game_state.count_tiles_for_interface()
    make_board_readable(board_setup)
    game_state.assign_winner_type(winner_input)
 #   game_state.declare_winner()
    end_game = game_state.end_game()
    turn = game_state.return_turn()
  #  print("TURN: " + str(turn))
    if game_state.switch_turn_if_player_has_no_moves() == False:
        game_state.opposite_next_turn()
        game_state.switch_turn_if_player_has_no_moves()
        if game_state.switch_turn_if_player_has_no_moves() == False:
 #           make_board_readable(board_setup)
 #           game_state.count_tiles_for_interface()
            game_state.declare_winner()
            
    #               make_board_readable(new_board)
    #               game_state.count_tiles_for_interface()
 #              break
    else:
        print("TURN: " + str(turn))
        while end_game != False: #winner not present
            numbers = input()
            final_numbers = numbers.split(' ')
            row = int(final_numbers[0])
            column = int(final_numbers[1])
            game_state.find_tile_spots()
            game_state.see_value()
            if game_state.switch_turn_if_player_has_no_moves() == False:
                game_state.opposite_next_turn()
                game_state.switch_turn_if_player_has_no_moves()
                if game_state.switch_turn_if_player_has_no_moves() == False:
 #                   make_board_readable(new_board)
 #                   game_state.count_tiles_for_interface()
                    game_state.declare_winner()
                    break
 #               make_board_readable(new_board)
 #               game_state.count_tiles_for_interface()
                #break
            else:
                if game_state.return_bool_for_move(row, column) == True:
                    print("VALID")

                    game_state.move_by_user()
                    game_state.flippable_coordinates()
                    new_board = game_state.flip_board()
                    game_state.count_tiles_for_interface()
                    make_board_readable(new_board)
                    game_state.switch_turn()
                    next_turn = game_state.return_turn()
                    print("TURN: " + str(next_turn))
                    game_state.reset_flip_coordinates()
                    if game_state.switch_turn_if_player_has_no_moves() == False:
                
 #                       print("TURN: " + game_state.return_turn())
                        game_state.opposite_next_turn()
                        print("TURN: " + game_state.return_turn())
                        game_state.switch_turn_if_player_has_no_moves()
                        if game_state.switch_turn_if_player_has_no_moves() == False:
 #                           make_board_readable(new_board)
#                            game_state.count_tiles_for_interface()
                            game_state.declare_winner()
                            break

                else:
                    
                    if game_state.switch_turn_if_player_has_no_moves() == False:
                        game_state.reset_flip_coordinates()
                        game_state.opposite_next_turn()
 #                       print("TURN: " + game_state.return_turn())
                        game_state.switch_turn_if_player_has_no_moves()
                        if game_state.switch_turn_if_player_has_no_moves() == False:
 #                           make_board_readable(new_board)
#                            game_state.count_tiles_for_interface()
                            game_state.declare_winner()
                            break
                    else:
                        print('INVALID')

 

