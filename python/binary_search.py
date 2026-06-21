def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1

    return -1

if __name__ == '__main__':
    arr = [1, 2, 3, 3, 6, 6, 8, 9, 13]
    target = 8
    print(binary_search(arr, target))