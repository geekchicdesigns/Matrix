# for i in range(0, 3):
#     for j in range(0, 3):
#         if i == 2:
#             print(i, j)

# a = [[1, 3, 9, 4], [5, 0, 9, -3]]
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j])

a_2d = [[1, 2, 3], [5, 6, 7]]
# a_2d[1][1] = 99
# print(a_2d)

# for row in a_2d:
#     for item in row:
#         print(item)

# for i in range(len(a_2d)):
#     for j in range(len(a_2d[i])):
#         print(a_2d[i][j])


def diagonal_sum(given_2d):
    total = 0
    for i in range(len(given_2d)):
        total += given_2d[i][i]
    return total

print("""
The diagonal sum of [[1,0],[0,1]] is: """)
print(diagonal_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

# def intersection_set(list1, list2):
#     # list3 = [value for value in list if value in list2]
#     # return list3
#     return list(set(list1) & set(list2))


# list1 = [1, 2, 3]
# list2 = [1, 3, 5]
# print(intersection_set(list1,list2))
