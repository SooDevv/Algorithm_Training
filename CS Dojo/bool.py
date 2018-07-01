def are_you_sad(is_rainy, has_umbrella):
    return is_rainy and not has_umbrella

print(are_you_sad(False, True))
print(are_you_sad(False, False))
print(are_you_sad(True, False))
print(are_you_sad(True, True))


def c_greater_than_d_plus_e(c, d, e):
    return c > d + e

print("c is greater thna d+e ?:", c_greater_than_d_plus_e(3, 1, 1))