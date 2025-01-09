def filter_list(lst):
    result = []
    for item in lst:
        if type(item) == int:
            result.append(item)
    return result
