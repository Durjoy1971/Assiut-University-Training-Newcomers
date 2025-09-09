h, w = map(int, input().split())
s = [input().strip() for _ in range(h)]

flag = True

for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            cnt = 0
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < h and 0 <= nj < w and s[ni][nj] == "#":
                    cnt += 1
            if cnt not in [2, 4]:
                flag = False

print("Yes" if flag else "No")