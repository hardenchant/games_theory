import random


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def generate_random_game_matrix(m, n):
    return [[[random.randint(0, 100), random.randint(0, 100)] for _ in range(n)] for _ in range(m)]


def print_matrix(matr, nash_points=None, pareto_points=None):
    if not nash_points:
        nash_points = []
    if not pareto_points:
        pareto_points = []

    print(Color.CYAN + "Nash points:" + str(nash_points) + Color.END)
    print(Color.BLUE + "Pareto points:" + str(pareto_points) + Color.END)
    print(Color.YELLOW + "Nash and Pareto points:" + str([i for i in nash_points if i in pareto_points]) + Color.END)

    for row in matr:
        for fp, sp in row:
            if [fp, sp] in nash_points and [fp, sp] in pareto_points:
                print(Color.YELLOW + f'{str(fp).rjust(3)},{str(sp).rjust(3)}' + Color.END, end=' | ')
            elif [fp, sp] in nash_points:
                print(Color.CYAN + f'{str(fp).rjust(3)},{str(sp).rjust(3)}' + Color.END, end=' | ')
            elif [fp, sp] in pareto_points:
                print(Color.BLUE + f'{str(fp).rjust(3)},{str(sp).rjust(3)}' + Color.END, end=' | ')
            else:
                print(f'{str(fp).rjust(3)},{str(sp).rjust(3)}', end=' | ')
        print()


def get_nash_equilibrium_points(matr):
    fp_matr = [[cell[0] for cell in row] for row in matr]
    fp_matr_col_maxs = [max(col) for col in zip(*fp_matr)]

    sp_matr = [[cell[1] for cell in row] for row in matr]
    sp_matr_row_maxs = [max(row) for row in sp_matr]
    # for i, row in enumerate(matr):
    #     for j, (fp, sp) in enumerate(row):
    #         if fp == fp_matr_row_maxs[i] and sp == sp_matr_col_maxs[j]:
    #             [(fp, sp), (i, j)]

    return [
        [fp, sp] for i, row in enumerate(matr) for j, (fp, sp) in enumerate(row) if
        fp == fp_matr_col_maxs[j] and sp == sp_matr_row_maxs[i]
    ]


def get_pareto_optimal_points(matr):
    pareto_optimals = []
    for row in matr:
        for fp, sp in row:
            par_opt = True
            for row_ in matr:
                for fp_, sp_ in row_:
                    if (sp_ > sp and fp_ >= fp) or (fp_ > fp and sp_ >= sp):
                        par_opt = False
                        break
                if not par_opt:
                    break
            if par_opt:
                pareto_optimals.append([fp, sp])
    return pareto_optimals


print("random 10x10:")
a = generate_random_game_matrix(10, 10)
print_matrix(a, get_nash_equilibrium_points(a), get_pareto_optimal_points(a))
print("------------------------------------------------------------------------------------------")

crossroad = [
    [[1, 1], [0.6, 2]],
    [[2, 0.6], [0, 0]],
]
print("crossroad:")
print_matrix(crossroad, get_nash_equilibrium_points(crossroad), get_pareto_optimal_points(crossroad))
print("------------------------------------------------------------------------------------------")

family = [
    [[4, 1], [0, 0]],
    [[0, 0], [1, 4]],
]
print("family:")
print_matrix(family, get_nash_equilibrium_points(family), get_pareto_optimal_points(family))
print("------------------------------------------------------------------------------------------")

prison = [
    [[-5, -5], [0, -10]],
    [[-10, 0], [-1, -1]],
]
print("prison:")
print_matrix(prison, get_nash_equilibrium_points(prison), get_pareto_optimal_points(prison))
print("------------------------------------------------------------------------------------------")

prison = [
    [[0, 10], [9, 1]],
    [[7, 8], [6, 11]],
]
print("var15:")
print_matrix(prison, get_nash_equilibrium_points(prison), get_pareto_optimal_points(prison))
