from turtle import *
import turtle
color('green')

left_drawer = Turtle()
right_drawer = Turtle()
left_drawer.left(90)
left_drawer.forward(50)
right_drawer.left(90)
right_drawer.forward(50)
# left_last_x, left_last_y = tuple(left_drawer.position())
# right_last_x, right_last_y = tuple(right_drawer.position())

max_branchs = 3
count = 0


def draw_branch():
    left_drawer = Turtle()
    right_drawer = Turtle()
    global count
    if count != 0:
        left_drawer.setposition(left_last_x, left_last_y)
        right_drawer.setposition(right_last_x, right_last_y)

    left_drawer.left(30)
    right_drawer.right(30)
    left_drawer.forward(50)
    right_drawer.forward(50)

    left_last_x, left_last_y = tuple(left_drawer.position())
    right_last_x, right_last_y = tuple(right_drawer.position())

    # backward(50)
    # right(60)
    # forward(50)
    # penup()
    # setposition(last_conjunction_x, last_conjunction_y)
    count += 1
    if count < max_branchs:
        # pendown()
        draw_branch()


# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
draw_branch()
done()
