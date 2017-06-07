num_of_students, num_of_subjects = map(int, input().split())
subject_scores = [list(map(float, input().split())) for i in range(num_of_subjects)]
student_scores = list(zip(*subject_scores))
averages = [sum(marks) / len(subject_scores) for marks in student_scores]
print(*averages,sep='\n')
