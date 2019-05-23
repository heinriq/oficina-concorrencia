import time
import random
import threading

def a_task():
    print("doing a1")
    global a1_done
    a1_done = True
    b1_action.release()
    a1_action.acquire()
    assert a1_done and b1_done
    print("doing a2")

def b_task():
    print("doing b1")
    global b1_done
    b1_done = True
    a1_action.release()
    b1_action.acquire()
    assert a1_done and b1_done
    print("doing b2")

a1_done = False
b1_done = False
a1_action = threading.Semaphore(0)
b1_action = threading.Semaphore(0)

def main():
    a = threading.Thread(target=a_task)
    a.start()
    b = threading.Thread(target=b_task)
    b.start()
    a.join()
    b.join()

main()