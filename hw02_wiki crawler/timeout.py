import time
import threading


def threading_main():
    print("main thread: start")
    thrd = threading.Timer(5.0, threading_sub, args=["sub thread"])
    thrd.start()
    print("main thread: wait")
    thrd.join()     # add this line
    # thrd.join(timeout=2)  # just wait 2s then continue
    print("main thread: end")


def threading_sub(name):
    print(name + ": hello")


if __name__ == "__main__":
    start = time.time()
    threading_main()
    end = time.time()
    print("run time: {}".format(end - start))
