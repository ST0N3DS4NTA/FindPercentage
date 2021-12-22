if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

average = 0
for key, value in student_marks.items():
    if key == query_name:
        average = ((value[0] + value[1] + value[2])/3)
        form = "{:.2f}".format(average)
        print(form)




