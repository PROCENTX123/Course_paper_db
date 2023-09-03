if __name__ == "__main__":
    arr = [ 12.227, 12.222, 12.300, 12.306, 12.281, 12.263, 12.354, 12.406, 12.236, 12.234]

    mean = sum(arr) / len(arr)

    variance = sum((x - mean) ** 2 for x in arr) / (len(arr) - 1)

    print(mean)
    print(variance)
