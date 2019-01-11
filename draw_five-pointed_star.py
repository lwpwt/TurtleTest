import turtle as t
"""
    递归绘制五角星
"""

def draw_five_star(size):
    count = 1
    while count <= 5:
        t.forward(size)
        t.right(144)
        count += 1
    size +=100
    if size <= 1000:
        draw_five_star(size)
# 主函数
def main():
    t.penup()
    t.backward(300)
    t.pendown()
    draw_five_star(100)
    t.exitonclick()

if __name__ == "__main__":
    main()