# -*- coding:UTF-8 -*-
import turtle


def draw(length):
    if length > 5:
        if length < 25:
            turtle.pendown()
            turtle.color("green")
            turtle.forward(length)
            turtle.right(20)
            draw(length - 15)

            turtle.left(40)
            draw(length - 15)

            turtle.penup()
            turtle.right(20)
            turtle.backward(length)
        else:
            turtle.pendown()
            turtle.color("brown")
            turtle.forward(length)
            turtle.right(20)
            draw(length - 15)

            turtle.left(40)
            draw(length - 15)

            turtle.right(20)
            turtle.backward(length)


def main():
    """
        主函数
    """
    turtle.left(90)
    turtle.penup()
    turtle.backward(50)
    turtle.pendown()
    draw(80)
    turtle.exitonclick()


if __name__ == '__main__':
    main()
