
# dealing with input file and orginizing the format of input
inputs = [line.rstrip('\n') for line in open('Inputs/asci-flood-fill.txt')]
dimensions = inputs.pop(0).split()
fillInfo = inputs.pop(len(inputs) - 1 ).split()
grid = [list(line) for line in inputs]

# assigning all variables needed to fill
w , h = map(int ,dimensions)
x , y , changeTo = list(fillInfo)
x , y = int(x) , int(y) 
base = grid[x][y]

# recursive solution
def fill(x, y):
    if grid[y][x] == base:
        grid[y][x] = changeTo
        for nx, ny in [((x+1)%w, y), ((x-1)%w, y), (x, (y+1)%h), (x, (y-1)%h)]:
            fill(nx, ny)
fill(x, y)

#final print
for line in grid:
        print("".join(line))
