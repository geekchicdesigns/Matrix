# for i in range(0, 3):
#     for j in range(0, 3):
#         if i == 2:
#             print(i, j)

# a = [[1, 3, 9, 4], [5, 0, 9, -3]]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j])


def intersection_set(list1, list2):
    # list3 = [value for value in list if value in list2]
    # return list3
    return list(set(list1) & set(list2))


list1 = [1, 2, 3]
list2 = [1, 3, 5]
print(intersection_set(list1,list2))
