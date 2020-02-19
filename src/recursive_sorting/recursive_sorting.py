# TO-DO: complete the helper function below to merge 2 sorted arrays
import random

arr5 = [13, 6, 15, 44, 20, 36, 5, 73, 55, 49, 2, 25]
arr5 = random.sample(range(100), 8)


def merge(arrA, arrB):
    arr = arrA + arrB

    if len(arrA) == len(arrB) and len(arrA) > 1:

        for i in range(len(arr) - 1):
            if i % 2 == 0 and arr[i][0] > arr[i + 1][0]:
                arr[i][0], arr[i + 1][0] = arr[i + 1][0], arr[i][0]

        arr = [[arr[i][0], arr[i + 1][0]]
               for i in range(len(arr) - 1) if i % 2 == 0]

        print(arr)
        new_array = []
        while len(arr[0]) > 0 and len(arr[1]) > 0:
            if min(arr[0]) < min(arr[1]):
                new_array.append(min(arr[0]))
                arr[0].remove(min(arr[0]))
            else:
                new_array.append(min(arr[1]))
                arr[1].remove(min(arr[1]))

        if len(arr[0]) > 0:
            while len(arr[0]) > 0:
                new_array.append(min(arr[0]))
                arr[0].remove(min(arr[0]))
        else:
            while len(arr[1]) > 0:
                new_array.append(min(arr[1]))
                arr[1].remove(min(arr[1]))

        arr = [new_array]
    return arr


print(arr5)


def merge_sort(arr):
    # TO-DO
    if len(arr) == 1:
        return [arr]

    t = merge_sort(arr[0:len(arr)//2]) + merge_sort(arr[len(arr)//2:])

    if len(t[0]) == 1:
        if merge(t[0:len(t)//2], t[len(t)//2:]) != []:
            return merge(t[0:len(t)//2], t[len(t)//2:])

    final = []
    while len(t[0]) > 0 and len(t[1]) > 0:
        if min(t[0]) < min(t[1]):
            final.append(min(t[0]))
            t[0].remove(min(t[0]))
        else:
            final.append(min(t[1]))
            t[1].remove(min(t[1]))

    if len(t[0]) > 0:
        while len(t[0]) > 0:
            final.append(min(t[0]))
            t[0].remove(min(t[0]))
    else:
        while len(t[1]) > 0:
            final.append(min(t[1]))
            t[1].remove(min(t[1]))

    return final


print(merge_sort(arr5))


# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr


# def recurse_factorial(n):
#     if n == 0:
#         return 1
#     return n * recurse_factorial(n - 1)


# print(recurse_factorial(4))

# while True:
#         count = 0
#         for i in range(len(arr) - 1):
#             if arr[i][0] > arr[i + 1][0]:
#                 arr[i][0], arr[i + 1][0] = arr[i + 1][0], arr[i][0]
#                 count = 1
#         if count == 0:
#             break

#     return [arr[i][0] for i in range(len(arr))]


my_list = [5, 9, 3, 7, 2, 8, 1, 6]


def partition(data):
    left = []
    pivot = data[0]
    right = []

    for item in data[1:]:
        if item < pivot:
            left.append(item)

        else:  # Handling > or =
            right.append(item)
    return left, pivot, right


def quicksort(data):
    if data == []:
        return data

    left, pivot, right = partition(data)
    return quicksort(left) + [pivot] + quicksort(right)


# print(quicksort(my_list))


# if len(arrA) == 2:
# if arrA[0][0] > arrA[1][0]:
#     arrA[0][0], arrA[1][0] = arrA[1][0], arrA[0][0]
#     arrA = [[arrA[0][0], arrA[1][0]]]
#     if len(arrB) == 2:
#         if arrB[0][0] > arrB[1][0]:
#             arrB[0][0], arrB[1][0] = arrB[1][0], arrB[0][0]
#             arrB = [[arrB[0][0], arrB[1][0]]]


# ta = [[arrA[i][0], arrA[i + 1][0]]
#           for i in range(len(arrA) - 1) if i % 2 == 0]
#     tb = [[arrB[i][0], arrB[i + 1][0]]
#           for i in range(len(arrB) - 1) if i % 2 == 0]

#     print(ta, tb)


# if arr[0][0] < arr[1][0]:
#             new_array = [arr[0][0], arr[1][0]]
#         else:
#             new_array = [arr[1][0], arr[0][0]]

#         if arr[0][1] < arr[1][1]:
#             if arr[0][1] < new_array[1]:
#                 new_array = [new_array[0], arr[0][1], new_array[1], arr[1][1]]
#             else:
#                 new_array = new_array + [arr[0][1]] + [arr[1][1]]
#         else:
#             if arr[1][1] < new_array[1]:
#                 new_array = [new_array[0], arr[1][1], new_array[1], arr[0][1]]
#             else:
#                 new_array = new_array + [arr[1][1]] + [arr[0][1]]
