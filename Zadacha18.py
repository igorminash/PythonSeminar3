N = int(input())
list = []

for i in range(0,N):
    list.append(i+1)
print (list)

X = int(input())

max_num = list[0]

for j in list:
    if abs(j - X) < abs(max_num - X):
        max_num = j

print(max_num)
    
