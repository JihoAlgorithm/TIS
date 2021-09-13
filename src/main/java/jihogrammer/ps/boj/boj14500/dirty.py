from sys import stdin

read = stdin.readline

N, M = map(int, read().split())

field = [[*map(int, read().split())] for _ in range(N)]
visited = [[0 for _ in range(M)] for __ in range(N)]

NEWS = [
    [(0, -1), (-1, 0), (1, 0)],
    [(0, -1), (1, 0), (0, 1)],
    [(1, 0), (0, 1), (-1, 0)],
    [(0, -1), (0, 1), (-1, 0)],
]

delta = [(0, -1), (1, 0), (0, 1), (-1, 0)]

answer = 0

def dfs(r, c, count, sum):
    global answer
    if count == 3:
        answer = max(answer, sum)
        return
    for d in delta:
        try:
            nr = r + d[0]
            nc = c + d[1]
            if not visited[nr][nc]:
                visited[nr][nc] = 1
                dfs(nr, nc, count + 1, sum + field[nr][nc])
                visited[nr][nc] = 0
        except: continue
    for direction in NEWS:
        sum = field[r][c]
        try:
            for d in direction:
                sum += field[r + d[0]][c + d[1]]
            answer = max(answer, sum)
        except: continue

for r in range(N):
    for c in range(M):
        visited[r][c] = 1
        dfs(r, c, 0, field[r][c])
        visited[r][c] = 0

print(answer)