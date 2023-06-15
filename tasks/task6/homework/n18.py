from turtle import *
import matplotlib.pyplot as plt


SCALE = 5

tracer(0)
screensize(2000, 2000)


def draw_grid():
    up()
    for x in range(-20, 20):
        for y in range(-20, 20):
            goto(x * SCALE, y * SCALE)
            dot(4, 'red')


def draw_axis():
    up()
    goto(-20 * SCALE, 0 * SCALE)
    down()
    goto(20 * SCALE, 0 * SCALE)
    
    up()
    goto(0 * SCALE, -20 * SCALE)
    down()
    goto(0 * SCALE, 20 * SCALE)


def move(x, y):
    goto(xcor() + x * SCALE, ycor() + y * SCALE)


def main():
    cnt = 0
    for x in range(120):
        for y in range(16):
            cond1 = y < x * 3
            cond2 = y < 15
            cond3 = y > x // 4 - 14         
            cond4 = y > 0
            if cond1 and cond2 and cond3 and cond4:
                cnt += 1
    print(cnt)
    cond1 = [x * 3 for x in range(120)]
    cond2 = [15 for x in range(120)]
    cond3 = [x / 4 - 14 for x in range(120)]
    cond4 = [0 for x in range(120)]
    plt.plot(range(120), cond1)
    plt.plot(range(120), cond2)
    plt.plot(range(120), cond3)
    plt.plot(range(120), cond4)
    plt.show()

    
main()
