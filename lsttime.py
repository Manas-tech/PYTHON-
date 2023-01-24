lst =range(10000000)
lst1 =range(10000000)
import time
start=time.time()
result=[(x+y) for x,y in zip(lst,lst1)]
print((time.time()-start)*1000) 
 
 
 