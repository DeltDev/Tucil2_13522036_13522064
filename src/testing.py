def func(i,arr):
    if(i >0):
        arr.append(i)
        i = i-1
        func(i,arr)

arr = []

func(69,arr)

print(arr)