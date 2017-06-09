_ = input()
s = set(map(int, input().split()))
commands = {'discard': lambda x, y: x.discard(y),
            'remove': lambda x, y: x.remove(y)
           }

for i in range(int(input())):
    command = input().split()
    if command[0][0] == 'p':
        s.pop()
    else:
        commands[command[0]](s, int(command[1]))

print(sum(s))
