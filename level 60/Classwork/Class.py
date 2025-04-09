def max_possible_score(points, seen):
    total_score = 0

    for key in points:
        value = points[key]

        if key in seen:
            total_score += value * 2
        else:
            total_score += value

    return total_score