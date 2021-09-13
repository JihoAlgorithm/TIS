import sys
read = sys.stdin.readline

def dfs(r, c, count, sum):
    global ans
    if ans >= sum + MAX * (3 - count):
        return
    if count == 3:
        ans = max(ans, sum)
        return
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            try:
                if not visit[nr][nc]:
                    visit[nr][nc] = 1
                    if count == 1:
                        dfs(r, c, count + 1, sum + field[nr][nc])
                    dfs(nr, nc, count + 1, sum + field[nr][nc])
                    visit[nr][nc] = 0
            except: continue

N, M = map(int, read().split())
field = [list(map(int, read().split())) for _ in range(N)]
visit = [([0] * M) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
ans = 0
MAX = max(map(max, field))

for r in range(N):
    for c in range(M):
        visit[r][c] = 1
        dfs(r, c, 0, field[r][c])
        visit[r][c] = 0

print(ans)