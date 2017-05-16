from collections import namedtuple
n = int(input())
columnNames = input().split()
Student = namedtuple('Student', '{}, {}, {}, {}'.format(*columnNames))
students = [Student(*input().split()) for i in range(n)]
examAverage = sum(map(lambda x: float(x.MARKS), students)) / len(students)
print('{:.2f}'.format(examAverage))
