class Dir:
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

def is_out_of_bounds(x, y, arr):
    return x < 0 or y < 0 or x >= len(arr[0]) or y >= len(arr)

def guard_walk(guard_start, guard_map):
    pos = guard_start.copy()
    count = 0
    current_dir = Dir.NORTH
    already_visited = {}
    while True:
        if (pos[0],pos[1]) not in already_visited:
            already_visited[(pos[0],pos[1])] = [current_dir]
            count += 1
        elif current_dir not in already_visited[(pos[0],pos[1])]:
            already_visited[(pos[0],pos[1])].append(current_dir)
        else:
            return True

        if guard_map[pos[1]][pos[0]] in [".", "^"]:
            guard_map[pos[1]] = guard_map[pos[1]][:pos[0]] + "X" + guard_map[pos[1]][pos[0]+1:]

        new_pos = pos.copy()
        match current_dir:
            case Dir.NORTH:
                new_pos[1] -= 1
            case Dir.EAST:
                new_pos[0] += 1
            case Dir.SOUTH:
                new_pos[1] += 1
            case Dir.WEST:
                new_pos[0] -= 1
        
        if (new_pos[0] == guard_start[0] and new_pos[1] == guard_start[1] and current_dir == Dir.NORTH):
            return True
        elif is_out_of_bounds(new_pos[0], new_pos[1], guard_map):
            break

        if guard_map[new_pos[1]][new_pos[0]] == "#":
            match current_dir:
                case Dir.NORTH:
                    current_dir = Dir.EAST
                case Dir.EAST:
                    current_dir = Dir.SOUTH
                case Dir.SOUTH:
                    current_dir = Dir.WEST
                case Dir.WEST:
                    current_dir = Dir.NORTH
        else:
            pos = new_pos

    # For Part 1 results
    # print(count)
    return False

gmap = []
with open('input.txt') as f:
    for line in f:
        gmap.append(line.strip())

gstart = [-1,-1]
for y in range(len(gmap)):
    if "^" in gmap[y]:
        gstart[0] = gmap[y].index("^")
        gstart[1] = y

guard_walk(gstart, gmap.copy())

count2 = 0
for j in range(len(gmap)):
    for i in range(len(gmap[j])):
        if gmap[j][i] == ".":
            gmap_copy = gmap.copy()
            gmap_copy[j] = gmap_copy[j][:i] + "#" + gmap_copy[j][i+1:]
            if guard_walk(gstart.copy(), gmap_copy):
                count2 += 1
print(count2)

