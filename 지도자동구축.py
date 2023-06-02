# 1 -> 2칸씩 나눠짐
# 3번째는 가로 8 세로 8칸 
n = int(input())
width = 2**n
width+=1
print(width* width)