# Solution 1
# num = int(input())
# arr = []
#
# for i in range(1, num + 1):
#     arr += [i] * i
#
# print(*arr[:num])

# Solution 2
user_input = int(input())
counter = 0

for num in range(1, user_input + 1):
    for i in range(num):
        if counter < user_input:
            print(num, end=' ')
            counter += 1
        else:
            break
