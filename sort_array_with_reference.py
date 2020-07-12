flag = 'run'
print("Enter the values, (press enter to stop input):")
s = []
f = []
while flag != 'over':
    try:
        temp = list(map(int, input().split(',')))
        if temp:
            s.append(temp[1:])
            f.append(temp[0])
        else:
            flag = 'over'
    except ValueError:
        flag = 'over'

#
# s = [10, 12, 20]
# f = [20, 19, 30]

map_f = {}
map_s = {}
for i in range(len(f)):
    map_f[i] = f[i]

for i in range(len(s)):
    map_s[i] = s[i]

# print(map_f)
sorted_f = []
new_s = []
for k, v in sorted(map_f.items(), key=lambda x: x[1]):
    sorted_f.append(v)
    new_s.append(map_s[k])

# print(sorted_f, '\n', new_s)
for i in range(len(sorted_f)):
    print(f'{sorted_f[i]},{new_s[i][0]},{new_s[i][1]}')
