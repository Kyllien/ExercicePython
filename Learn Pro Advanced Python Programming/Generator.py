import time
import memory_profiler

mem0 = memory_profiler.memory_usage()
print("Memory : {}".format(mem0))

def naturalNoList(n):
    res = []
    for i in range(1,n):
        res.append(i)
    return res

def naturalNoGen(n):
    for i in range(1,n):
        yield(i+5)

print(memory_profiler.profile())
t1 = time.time()
listN = naturalNoList(10)
t2 = time.time()
mem1 = memory_profiler.memory_usage()
listG = naturalNoGen(10)
mem2 = memory_profiler.memory_usage()
t3 = time.time()

print("Memory after 1 : {0}, after 2 {1}".format(mem1[0]-mem0[0],mem2[0]-mem1[0]))
print("Temps 1 : {0}, temps 2 : {1}".format(t1 - t2, t2-t3))

print(listN)
for i in listG:
    print(i)
