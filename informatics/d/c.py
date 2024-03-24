N=int(input())
array = list(map(int, input().split()))
cnt=0
for i in array:
    if(i>0):
        cnt+=1


print(cnt)