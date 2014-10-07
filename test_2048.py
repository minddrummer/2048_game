"""
A simple testing suite for 2048 game
Note that tests are not exhaustive and should be supplemented
"""

import poc_simpletest

def run_test(game_class):
    """
    Some informal testing code
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    #game = game_class()
    # test the init
    height = 4
    width = 5
    game = game_class(height, width)
    suite.run_test(game.height, 4, "Test #0: height") 
    suite.run_test(game.width, 5, "Test #1: width")
    suite.run_test(game.grids, [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], "Test #2: grids")
    #suite.run_test(game.reset(), [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], "Test #2: grids")

    #test str function in twentyfortyeight
    height1 = 3
    width1 = 4
    game1 = game_class(height1, width1)
    suite.run_test(str(game1), '[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]', 'Test #3: str function')
    
    #test setting tiles and get tile in the class
    h2 = 4
    w2 = 5
    game2 = game_class(h2,w2)
    game2.set_tile(1,1,99)
    game2.set_tile(1,3,40)
    game2.set_tile(3,4, 21)
    suite.run_test(game2.get_tile(0,0), 0, 'Test #4: expect 0')
    suite.run_test(game2.get_tile(1,1), 99, 'Test #5:expect 99')
    suite.run_test(game2.get_tile(1,3), 40, 'Test #6:expect 40')
    suite.run_test(game2.get_tile(3,4), 21, 'Test #7:expect 21')
    
    
    # check the str and get_num_seeds methods
    #config1 = [0, 0, 1, 1, 3, 5]    
    #game.set_board(config1)   
    #suite.run_test(str(game), str([5, 3, 1, 1, 0, 0]), "Test #1a: str")
    #suite.run_test(game.get_num_seeds(1), config1[1], "Test #1b: get_num_seeds")
    #suite.run_test(game.get_num_seeds(3), config1[3], "Test #1c: get_num_seeds")
    #suite.run_test(game.get_num_seeds(5), config1[5], "Test #1d: get_num_seeds")
    
    ## test is_game_won
    #config1 = [0, 0, 1, 1, 3, 5]    
    #game.set_board(config1)
    #suite.run_test(game.is_game_won(), False, "Test #2a: is_game_won.")
    #config2 = [1, 0, 0]
    #game.set_board(config2)
    #suite.run_test(game.is_game_won(), True, "Test #2b: is_game_won.")                     

    ## check the effect of a legal move, test for mutation of config
    #config1 = [0, 0, 1, 1, 3, 5]    
    #game.set_board(config1)
    #suite.run_test(game.is_legal_move(0), False, "Test #3a: is_legal_move")
    #suite.run_test(game.is_legal_move(5), True, "Test #3b: is_legal_move")
    #game.apply_move(5)
    #suite.run_test(str(game), str([0, 4, 2, 2, 1, 1]), "Test #3c: apply_move.")
    #suite.run_test(config1, [0, 0, 1, 1, 3, 5], "Test #3d: mutation of config.")

    #config3 = [1, 1, 2, 2, 4, 0]    
    #game.set_board(config3)
    ## check the effect of an illegal move
    #suite.run_test(game.is_legal_move(3), False, "Test #4a: is_legal_move")
    #game.apply_move(3)
    #suite.run_test(str(game), str([0, 4, 2, 2, 1, 1]), "Test #4b: apply_move.")

    #config1 = [0, 0, 1, 1, 3, 5]    
    ## test choose_move and apply_move
    #game.set_board(config1)
    #move = game.choose_move()
    #suite.run_test(move, 5, "Test 5a: choose_move.")
    #game.apply_move(move)
    #suite.run_test(str(game), str([0, 4, 2, 2, 1, 1]), "Test 5b: apply_move.")
    #config6 = [0, 0, 1]
    #game.set_board(config6)
    #move = game.choose_move()
    #suite.run_test(move, 0, "Test 5c: choose_move.")

    ## test plan_moves
    #config3 = [1, 1, 2, 2, 4, 0]    
    #game.set_board(config3)
    #move_list = game.plan_moves()
    #suite.run_test(move_list, [1, 2, 1, 4, 1, 3, 1, 2, 1], "Test 6a: plan_moves.")
    #for move in move_list:
        #game.apply_move(move)
    #suite.run_test(str(game),  str([0, 0, 0, 0, 0, 10]), "Test 6b: apply_move.")
    #config5 = [0, 0, 0, 3]    
    #game.set_board(config5)
    #move_list = game.plan_moves()
    #suite.run_test(move_list,  [3, 1], "Test 6c: plan_move.")
    
    # report number of tests and failures
    suite.report_results()
