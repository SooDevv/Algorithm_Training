import array
import resource

startMem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

mylist = []
for i in range(1,100000):
    mylist.append(i)

listMem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

myarray = array.array('i')
for i in range(1,100000):
    myarray.append(i)

arrayMem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

print("list를 만드는 데는 :", listMem-startMem)
print("array를 만드는 데는 : ", arrayMem-listMem)