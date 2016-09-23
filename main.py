# coding:utf-8
import time
import threading
from req_work import p_info
from time import sleep


# config
THREAD_NUM = 100        
ONE_WORKER_NUM = 10000      
LOOP_SLEEP = 0.5        


ERROR_NUM = 0


def doWork(index):
    p_info()

def working():
    t = threading.currentThread()
    print "["+t.name+"] Sub Thread Begin"

    i = 0
    while i < ONE_WORKER_NUM:
        i += 1
        doWork(i)
        sleep(LOOP_SLEEP)

    print "["+t.name+"] Sub Thread End"


def main():
    #doWork(0)
    #return

    t1 = time.time()

    Threads = []

    # create thread
    for i in range(THREAD_NUM):
        t = threading.Thread(target=working, name="T"+str(i))
        t.setDaemon(True)
        Threads.append(t)

    for t in Threads:
        t.start()

    for t in Threads:
        t.join()

    print "main thread end"

    t2 = time.time()
    print "========================================"
    print "URL:", PERF_TEST_URL
    print "task count:", THREAD_NUM, "*", ONE_WORKER_NUM, "=", THREAD_NUM*ONE_WORKER_NUM
    print "total second:", t2-t1
    print "second per request:", (t2-t1) / (THREAD_NUM*ONE_WORKER_NUM)
    print "request per second:", 1 / ((t2-t1) / (THREAD_NUM*ONE_WORKER_NUM))
    print "error count:", ERROR_NUM


if __name__ == "__main__": 
    main()
