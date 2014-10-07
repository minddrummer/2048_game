"""
Clone of 2048 game.
"""

import poc_2048_gui        

from random import randint 
# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.    
OFFSETS = {UP: (1, 0), 
           DOWN: (-1, 0), 
           LEFT: (0, 1), 
           RIGHT: (0, -1)} 
   
def merge(line):
    """
    Helper function that merges a single row or column in 2048
    line should be a list; and if there is blank position, should put 0s
    """
    #Start with a result list that contains the same number of 0's as the length of the line argument.
    #Iterate over the line input looking for non-zero entries. For each non-zero entry, put the value into the next available entry of the result list (starting at position 0).
    #create an empty 0 list    
    init_lst = [0]*len(line)
    res_lst = []
    #remove 0s from line first
    line = filter(lambda a: a != 0, line)
    if len(line) == 0:
        res_lst = init_lst[:]
        return res_lst
    
    while len(line) >= 1:
        if len(line) == 1:
            merge_ele = line[0]
            res_lst.append(merge_ele)
            line.pop(0)            
        elif line[0] == line[1]:
            merge_ele = line[0] + line[1]
            res_lst.append(merge_ele)
            #pop twice
            line.pop(0)
            line.pop(0)
        else:
            merge_ele = line[0]
            res_lst.append(merge_ele)
            line.pop(0)       
    
    if len(res_lst) < len(init_lst):
        add_0 = [0]*(len(init_lst)-len(res_lst))
        res_lst = res_lst + add_0 
    
    return res_lst

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self.height = grid_height
        self.width = grid_width
        #could call other methods in the class in the __init__ function!!
        #like below, using self.reset() to reset the grid of the game
        #better put all the attributes in the init function, it is more clear
        self.grids = []
        self.reset()  
    
        up_lst = []
        down_lst =[]
        right_lst =[]
        left_lst = []
        
        for i in range(self.width):
            up_ele = (0,i)
            down_ele = (self.height-1, i)
        
            up_lst.append(up_ele)
            down_lst.append(down_ele)
        for j in range(self.height):
            right_ele = (j, self.width - 1)
            left_ele = (j, 0)
        
            right_lst.append(right_ele)
            left_lst.append(left_ele)
        
        self.direct = {UP:up_lst, DOWN:down_lst, RIGHT:right_lst, LEFT: left_lst}
     
    def reset(self):
        """
        Reset the game so the grid is empty.
        reset the grid to have all 0 for each grid cell
        """
        #write a loop to set all 0s
        self.grids = []
        for i in range(self.height):
            self.grids.append([0]*self.width)
        #return self.grids
        
    
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        grids_format = ''
        for i in range(self.height):
            grids_format = grids_format + '\n' + str(self.grids[i])
        print grids_format
        return str(self.grids)        

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self.height
    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self.width
        
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # first create an initial list for the directions, as I have to reshape the list to match the merge fucntion
        #then given the direction UP etc, reconstruct the list of grids
        offsets = OFFSETS[direction]
        starting_lst = self.direct[direction]
        if direction == 1:
            for i in range(len(starting_lst)):
                starting_grid = starting_lst[i]
                pos_h = starting_grid[0]
                pos_w = starting_grid[1]
                temp_lst = []
                grid_pos = []
                while pos_h < self.height:
                    grid_pos.append((pos_h, pos_w))
                    temp_lst.append(self.grids[pos_h][pos_w])
                    pos_h = pos_h + offsets[0]
                    pos_w = pos_w + offsets[1]
                merge_lst = merge(temp_lst)
                for j in range(len(grid_pos)):
                    self.grids[grid_pos[j][0]][grid_pos[j][1]] = merge_lst[j]
        elif direction == 2:
            for i in range(len(starting_lst)):
                starting_grid = starting_lst[i]
                pos_h = starting_grid[0]
                pos_w = starting_grid[1]
                temp_lst = []
                grid_pos = []
                while pos_h >= 0:
                    grid_pos.append((pos_h, pos_w))
                    temp_lst.append(self.grids[pos_h][pos_w])
                    pos_h = pos_h + offsets[0]
                    pos_w = pos_w + offsets[1]
                merge_lst = merge(temp_lst)
                for j in range(len(grid_pos)):
                    self.grids[grid_pos[j][0]][grid_pos[j][1]] = merge_lst[j]
                    
        elif direction ==3:
            for i in range(len(starting_lst)):
                starting_grid = starting_lst[i]
                pos_h = starting_grid[0]
                pos_w = starting_grid[1]
                temp_lst = []
                grid_pos = []
                while pos_w < self.width:
                    grid_pos.append((pos_h, pos_w))
                    temp_lst.append(self.grids[pos_h][pos_w])
                    pos_h = pos_h + offsets[0]
                    pos_w = pos_w + offsets[1]
                merge_lst = merge(temp_lst)
                for j in range(len(grid_pos)):
                    self.grids[grid_pos[j][0]][grid_pos[j][1]] = merge_lst[j]   
        else:
            for i in range(len(starting_lst)):
                starting_grid = starting_lst[i]
                pos_h = starting_grid[0]
                pos_w = starting_grid[1]
                temp_lst = []
                grid_pos = []
                while pos_w >= 0:
                    grid_pos.append((pos_h, pos_w))
                    temp_lst.append(self.grids[pos_h][pos_w])
                    pos_h = pos_h + offsets[0]
                    pos_w = pos_w + offsets[1]
                merge_lst = merge(temp_lst)
                for j in range(len(grid_pos)):
                    self.grids[grid_pos[j][0]][grid_pos[j][1]] = merge_lst[j]  
        self.new_tile()
        
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # first select the grid 
        # then generate a value either 2 or 4
        pos_0 = []
        for h in range(self.height):
            for w in range(self.width):
                if self.grids[h][w] == 0:
                    pos_0.append((h,w))
                    
        if len(pos_0) == 0:
            message = 'You lose!'
            return message
        else:
            high_end = len(pos_0) - 1
            low_end = 0
            #pos is the postion in pos_0
            pos = pos_0[randint(low_end, high_end)]
            #pos[0] is the height; pos[1] is the width
            #apply it to self.grids, and find the corresponding row and col
            #then generate a value either 2 or 4
            decision_thres = randint(0,9)
            if decision_thres == 9:
                self.grids[pos[0]][pos[1]] = 4
            else:
                self.grids[pos[0]][pos[1]] = 2
            
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """        
        # replace with your code
        self.grids[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """        
        # get the specific grid number in the row and col
        #self.grids is a list of lists
        return self.grids[row][col] 
 
    
poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
#import test_2048
#test_2048.run_test(TwentyFortyEight)


