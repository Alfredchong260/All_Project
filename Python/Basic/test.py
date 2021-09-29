a = [4,6,8,3,6,2,5]
a.sort(reverse=True)
print(a)

b = {}

for i in a:
    if i not in b.keys():
        b[i] = 1
    else:
        b[i] += 1

print(b)
