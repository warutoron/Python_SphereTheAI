import tkinter as tk
import tkinter
import message

class Scribble:

    def create_window(self):

        # 参考
        # https://python.keicode.com/advanced/tkinter-widget-text.php

        # ウィンドウを生成
        window = tk.Tk()
        # ウィンドウ上部に表示するタイトル
        window.title('Sphere')
        #　サイズを固定
        window.geometry("540x390")
        # サイズ変更を許可しない(許可する場合は1を入力)
        window.resizable(0,0)

        # 画像の取得
        # img = tkinter.PhotoImage(file='backboard.png')
        # label1 = tkinter.Label(window, image=img)
        # label1.grid(row=1, column=1)

        self.text_widget = tk.Text(window)
        self.text_widget.pack()

        # メニュー
        menu = tk.Menu(window)
        window.config(menu = menu)
        # ファイルメニューボタン
        filemenu = tk.Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        # filemenu.add_command(label="New", command=message.callback)
        # filemenu.add_command(label="Open...", command=message.callback)
        # filemenu.add_separator()
        # filemenu.add_command(label="Exit", command=message.callback)

        helpmenu = tk.Menu(menu)
        menu.add_cascade(label="Help", menu=helpmenu)
        #helpmenu.add_command(label="About", command=message.callback)

        return window;
    
    def __init__(self):
        self.window = self.create_window();
            
    def run(self):
        self.window.mainloop()
 
Scribble().run()