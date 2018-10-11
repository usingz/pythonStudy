import multiprocessing as mp
import threading as td
# coding=utf-8
'''
append_text = '\tThis is appended file'
my_file = open('my_file', 'a')# 'a'以增加内容的方式打开
my_file.write(append_text)
my_file.close()
'''
'''
file = open('my_file', 'r')
content = file.read()
print(content)
'''
# num = int(input())
# multiprocessing practice
# 定义一个被线程和进程调用的函数


def job(a,d):
    print('aaaaa')


# 创建线程和进程,调动的函数放在target后面，参数放在args中
t1 = td.Thread(target=job, args=(1,2))
p1 = mp.Process(target=job, args=(1,2))
t1.start()
p1.start()
t1.join()
p1.join()


