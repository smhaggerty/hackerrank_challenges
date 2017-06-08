if __name__ == '__main__':
    results = []
    scores = set()

    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.add(score)
        results.append([name, score])

    penultimate_score = sorted(scores)[1]
    students = [stdnt[0] for stdnt in results if stdnt[1] == penultimate_score]
    print(*sorted(students), sep='\n')
