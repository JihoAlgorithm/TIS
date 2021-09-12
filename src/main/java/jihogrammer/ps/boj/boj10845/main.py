from sys import stdin

read = stdin.readline

N = int(read())
queue = []
answer = []
command = {
    "push": queue.append,
    "pop": lambda q: q.pop(0) if q else '-1',
    "size": lambda q: str(len(q)),
    "empty": lambda q: '0' if q else '1',
    "front": lambda q: q[0] if q else '-1',
    "back": lambda q: q[-1] if q else '-1'
}

for _ in range(N):
    o, *v = read().split()
    if o == "push": command[o](v[0])
    else: answer.append(command[o](queue))

print('\n'.join(answer))
