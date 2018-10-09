from graphics import *
'''
Python作业3
By:刘茂-SA18225243
Date:2018-10-09
'''
def image_demo():
    '''
    1、通过Image( )加载图片、展示（通过clone方法获取副本）
    2、获取图片大小
    3、从左上角开始，按行每个像素进行颜色转换，并且update
    4、保存转换后的图片
    '''
    btn_ok = Text(Point(200,20),"点击转换图片颜色")
    btn_ok.setTextColor('red')
    btn_ok.setSize(size=30)
    btn_ok.setStyle(style='bold')
    im = Image(Point(230, 230), "star.gif").clone()
    win = GraphWin("展示图片",width=600,height=500)
    im.draw(win)
    btn_ok.draw(win)
    p = win.getMouse()
    w = im.getWidth()
    h = im.getHeight()
    for i in range(h):
        for j in range(w):
            r,g,b=im.getPixel(j,i)
            mix = int(round(0.299*r+0.587*g+0.114*b))
            im.setPixel(j,i,color_rgb(mix,mix,mix))
            update()
    im.save("test2.gif")
    btn_ok.setText("转换换成,点击关闭！")
    win.getMouse()
    win.close()
if __name__ == '__main__':
    image_demo()