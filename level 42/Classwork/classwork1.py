def points(matches):
    points = 0
    for match in matches:
        x, y = match.split(':')
        if int(x) > int(y):
            points += 3 
        elif int(x) < int(y):
            points += 0 
        else:
            points += 1 
    return points