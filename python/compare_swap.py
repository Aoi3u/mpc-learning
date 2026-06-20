def compare_swap(a, b):
    if a > b:
        return b, a
    return a, b

print(compare_swap(2, 1))
print(compare_swap(5, 5))