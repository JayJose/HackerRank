def get_next_multiple(n, m=5):
    return (n // m + 1) * m

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    for i, g in enumerate(grades):
        if g >= 38 and get_next_multiple(g) - g < 3:
            grades[i] = get_next_multiple(g)
    return grades

grades = [38, 69, 75]

x = gradingStudents(grades)

print(x)
