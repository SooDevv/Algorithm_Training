# input 07:05:45PM/AM
# output 19:05:45
# return time[:-2] if time[-2:] == "AM" else str(int(time[:2]) + 12) + time[2:8]

def timeConversion(time):
    return time[:-2] if time[-2:] =='AM' else str(int(time[:2]) + 12) + time[2:8]

if __name__ == '__main__':
    time = input()

    result = timeConversion(time)
    print(result)