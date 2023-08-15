# -*- coding:utf-8 -*-
import time
import tkinter
from tkinter import messagebox
import threading


user_window_count = 0
blacklist_window_count = 0
qrcode_window_count = 0
back_window_count = 0

def destroy_window(window_name):
    global user_window_count, blacklist_window_count, qrcode_window_count, back_window_count
    user_window_count = 0
    blacklist_window_count = 0
    qrcode_window_count = 0
    back_window_count = 0
    window_name.destroy()

#重复打开相同界面告警
def warning_window():
    messagebox.showwarning("警告", "不可同时打开多个相同界面！")

#通知
def notice(root_window, label_text):
    all_info = "Python图形用户系统欢迎您，如有任何问题，欢迎联系客服，联系电话123456789"
    #字幕左右滚动效果
    if len(all_info) >= 27:
        while True:
            #循环的步长设置为1，则为滚动效果，设置为27，则为分段翻动效果
            for i in range(0, len(all_info), 1):
                notice_str = all_info[i:i+27]
                #print(notice_str)
                label_text.configure(text=str(notice_str))
                root_window.update()
                time.sleep(1)
    else:
        label_text.configure(text=all_info)

#用户
def user():
    global user_window_count
    if user_window_count == 1:
        warning_window()
        return
    user_window = tkinter.Tk()
    user_window.title('用户管理界面')
    # 设置窗口大小:宽x高,注,此处不能为 "*",必须使用 "x"
    user_window.geometry('300x200+70+105')
    user_window["background"] = "#C9C9C9"
    button_user_close = tkinter.Button(user_window, text="关闭", width=6, height=1, command=lambda: destroy_window(user_window))
    button_user_close.place(x=130, y=165)
    user_window_count = 1

#黑名单
def blacklist():
    global blacklist_window_count
    if blacklist_window_count == 1:
        warning_window()
        return
    #blacklist_window = Toplevel(root_window)
    blacklist_window = tkinter.Tk()
    blacklist_window.title('黑名单处理界面')
    # 设置窗口大小:宽x高,注,此处不能为 "*",必须使用 "x"
    blacklist_window.geometry('300x200+70+105')
    blacklist_window["background"] = "#C9C9C9"
    button_blacklist_close = tkinter.Button(blacklist_window, text="关闭", width=6, height=1, command=lambda: destroy_window(blacklist_window))
    button_blacklist_close.place(x=130, y=165)
    blacklist_window_count = 1


#二维码
def qrcode():
    global qrcode_window_count
    if qrcode_window_count == 1:
        warning_window()
        return
    #back1_window = Toplevel(root_window)
    qrcode_window = tkinter.Tk()
    qrcode_window.title('二维码界面')
    # 设置窗口大小:宽x高,注,此处不能为 "*",必须使用 "x"
    qrcode_window.geometry('300x200+70+105')
    qrcode_window["background"] = "#C9C9C9"
    button_qrcode_close = tkinter.Button(qrcode_window, text="关闭", width=6, height=1, command=lambda: destroy_window(qrcode_window))
    button_qrcode_close.place(x=130, y=165)
    qrcode_window_count = 1

#备用
def back():
    global back_window_count
    if back_window_count == 1:
        warning_window()
        return
    #back2_window = Toplevel(root_window)
    back_window = tkinter.Tk()
    back_window.title('备用界面')
    # 设置窗口大小:宽x高,注,此处不能为 "*",必须使用 "x"
    back_window.geometry('300x200+70+105')
    back_window["background"] = "#C9C9C9"
    button_back_close = tkinter.Button(back_window, text="关闭", width=6, height=1, command=lambda: destroy_window(back_window))
    button_back_close.place(x=130, y=165)
    back_window_count = 1

#主窗口，一个通知，五个按钮（四个功能+一个关闭）
def create_tk():
    root_window = tkinter.Tk()
    # 设置窗口title
    root_window.title('Python图形用户界面')
    # 设置窗口大小:宽x高,注,此处不能为 "*",必须使用 "x"
    root_window.geometry('300x200+50+50')
    # 更改左上角窗口的的icon图标
    # 设置主窗口的背景颜色,颜色值可以是英文单词，或者颜色值的16进制数,除此之外还可以使用Tk内置的颜色常量
    root_window["background"] = "#C9C9C9"
    # 添加label,设置字体的前景色和背景色，和字体类型、大小
    label_text = tkinter.Label(root_window, text="", bg="#C9C9C9", fg="red")
    label_text.place(x=0, y=0)
    notice_thread = threading.Thread(target=notice, args=(root_window, label_text), daemon=True)
    notice_thread.start()
    # 添加按钮，以及按钮的文本，并通过command 参数设置关闭窗口的功能
    #button_user = tkinter.Button(root_window, text="用户管理", width=10, height=1, command=lambda: user(root_window))
    button_user = tkinter.Button(root_window, text="用户管理", width=10, height=1, command=user)
    button_blacklist = tkinter.Button(root_window, text="黑名单", width=10, height=1, command=blacklist)
    button_qrcode = tkinter.Button(root_window, text="二维码", width=10, height=1, command=qrcode)
    button_back = tkinter.Button(root_window, text="备用", width=10, height=1, command=back)
    button_close = tkinter.Button(root_window, text="关闭", width=6, height=1, command=root_window.quit)
    # 将按钮放置在主窗口内
    button_user.place(x=50, y=50)
    button_blacklist.place(x=175, y=50)
    button_qrcode.place(x=50, y=100)
    button_back.place(x=175, y=100)
    button_close.place(x=130, y=165)
    # 进入主循环，显示主窗口
    root_window.mainloop()

def main():
    create_tk()

if __name__ == '__main__':
    main()
