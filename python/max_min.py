def max2(a, b):
    if a < b:
        return b
    return a

def min2(a, b):
    if a < b:
        return a
    return b

if __name__ == "__main__":
    print(max2(1, 2))  # 2
    print(min2(1, 2))  # 1
    print(max2(5, 5))  # 5
    print(min2(5, 5))  # 5