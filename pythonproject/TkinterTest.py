import tkinter as tk
# coding=utf-8
# 每一个Tkinter应用的主体框架都可以包含下面这部分，定义windows窗口和windows的一些属性，然后书写窗口内容，最后执行windows mainloop让窗口活起来

# 窗口主体框架


windows = tk.Tk()  # 建立一个窗口对象
windows.title("My Windows")  # 窗口名字
windows.geometry('200x100')  # 窗口大小

var = tk.StringVar()

l = tk.Label(windows, text='OMG', bg='green', font=('Arial', 12), width=15, height=2)
l.pack()

windows.mainloop()
