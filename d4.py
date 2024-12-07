import re
input_file="inputs/input_d4.txt"

with open(input_file, 'r') as f:
    grid = f.read().splitlines()

fliplr = lambda x: [row[::-1] for row in x]
transpose = lambda x: ["".join(row) for row in zip(*x)]
get_shifts = lambda x: ["*"*shift+s+"*"*(len(x[0])-shift-1) for s,shift in zip(x,range(len(x[0])))]
get_diags = lambda x: transpose(get_shifts(x))
rot = lambda x: transpose(fliplr(x))
count_substr = lambda x: sum([len(re.findall("XMAS", s)) for s in x])
lr = grid
rl = fliplr(grid)
ud = transpose(grid)
du = fliplr(transpose(grid))
d1 = get_diags(grid)
d2 = get_diags(fliplr(grid))
d3 = fliplr(d1)
d4 = fliplr(d2)
print("Part 1:", sum([count_substr(g) for g in [lr, rl, ud, du, d1, d2, d3, d4]]))


def count_x_mas(grid):
    count = 0
    x = [r"M.S",r".A.",r"M.S"]
    for i in range(len(grid)-2):
        for x_rot in [x, rot(x), rot(rot(x)), rot(rot(rot(x)))]:
            x_aug = [f"(?=({s}))" for s in x_rot]
            matches_0 = [m.start() for m in re.finditer(x_aug[0], grid[i])]
            matches_1 = [m.start() for m in re.finditer(x_aug[1], grid[i+1])]
            matches_2 = [m.start() for m in re.finditer(x_aug[2], grid[i+2])]
            count += len(set(matches_0).intersection(set(matches_1),set(matches_2)))
    return count

print("Part 2: ", count_x_mas(grid))


