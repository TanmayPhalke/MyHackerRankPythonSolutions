#The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name #provided, showing 2 places after the decimal.

n = int(input())
student_marks = {}

for line in range(n):
    line = input().split()
    name, scores = line[0], line[1:]
    scores = map(float, scores)
    student_marks[name] = scores
query_name = input()

list_marks = list()
for item in student_marks[query_name]:
    list_marks.append(item)

average = float(sum(list_marks)/3)
formatted_float = "{:.2f}".format(average)
print(formatted_float)
