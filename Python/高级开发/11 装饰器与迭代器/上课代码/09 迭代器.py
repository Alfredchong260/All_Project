# for in 可迭代对象
# 有序,无序的内容都可以进行迭代
arr = [1, 2, 3, 4, 5]
for item in arr:  # 集合是无序的
    print(item)

print('-----------------------')
index = 0
while index < len(arr):
    print(arr[index])
    index += 1
