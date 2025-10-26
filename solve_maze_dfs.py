def solve_maze_dfs():
    visited = {}
    stack = [((get_pos_x(), get_pos_y()), None)]
    visited[(get_pos_x(), get_pos_y())] = True
    directions = [North, East, South, West]
    opposites = {North: South, East: West, South: North, West: East}

    while len(stack) > 0:
        if get_entity_type() == Entities.Treasure:
            harvest()
            quick_print("Found Treasure!")
            return
        (current_x, current_y), came_from = stack[-1]
        moved_forward = False

        for direction in directions:
            next_x, next_y = current_x, current_y
            if direction == North:
                next_y += 1
            if direction == South:
                next_y -= 1
            if direction == East:
                next_x += 1
            if direction == West:
                next_x -= 1

            if (next_x, next_y) not in visited:
                if move(direction):
                    visited[(next_x, next_y)] = True
                    stack.append(((next_x, next_y), direction))
                    moved_forward = True
                    break

        if not moved_forward:
            stack.pop()
            if len(stack) > 0:
                move(opposites[came_from])            