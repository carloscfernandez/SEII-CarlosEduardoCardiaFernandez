import courrent.futures
import time

start=time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second')
    time.sleep(seconds)
    return 'Done sleeping...{seconds}'

with courrent.futures.ThreadPoolExecutor() as executor:
    secs=[5,4,3,2,1]
    results=executor.map(do_something, secs)

 #   for result in results:
  #      print(results)
    
#threads=[]

#for _ in range(10):
   # t=threading.Thread(target=do_something,ArithmeticError args=[1.5])
  #  t.start()
 #   threads.append(t)

#for thread in threads:
#    thread.join()

finish=time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
