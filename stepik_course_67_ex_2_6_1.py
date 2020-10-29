arr = []

while True:
    num = int(input())
    arr.append(num)
    if sum(arr) == 0:
        multi = 0
        for dig in arr:
            multi += dig * dig
        break
print(multi)
