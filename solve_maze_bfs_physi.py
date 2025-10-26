def solve_maze_bfs_physical():
    start_pos = (get_pos_x(), get_pos_y())
    queue = [start_pos]
    visited = {start_pos: True}
    parent = {start_pos: None}
    
    directions = [North, East, South, West]
    opposites = {North: South, East: West, South: North, West: East}
    head = 0

    while head < len(queue):
        target_pos = queue[head]
        head += 1

        if get_entity_type() == Entities.Treasure:
            quick_print("Found Treasure!")
            return

        for direction in directions:
            if move(direction):
                next_pos = (get_pos_x(), get_pos_y())
                if next_pos not in visited:
                    visited[next_pos] = True
                    parent[next_pos] = (target_pos, direction)
                    queue.append(next_pos)
                move(opposites[direction])    