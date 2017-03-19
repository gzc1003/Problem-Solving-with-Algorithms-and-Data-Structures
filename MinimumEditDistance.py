origin = 'algor'
target = 'allig'
edit = []
str_matrix = [[0 for j in range(len(target)+1)]
                 for i in range(len(origin)+1)
             ]


def min_edit_distance(str_matrix):
    for i in range(len(origin)+1):

        str_matrix[i][0] = i*20

    for j in range(len(target)+1):
        str_matrix[0][j] = j*20

    for i in range(1,len(origin)+1):

        for j in range(1,len(target)+1):

            if origin[i-1] == target[j-1]:
                str_matrix[i][j] = min(str_matrix[i][j-1]+20,
                                       str_matrix[i-1][j]+20,
                                       str_matrix[i-1][j-1])
            elif origin[i-1] == ' ' or target[j-1] == ' ':
                str_matrix[i][j] = min(str_matrix[i][j-1]+20,
                                       str_matrix[i-1][j]+20,
                                       str_matrix[i-1][j-1]+20)
            else:
                str_matrix[i][j] = min(str_matrix[i][j-1]+20,
                                       str_matrix[i-1][j]+20,
                                       str_matrix[i-1][j-1]+40)

    a=i
    b=j
    while i>0 and j>0:
        if origin[i-1] == target[j-1]:
            edit.append('copy')
            i -= 1
            j -= 1
            continue

        elif str_matrix[i][j] == str_matrix[i-1][j-1]+40:
            edit.append('substitute')
            i -= 1
            j -= 1
            continue

        elif str_matrix[i][j] == str_matrix[i][j-1]+20:
            edit.append('insert')
            j -= 1
            continue
        elif str_matrix[i][j] == str_matrix[i-1][j]+20:
            edit.append('delete')
            i -= 1
            continue

    return str_matrix[a][b]

print(min_edit_distance(str_matrix))
for i in range(len(edit)):
    print(edit.pop())