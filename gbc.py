n,m = map(int,input().split())
limit = [0]*101
cnt_meter=1
exceed=0
for i in range(n):
    meter,speed = map(int,input().split())
    
    for j in range(cnt_meter,cnt_meter +meter):
        limit[j]=speed
    cnt_meter+=meter
# 경계선 문제
cnt_meter =1
for k in range(m):
    meter2 ,speed2 =map(int,input().split())
    for x in range(cnt_meter,cnt_meter + meter2):
        exceed = max(exceed,speed2 - limit[x])
    cnt_meter +=meter2
print(exceed)