import sys
read = sys.stdin.readline

N = int(read())
stack = []
answer = []
command = {
    'push': stack.append,
    'pop': lambda s: s.pop() if s else '-1',
    'size': lambda s: str(len(s)),
    'empty': lambda s: '0' if s else '1',
    'top': lambda s: s[-1] if s else '-1'
}

for _ in range(N):
    o, *v = read().split()
    if o == 'push': command[o](v[0])
    else: answer.append(command[o](stack))

print('\n'.join(answer))