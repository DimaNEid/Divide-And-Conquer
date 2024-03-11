def calculate_least_sugar(mat, day, prev_item):
    if day == 0:
        return mat[prev_item][0]
    else:
        if prev_item == 0:
            return mat[0][day] + min(calculate_least_sugar(mat, day - 1, 1), calculate_least_sugar(mat, day - 1, 2))
        elif prev_item == 1:
            return mat[1][day] + min(calculate_least_sugar(mat, day - 1, 0), calculate_least_sugar(mat, day - 1, 2))
        elif prev_item == 2:
            return mat[2][day] + min(calculate_least_sugar(mat, day - 1, 0), calculate_least_sugar(mat, day - 1, 1))


def calculate_least_sugar_dp(mat):
    dp_mat = []
    for i in range(len(mat)):
        row = []
        for j in range(len(mat[0])):
            row.append(0)
        dp_mat.append(row)
    dp_mat[0][0] = mat[0][0]
    dp_mat[1][0] = mat[1][0]
    dp_mat[2][0] = mat[2][0]
    for i in range(1, days):
        dp_mat[0][i] = mat[0][i] + min(dp_mat[1][i - 1], dp_mat[2][i - 1])
        dp_mat[1][i] = mat[1][i] + min(dp_mat[0][i - 1], dp_mat[2][i - 1])
        dp_mat[2][i] = mat[2][i] + min(dp_mat[1][i - 1], dp_mat[0][i - 1])
    return min(dp_mat[0][-1], dp_mat[1][-1], dp_mat[2][-1])

def define_steps(dp_mat, days, least_value):
    choices = (days +1) * [0]  # To store the choices made at each step
    dict = {
        dp_mat[0][-1]: 0,
        dp_mat[1][-1]: 1,
        dp_mat[2][-1]: 2
    }
    choices[-1] = dict.get(least_value)
    prev_item = choices[-1]
    for i in range(days-1, 0, -1):
        dict = {
            dp_mat[0][i]: 0,
            dp_mat[1][i]: 1,
            dp_mat[2][i]: 2
        }
        if prev_item == 0:
            choices[i] = 1 if dp_mat[1][i] < dp_mat[2][i] else 2
            prev_item = choices[i]
        elif prev_item == 1:
            choices[i] = 0 if dp_mat[0][i] < dp_mat[2][i] else 2
            prev_item = choices[i]
        elif prev_item == 2:
            choices[i] = 0 if dp_mat[0][i] < dp_mat[1][i] else 1
            prev_item = choices[i]

    return ' ,'.join([str(choice) for choice in choices])

if __name__ == "__main__":
    mat = []
    days = int(input())
    for i in range(3):
        row = number_list = list(map(int, input().split()))
        mat.append(row)
    # print(min(calculate_least_sugar(mat, days-1, 0), calculate_least_sugar(mat, days-1, 1), calculate_least_sugar(mat, days-1, 2)))
    print(calculate_least_sugar_dp(mat))
