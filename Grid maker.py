n,m = 4,12
Light_grid = [["X" for i in range(m)] for j in range(n)]

print(" "*3 + (" "*3).join(["{}".format(i) for i in range(1,m+1)]))
for j,bb in enumerate(Light_grid):
    print("{}: ".format(j+1)  + " | ".join(bb))
