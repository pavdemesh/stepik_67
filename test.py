x = int(input('Enter the number of minutes to sleep: '))
h = int(input('Hours to add: '))
m = int(input('Minutes to add: '))

add_h = (x % 60 + m) // 60
print(add_h)
print((x % 60 + m) % 60)
