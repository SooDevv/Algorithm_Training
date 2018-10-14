import re

if __name__ == '__main__':
    N = int(input())
    gmail = []

    for _ in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        pattern = re.compile("@gmail.com")

        if pattern.search(emailID):
            gmail.append(firstName)

    gmail.sort()
    print('\n'.join(gmail))