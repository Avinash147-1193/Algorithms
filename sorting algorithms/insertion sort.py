def insertionSort(arr):
    length = len(arr)

    for i in range(1, length):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    for i in range(len(arr)):
        print("%d" % arr[i])

print('Enter the elements in array')
j = input()
A = [int(x) for x in j.split()]

insertionSort(A)
