w,n =map(int,input().split())
mineral = []
rst=0
for i in range(n):
    min, permin = map(int,input().split())
    mineral.append([min,permin])
#print(mineral)
mineral.sort(key = lambda x: x[1],reverse= True)
for m in mineral:
    if w >= m[0]:
        w = w - m[0]
        rst += m[0]*m[1]
    elif w <m[0]:
        rst += w*m[1]
        w=0
    elif w==0:
        break
print(rst)