# handles inputs, makes array of single chars, in a grid style
data = [list(lines) for lines in open('Inputs/metro-tile-meltdown.txt').read().splitlines()]
base = '.'
w, h = len(data[0]), len(data)
starts = []
print w , h

for y in range(h):
    for x in range(w):
        c = data[y][x]
        if c != base and (data[y-1][x] != c and data[y][x - 1] != c):
            starts.append([c, x, y])

for c, x_start, y_start in starts:
    x, y = x_start, y_start
    while data[y][x] == c:
        x += 1
    while data[y][x-1] == c:
        y += 1
    print '{} starts at {} , {} and its dimensions are {}x{}'.format(c, x_start, y_start, x , y)


