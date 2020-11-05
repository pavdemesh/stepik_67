# x = int(input('Enter the number of minutes to sleep: '))
# h = int(input('Hours to add: '))
# m = int(input('Minutes to add: '))
#
# add_h = (x % 60 + m) // 60
# print(add_h)
# print((x % 60 + m) % 60)

# def mint(*a):
#     print(a[0])
#     print("length is equal {}".format(len(a)))
#     for pos, item in enumerate(a):
#         print(pos, "|", item)
#
#
# mint(5, 2, 6, True, 'abaka', 'mukata')


# def my_range(start, stop, step=1):
#     res = list()
#     x = start
#
#     if step > 0:
#         while x < stop:
#             res = res + [x]
#             x = x + step
#
#     if step < 0:
#         while x > stop:
#             res = res + [x]
#             x = x + step
#
#     return res
#

# print(my_range(stop=15, start=1))
# print(my_range(1, 18, 3))

#
# def tess():
#     a = 10
#     b = 15
#     return a, b
#
#
# print("Number a is {} and b is {}".format(tess()[0], tess()[1]))
#
# x = tess()
# print(type(x))

# d = {'a': 10, 'b': 20, 'c': 30}
#
# x = d.items()[1]
#
# print(x)

# b = {"a": [10]}
# b["a"] += [2]
# print(b)


# def update_dictionary(d, key, value):
#     if key in d:
#         d[key] += [value]
#     elif (2 * key) in d:
#         d[2 * key] += [value]
#     else:
#         d[2 * key] = [value]
#
#
# d = {}
# print(update_dictionary(d, 1, -1))  # None
# print(d)                            # {2: [-1]}
# update_dictionary(d, 2, -2)
# print(d)                            # {2: [-1, -2]}
# update_dictionary(d, 1, -3)
# print(d)                            # {2: [-1, -2, -3]}


# source = input().lower().split()
#
# res = {}
#
# for item in source:
#     res[item] = res.get(item, 0) + 1
#
# for key, value in res.items():
#     print(key, value)
#
#
# def f(a):
#     return a + 5
#
#
# x = [int(input()) for i in range(int(input()))]
#
# b = {x: f(x) for x in set(x)}
#
# print(*[b[i] for i in x], sep=' | ')

# with open('test.txt', 'r') as fh:
#     for line in fh:
#         line = line.strip()
#         print(line)
#
# with open('test.txt', 'w') as out:
#     out.write('additional line')
#     out.write('\n')
#     out.write(str(25))

# Using subprocess module
# import subprocess
# print("call print.py", '--------------', sep='\n')
# subprocess.call('python print.py')
# print("and now back to test")

# import sys
#
# for arg in sys.argv[1:]:
#     print(arg, end=' ')

# import requests
# r = requests.get(r'https://stepic.org/media/attachments/course67/3.6.2/580.txt')
# print(r.content)


x, y = 0, 0
moves = {
    "север": 0,
    "юг": 0,
    "запад": 0,
    "восток": 0
}

num_moves = int(input())

for _i in range(num_moves):
    (direction, value) = input().split()
    moves[direction] += int(value)

end_x = x + moves["восток"] - moves["запад"]
end_y = y + moves["север"] - moves["юг"]

print(end_x, end_y, sep=" ")
