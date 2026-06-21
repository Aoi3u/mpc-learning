def compare_swap(a, b):
    if a > b:
        return b, a
    return a, b

if __name__ == "__main__":
    print(compare_swap(2, 1))
    print(compare_swap(5, 5))