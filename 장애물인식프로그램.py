n= int(input())
graph = [list(map(str,input())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
cnt =0
blocks_cnt=0
blocks =[]
def dfs(x,y):
    visited[x][y]=1
    global blocks_cnt
    blocks_cnt +=1
    dy=[1,0,-1,0]
    dx = [0,1,0,-1]
    for i in range(4):
        nx =x+ dx[i]
        ny =y+ dy[i]
        if 0<= nx < n and 0<= ny < n and visited[nx][ny]==0 and graph[nx][ny]=='1':
            dfs(nx,ny)


for x in range(n):
    for y in range(n):

        if graph[x][y]=='1' and visited[x][y]==0:
            visited[x][y]=1
            cnt+=1
            dfs(x,y)
            blocks.append(blocks_cnt)
            blocks_cnt=0
print(cnt)
blocks.sort()
for b in blocks:
    print(b)