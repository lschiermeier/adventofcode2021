from numpy.core.fromnumeric import nonzero
from numpy.core.numeric import count_nonzero
from rich.traceback import install
import numpy as np

with open('day05/input.txt', 'r') as fp:
    lines = [x.strip() for x in fp.readlines()]

pairs = [l.split(" -> ") for l in lines]
pair_dicts = []
max_coord = 0

for a, b in pairs:
    ax, ay = a.split(",")
    bx, by = b.split(",")
    p = {"ax": int(ax), "ay": int(ay), "bx": int(bx), "by": int(by)}
    pair_dicts.append(p)
    max_coord = max(max(p.values()), max_coord)

grid = np.zeros((max_coord+1,max_coord+1), dtype=np.int64)
for p in pair_dicts:
    if p["ax"] == p["bx"]:
        # vertical line
        top = min(p["ay"],p["by"])
        bot = max(p["ay"],p["by"])
        for y in range(top,bot+1):
            grid[p["ax"],y] += 1
    elif p["ay"] == p["by"]:
        # horizontal line
        left = min(p["ax"],p["bx"])
        right = max(p["ax"],p["bx"])
        for x in range(left,right+1):
            grid[x,p["ay"]] += 1
    else:
        left = min(p["ax"],p["bx"])
        right = max(p["ax"],p["bx"])
        top = min(p["ay"],p["by"])
        bot = max(p["ay"],p["by"])
        for x in range(left,right+1):
            for y in range(top,bot+1):
                grid[x,y] += 1

print(len(np.where(grid>1)[0]))
