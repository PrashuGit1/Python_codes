from functools import reduce


def grade(n):
    if n>=90:
        return 'A'
    elif 89>n>=80:
        return "B"
    elif 79>n>=70:
        return 'C'
    elif 69>n>-60:
        return 'D'
    elif 59>n>=40:
        return "E"



def mark_fun(marks):
    dic={}
    marks=list(filter(lambda x : x>40, marks))
    marks=list(map(grade, marks))
    grade_count = reduce(
    lambda acc, grade: {**acc, grade: acc.get(grade, 0) + 1},
    marks,
    {}
)

    print(grade_count)
    





marks = [95, 85, 73, 60, 45, 88, 33, 55, 99, 38]
mark_fun(marks)