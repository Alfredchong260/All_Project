arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

new_arr = []
for index in range(len(arr)):
    if arr[index] % 2 == 0:
        new_arr.append(arr[index])


new_arr1 = filter(lambda temp: temp % 2 == 0, arr)



print(list(new_arr1))
print(new_arr)
