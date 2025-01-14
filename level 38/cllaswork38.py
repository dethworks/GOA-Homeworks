                                    # 1
def manual_diffrence(set1, set2):
    result = set()
    for item in set1:
        if item not in set2:
            result.add(item)
    return result


                                     # 2

student1 = {
    "name": "ლუკა",
    "surname": "კვარაცხელია",
    "age": 16,
    "average_grade": 8.5
}

student2 = {
    "name": "ნიკა",
    "surname": "ნიკაძე",
    "age": 17,
    "average_grade": 9.5
}


print(student1)
print(student2)










