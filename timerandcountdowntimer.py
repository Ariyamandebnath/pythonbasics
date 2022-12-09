import time
a=input("select form the two:\ncountdown Timer, Timer\n")
if a=='countdown Timer':
    t=int(input("set countdown time in secounds"))
    def countdown(t):
        while t:
            min, sec = divmod(t, 60)
            timer = "{:02d}:{:02d}".format(min, sec)
            print(timer)
            time.sleep(1)
            t -= 1
        print("the times is up!!")
    countdown(t)


if a=='Timer':
    def timer():
        t = 0
        while True:
            t += 1
            min, sec = divmod(t, 60)
            hr, min = divmod(min, 60)
            timer = "{:02d}:{: 02d}:{:02d}".format(hr, min, sec)
            print(timer)
            time.sleep(1)
    timer()


