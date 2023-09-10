if __name__ == "__main__":
    arr = [9.593, 9.670, 9.470, 9.381, 9.480, 9.433, 9.500, 9.485, 9.487, 9.507]

    mean = sum(arr) / len(arr)

    variance = sum((x - mean) ** 2 for x in arr) / (len(arr) - 1)

    print(mean)
    print(variance)
