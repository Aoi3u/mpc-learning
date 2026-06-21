def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

if __name__ == '__main__':
    arr = [21, 5, 92, 5, 0]
    target = 5
    print(linear_search(arr, target))