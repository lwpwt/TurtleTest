import turtle as t

"""
    用递归画分型树
"""

def draw_branch(branch_length):
    """
        绘制分型树
    :param branch_length:  初始长度
    :return:
    """
    if branch_length >=5:

        # 绘制右边树枝
        if branch_length > 15:
            t.color("green")
        else:
            t.color("red")
        t.forward(branch_length)
        t.pensize(1)
        t.right(20)
        draw_branch(branch_length-8)
        # 绘制左边树枝
        t.left(40)
        draw_branch(branch_length - 8)
        if branch_length > 15:
            t.color("green")
        else:
            t.color("red")
        #回到原点
        t.right(20)
        t.backward(branch_length)

def main():

    t.left(90)
    t.penup()
    t.backward(300)
    t.pendown()
    draw_branch(100)
    t.exitonclick()


if __name__ == "__main__":
    main()