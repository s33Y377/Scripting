import threading


def f(a):
    print('Thread function')
    print(a+1)
    return


t = threading.Thread(target=f, args=(5,))
t.start()
t.join()
