class Student:
    def __init__(self, firstName, lastName, id, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.id = id
        self.scores = scores

    def calculate(self):
        mean = sum(scores) / len(scores)
        if 90 <= mean <=100:
            return 'O'
        elif 80 <= mean < 90:
            return 'E'
        elif 70 <= mean < 80:
            return 'A'
        elif 55 <= mean < 70:
            return 'P'
        elif 40 <= mean < 55:
            return 'D'
        else:
            return 'T'


    def printPerson(self):
        print('Name: {}, {} \nID: {} \nGrade: {}'.format(
            self.lastName, self.firstName, self.id, self.calculate()
        ))


if __name__ == '__main__':
    line = input().rstrip().split()
    firstName = line[0]
    lastName = line[1]
    id = line[2]

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    student = Student(firstName, lastName, id, scores)

    student.printPerson()