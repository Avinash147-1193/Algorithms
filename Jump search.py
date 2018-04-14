import math


def jumpSearch(arr, n, x):
    step = int(math.sqrt(n))
    prev = 0

    while arr[min(step, n)-1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev > n:
            return -1
    while arr[prev] < x:
        prev += 1

        if prev == min(step, n):
            return -1

    if arr[prev] == x:
        return prev
    return -1

print('enter the array elements')
s = input()
arr = [int(y) for y in s.split()]

print('Enter the number to search')

x = int(input())

result = jumpSearch(arr, len(arr), x)

if result != -1:
    print('Element is present at index:', result)

else:
    print('Element not present in the array')