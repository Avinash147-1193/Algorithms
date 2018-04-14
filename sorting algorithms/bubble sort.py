def bubbleSort(arr):
    length = len(arr)

    for i in range(len(arr)):
        swapped = 0

        for j in range(0, length-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1] , arr[j]
                swapped = 1
        if swapped == 0:
            break

    for i in range(len(arr)):
        print("%d" % arr[i]),


print('Enter the elements in array')
j = input()
A = [int(x) for x in j.split()]

bubbleSort(A)

