import time

def memo(num,d):
    if num in d:
        return d[num]

    else:
        d[num] = memo(num-1,d) + memo(num-2,d)
        return d[num]


start = time.time()
d = {0:1,1:1}

print(memo(777,d))
print(time.time()-start)
