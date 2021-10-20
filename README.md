# didactic-memory-Sudoku
 Your goal for this challenge is to write a Python function to solve Sudoku puzzles. 
## Challenge
Write a python function to solve a sudoku puzzle. 

## Input
Represent the Sudoku grid as a two-dimensional list of lists. 
It should have nine sub-lists, representing the rows, with nine elements each, and use the number zero to indicate empty spaces. 

You solve_sudoku function should take a new, partially filled in puzzle as input, and then return a two-dimensional list representing the solution to that puzzle with all the spaces filled in, one through nine. 

## Output 

 5  3  *  |  *  7  *  |  *  *  * 
 6  *  *  |  1  9  5  |  *  *  * 
 *  9  8  |  *  *  *  |  *  6  * 
---------------------------------
 8  *  *  |  *  6  *  |  *  *  3 
 4  *  *  |  8  *  3  |  *  *  1 
 7  *  *  |  *  2  *  |  *  *  6 
---------------------------------
 *  6  *  |  *  *  *  |  2  8  * 
 *  *  *  |  4  1  9  |  *  *  5 
 *  *  *  |  *  8  *  |  *  7  9 


 5  3  4  |  6  7  8  |  9  1  2 
 6  7  2  |  1  9  5  |  3  4  8 
 1  9  8  |  3  4  2  |  5  6  7 
---------------------------------
 8  5  9  |  7  6  1  |  4  2  3 
 4  2  6  |  8  5  3  |  7  9  1 
 7  1  3  |  9  2  4  |  8  5  6 
---------------------------------
 9  6  1  |  5  3  7  |  2  8  4 
 2  8  7  |  4  1  9  |  6  3  5 
 3  4  5  |  2  8  6  |  1  7  9 
