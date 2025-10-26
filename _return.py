from solve_maze_dfs import *
from solve_maze_bfs_physi import *

def mazes_main(): 
    while True:    
        plant(Entities.Bush)
        maze_area = 32 * 32
        use_item(Items.Weird_Substance, maze_area)
        solve_maze_bfs_physical()
        solve_maze_dfs()