n= list(map(str,input().split()))
s=''
for i in n:
    s+=i
if s =='12345678':
    print('ascending')
elif s =='87654321':
    print('descending')
else:
    print('mixed')