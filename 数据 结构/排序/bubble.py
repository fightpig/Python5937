
def bubble_1(to_sort_arr):
    """
    张三出人头地PK大法
        张三先出战PK，且PK至最后并获胜
        因为张三一直PK胜，则一直是张三
        若有谁PK胜，则他代替张三，成为新的张三
    :param to_sort_arr:
    :return:
    """
    length = len(to_sort_arr)
    change = False
    change_count = 0
    for i in range(length - 1):
        for j in range(i + 1, length):
            if to_sort_arr[i] < to_sort_arr[j]:
                to_sort_arr[i], to_sort_arr[j] = to_sort_arr[j], to_sort_arr[i]
                change = True
                change_count += 1
        if change is False:
            break
    print(f'total change: {change_count} times')


def test_bubble_1():
    arr = list(range(10))[::-1]
    print(arr)
    bubble_1(arr)
    print(arr)
    #
    arr = list(range(10))
    print(arr)
    bubble_1(arr)
    print(arr)

    arr = [99, 1, 100, 10, 8, 50, -1, 101, 0.9, -50]
    print(arr)
    bubble_1(arr)
    print(arr)


if __name__ == '__main__':
    test_bubble_1()