def partition(arr, low, high):
    i = low - 1
    key = arr[high]

    for j in range(low, high):
        if arr[j] < key:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quicksortIterative(arr, l, h):
    size = h-l+1
    stack = [0]* size

    top = -1
    top += 1
    stack[top] = l
    top += 1
    stack[top] = h
    while top >= 0:
        h = stack[top]
        top -= 1
        l = stack[top]

        p = partition(arr, l, h)

        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1

            # If there are elements on right side of pivot,
            # then push right side to stack
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h


print('Enter the elements in the array')
j = input()
arr = [int(x) for x in j.split()]
n = len(arr)
quicksortIterative(arr, 0, n-1)

for i in range(n):
    print("%d" % arr[i])