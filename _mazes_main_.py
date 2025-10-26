from solve_maze_dfs import *
from solve_maze_bfs_physi import *
from _return import *

#clear()

plant(Entities.Bush)
    
maze_area = 32 * 32
use_item(Items.Weird_Substance, maze_area)
solve_maze_bfs_physical()
solve_maze_dfs()
mazes_main()
    