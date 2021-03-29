
import numpy as np

grid = [[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]]

def valid(row,col,num) :
    global grid
    for i in range(9):
        if grid[row][i] == num :
            return False
    for i in range(9):
        if grid[i][col] == num :
            return False
    y = (row//3)*3    
    x = (col//3)*3
    for i in range(3):
        for j in range(3):
            if grid[y + i][x + j] == num : 
                return False
    return True        

def solver():
    global grid
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0 :
                for num in range(1,10):
                    if valid(row,col,num):
                        grid[row][col] = num
                        solver()
                        grid[row][col] = 0
                return        
    print(np.matrix(grid))
    input('Press any key to see if there are any other solutions')

solver()            