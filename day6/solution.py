class Dir:
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

def is_out_of_bounds(x, y, arr):
    return x < 0 or y < 0 or x >= len(arr[0]) or y >= len(arr)

guard_map = []
with open('input.txt') as f:
    for line in f:
        guard_map.append(line.strip())

guard_start = [-1,-1]
for y in range(len(guard_map)):
    if "^" in guard_map[y]:
        guard_start[0] = guard_map[y].index("^")
        guard_start[1] = y

pos = guard_start.copy()
count = 0
current_dir = Dir.NORTH
while True:
    if guard_map[pos[1]][pos[0]] != "X":
        count += 1
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
    
    if (new_pos[0] == guard_start[0] and new_pos[1] == guard_start[1] and current_dir == Dir.NORTH) or is_out_of_bounds(new_pos[0], new_pos[1], guard_map):
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

print(count)