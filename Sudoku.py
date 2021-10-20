from itertools import product

def sudoku(puzzle):
    for (row, col) in product(range(0,9), repeat=2):#uses the product function from itertools to iterate through every combination of indices
        if puzzle[row][col] == 0: # find an unassigned cell
            for num in range(1,10): #for loop to sequentially place numbers one through nine
                allowed = True # check if num is allowed in row/col/box
                for i in range(0,9):#check if the num doesn't already exist
                    if (puzzle[i][col ] == num) or (puzzle[row][i] == num):
                        allowed = False; break # not allowed in row or col
                for (i, j) in product(range(0,3), repeat=2): # check to see if num exists within the sub-grid
                    if puzzle[row-row%3+i][col-col%3+j] == num:
                        allowed = False; break # not allowed in box
                if allowed: # test passes     
                    puzzle[row][col] = num # placed in cell 
                    if trial := sudoku(puzzle): #recursively calling the sudoku function on the update puzzle grid
                        return trial #return the completed grid
                    else: 
                        puzzle[row][col] = 0 # reset the cell to empty so the for loop can try more numbers 
            return False # could not place a number in this cell
    return puzzle


