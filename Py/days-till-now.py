import arrow

# input dealings , takes file formattted YYYY MM DD
inputs = [map(int, lines.split()) for lines in open('Inputs/days-till-now.txt').read().splitlines()]

for y , m , d in inputs:
    future , today = arrow.now(), arrow.get(y, m, d)
    daysUntill =  (today - future).days + 1

    print("{} days from {} to {}".format(daysUntill, today.format("YYYY M D"), future.format("YYYY M D")))
