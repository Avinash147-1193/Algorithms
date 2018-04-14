def binarySearch(arr, start, end, elem):

    if start > end:
        return False

    mid = (start + end) // 2
    if elem == arr[mid]:
        return mid
    if elem < arr[mid]:
        return binarySearch(arr, start, mid-1, elem)
    # elem > arr[mid]
    return binarySearch(arr, mid+1, end, elem)

def exponentialSearch(arr, n, x):
    if arr[0] == x:
        return 0
    i = 1
    while i < n and arr[i] <= x:
        i *= 2

    return binarySearch(arr, i // 2, min(i, n), x)

print('enter the array elements')
s = input()
arr = [int(y) for y in s.split()]

print('Enter the number to search')

x = int(input())

result = exponentialSearch(arr, len(arr)-1, x)

if result != -1:
    print('Element is present at index:', result)

else:
    print('Element not present in the array')