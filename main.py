import tkinter
import csv
import os
from datetime import datetime

date = []

file_path = './预约表.csv'

def initialize():
    message = "此程序目前处于早期测试阶段，如有问题请联系微信：_n_u_l_l_ 姓名：徐梓傲，谢谢"
    print(message)
    try:
         print("正在检查数据文件")
         appointment = open(file_path)
         appointment.close()
    except FileNotFoundError:
        error_message = "预约数据未找到，可能被人为删除而造成数据丢失！\n正在重新生成新的数据文件"
        print(error_message)
        with open(file_path,'w',newline='') as f:
            write = csv.writer(f)
            head = ["姓名","年","月","日","起始时间","终止时间"]
            write.writerow(head) 
        print("已重新生成文件")
    print("数据文件已检查完毕")

def input_appointment():
    name = input("请输入您的姓名：")
    date.append(name)
    print("接下来我将询问您预定使用的时间和持续时间\n请您以阿拉伯数字分别输入并以回车结尾\n例如2023-2-28-13:30-14:30 代表预约在2023.2.28 13：30结束于14：30")
    appoint_time = input("请输入时间:")
    get_date = appoint_time.split('-')
    get_date[0] += '年'
    get_date[1] += '月'
    get_date[2] += '日'
    date.extend(get_date)

def check_appointment():
    print("正在为您打开预约数据文件，请在浏览完毕后关闭文件")
    os.system('pause')
    os.system('start ./预约表.csv')

def write_date():
    with open(file_path,'a',newline='') as f:
        write = csv.writer(f)
        write.writerow(date)
    print("写入成功！")
    os.system('pause')

initialize()
check_appointment()
input_appointment()
write_date()