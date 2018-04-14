def binarySearch(arr, elem, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if start > end:
        return False

    mid = (start + end) // 2
    if elem == arr[mid]:
        return mid
    if elem < arr[mid]:
        return binarySearch(arr, elem, start, mid-1)
    # elem > arr[mid]
    return binarySearch(arr, elem, mid+1, end)

#j = int(input())

print('enter the array elements')
s = input()
arr = [int(y) for y in s.split()]

print('Enter the number to search')

x = int(input())

result = binarySearch(arr, x, start=0, end=None)

if result != -1:
    print('Element is present at index:', result)

else:
    print('Element not present in the array')
