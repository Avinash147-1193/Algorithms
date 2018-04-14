def partition(arr, low, high):
    i = low -1
    key = arr[high]

    for j in range(low, high):
        if arr[j] < key:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

print('Enter the elements in array')
j = input()
arr = [int(x) for x in j.split()]
size = len(arr)
quickSort(arr, 0, size-1)

for i in range(0, size):
    print("%d" % arr[i])
