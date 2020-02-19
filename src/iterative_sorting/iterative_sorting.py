# TO-DO: Complete the selection_sort() function below
import random

arr4 = random.sample(range(100), 20)

print(arr4)


def selection_sort(arr):

    if len(arr) == 0:
        return []

    # loop through n-1 elements
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = arr[i]

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[i] and arr[j] <= smallest_index:
                smallest_index = arr[j]

                # TO-DO: swap
                arr[j] = arr[i]
                arr[i] = smallest_index

    return arr


print(selection_sort(arr4))


# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):

    if len(arr) == 0:
        return []

    while True:
        count = 0
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i + 1]
                arr[i + 1] = arr[i]
                arr[i] = temp
                count = 1

        if count == 0:
            break

    return arr


print(bubble_sort(arr4))


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
