from datetime import datetime
number_of_test_cases = int(input())

for i in range(number_of_test_cases):
    date_format = '%a %d %b %Y %H:%M:%S %z'
    t1, t2 = [datetime.strptime(input(), date_format) for i in range(2)]
    time_delta = int(abs((t1 - t2).total_seconds()))
    print(time_delta)
