from compare_swap import compare_swap

def bubble_sort(arr):
    arr_len = len(arr)
    for i in range(arr_len):
        for j in range(arr_len - i - 1):
            arr[j], arr[j + 1] = compare_swap(arr[j], arr[j + 1])
    return arr

if __name__ == "__main__":
    arr = [13, 6, 3, 2, 6, 8, 9, 3, 1]
    print(bubble_sort(arr))