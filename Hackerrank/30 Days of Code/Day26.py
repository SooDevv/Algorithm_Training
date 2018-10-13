if __name__ == '__main__':
    r_d, r_m, r_y = map(int, input().rstrip().split())
    e_d, e_m, e_y = map(int, input().rstrip().split())

    fine = 0
    if (r_y, r_m, r_d) <= (e_y, e_m, e_d):
        fine = 0
    elif (r_y, r_m) == (e_y, e_m):
        fine = 15 * (r_d - e_d)
    elif r_y == e_y:
        fine = 500 * (r_m - e_m)
    else:
        fine = 10000

    print(fine)

