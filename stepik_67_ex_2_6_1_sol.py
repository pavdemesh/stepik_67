num = [int(input())]

while sum(num) != 0:
    num.append(int(input()))

print(sum(i ** 2 for i in num))
