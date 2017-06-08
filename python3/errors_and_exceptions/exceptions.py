cases = [input().split() for i in range(int(input()))]
for case in cases:
    try:
        print(int(case[0]) // int(case[1]))
    except (ZeroDivisionError, ValueError) as e:
        print('Error Code:',e)
