def solve(m, tip_percent, tax_percent):
    tip = m * (tip_percent/100.0)
    tax = m * (tax_percent/100.0)

    total = round(m + tip + tax)
    print(total)


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)