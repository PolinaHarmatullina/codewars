def points(games):
    win = 0
    tie = 0
    for iter in games:
        if iter[0]>iter[2]:
            win += 3
        elif iter[0]==iter[2]:
            tie += 1
    return win+tie