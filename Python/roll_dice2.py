import random
N = 1000     # no of experiments
ndice = 4    # no of dice
nsix = 2   # wanted no of dice with six eyes
M = 0                     # no of successful events
for i in range(N):
    six = 0               # how many dice with six eyes?
    for j in range(ndice):
        # Roll die no. j
        r = random.randint(1, 6)
        if r == 6:
            six += 1
    # Successful event?
    if six >= nsix:
        M += 1
p = float(M)/N
print 'probability:', p

