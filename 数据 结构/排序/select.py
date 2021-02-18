

def select_1(to_sort_arr):
    length = len(to_sort_arr)
    change = False
    change_index_count = 0
    change_value_count = 0
    for i in range(0, length - 1):
        max_value_index = i
        for j in range(i + 1, length):
            if to_sort_arr[i] < to_sort_arr[j]:
                i, j = j, i
                change = True
                change_index_count += 1

        if max_value_index != i:
            to_sort_arr[i], to_sort_arr[max_value_index] = to_sort_arr[max_value_index], to_sort_arr[i]
            change_value_count += 1

        if change is False:
            break
    print(f'total change index: {change_index_count} times, total change value: {change_value_count} times')


def test_select_1():
    arr = list(range(10))[::-1]
    print(arr)
    select_1(arr)
    print(arr)
    #
    arr = list(range(10))
    print(arr)
    select_1(arr)
    print(arr)

    arr = [99, 1, 100, 10, 8, 50, -1, 101, 0.9, -50]
    print(arr)
    select_1(arr)
    print(arr)


if __name__ == '__main__':
    test_select_1()