
# list = [1, 2, 3, 2, 5]


N = int(input())
list = []

for i in range(0,N):
    list.append(i+1)
print (list)

X = int(input())
count = 0

for j in range(1, len(list)):
    if X == list[j]:
        count += 1
    else:
        list[j] += 1
print(count)

