company = ["google", "naver", "samsung"]

print("original: ", company)
company[0], company[2] = company[2], company[0]
print("swap 0, 2:", company)

temp = company[0]
company[0] = company[2]
company[2] = temp
print("reswap 0,2 :", company)