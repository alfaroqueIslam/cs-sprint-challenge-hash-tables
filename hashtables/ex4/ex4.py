
def has_negatives(a):
    cache = {}
    result = []
    for i in range(len(a)):
        if a[i] != 0:
            if a[i] not in cache:
                cache[a[i]] = i
            if -a[i] in cache:
                result.append(abs(a[cache[a[i]]]))


    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
