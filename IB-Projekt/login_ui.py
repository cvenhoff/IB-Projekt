from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import os
import ui_settings
import login
import time
import userdata
import threading
import wbdriver
from concurrent.futures import ThreadPoolExecutor

class login_ui_class:

    #init
    def __init__(self):
        self.font = ui_settings.make_font("Arial", 10)
        self.font_sec = ui_settings.make_font("Arial", 8)
        self.border_width = 12
        self.pad_x = 30
        self.root = Tk()

    #button function
    def login_start(self, username_wg, password_wg, root):
        self.stop = False
        #playing gif
        def loading_gif(speed):
            gifs = []
            for i in range(31):
                gifs.append(Image.open(os.path.join(os.path.dirname(__file__), "graphics/loading/frame-"+str(i)+".png")))
            gifs = [gif.resize((60,60)) for gif in gifs]
            load_widgets = []
            while(True):
                if(self.stop):
                    [elem.destroy() for elem in load_widgets]
                    break
                for gif in gifs:
                    if(self.stop):
                        [elem.destroy() for elem in load_widgets]
                        break
                    img = ImageTk.PhotoImage(gif)
                    load_widget = Label(root, image=img, borderwidth="0", bg = ui_settings.primary_bg)
                    load_widget.image = img
                    load_widget.grid(row=5, columnspan=3, sticky=W+E)
                    time.sleep(speed)
                    load_widgets.append(load_widget)
            return
        ThreadPoolExecutor().submit(loading_gif, 0.02)
        #login function
        username = username_wg.get()
        password = password_wg.get()
        userdata.username = username
        userdata.password = password
        res = login.login_func(username, password)
        if(res):
            self.stop = True
            if(self.remember_name_var.get() == True):
                with open(os.path.join(os.path.dirname(__file__),"username.txt"), "w") as file:
                    file.write(username_wg.get())
            self.root.destroy()
        else:
            login_text_wg = Label(root, text="wrong password or username", bg=ui_settings.primary_bg, fg=ui_settings.plain_text_fg)
            login_text_wg.grid(row=6, columnspan=3)
            login_text_wg.config(font=self.font_sec, foreground="red")
            self.stop = True

    #login function
    def login_(self):
        border_width = self.border_width 
        pad_x = self.pad_x 
        root = self.root
        font = self.font
        font_sec = self.font_sec
        #root settings
        root.geometry(ui_settings.login_size)   
        root.resizable(0,0)
        root.wm_iconbitmap(default=os.path.join(os.path.dirname(__file__), "graphics/icon.ico"))
        root.configure(background=ui_settings.primary_bg)
        root.title("Login")
        root.grid_columnconfigure(0, weight=1, uniform="fred")
        #data
        icon = Image.open(os.path.join(os.path.dirname(__file__), "graphics/icon.png"))
        icon = icon.resize((100,100))
        background = Image.new('RGB', icon.size, root['background'])
        icon.convert('RGBA')
        background.paste(icon, mask=icon)
        img = ImageTk.PhotoImage(background)
        login_text = "Log in to your Instagram account"
        #ui 
        #
        #icon
        icon_wg = Label(root, image=img, borderwidth="0")
        icon_wg.image = img
        icon_wg.grid(row=0, columnspan=3, pady=30)
        #text
        login_text_wg = Label(root, text=login_text, bg=ui_settings.primary_bg, fg=ui_settings.plain_text_fg)
        login_text_wg.grid(row=1, columnspan=3)
        login_text_wg.config(font=font)
        #username
        username_wg = Entry(root, font=font, relief="flat", borderwidth=border_width, width=ui_settings.login_size_x)
        username_wg.config(background=ui_settings.entry_bg, foreground="grey")
        with open(os.path.join(os.path.dirname(__file__),"username.txt"), "r") as file:
            username = file.read()
            if(username == "" or username == "username"):
                username = "username"
                username_wg.config(background=ui_settings.entry_bg, foreground="grey")
            else:
                username_wg.config(foreground=ui_settings.widget_text_fg)
        username_wg.insert(0,username)
        username_wg.grid(row=2, columnspan=3, pady=10, padx = pad_x)
        def handle_click_username(event):
            content_un = username_wg.get()
            if(content_un == "username"):
                username_wg.delete(0,END)
                username_wg.config(foreground=ui_settings.widget_text_fg)
        username_wg.bind("<Button-1>", handle_click_username)
        username_wg.bind("<Key>", handle_click_username)
        #password
        password_wg = Entry(root, show="", font=font, relief="flat", borderwidth=border_width, width=ui_settings.login_size_x)
        password_wg.config(background=ui_settings.entry_bg, foreground=ui_settings.greyed_fg)
        password_wg.insert(0,"password")
        password_wg.grid(row=3, columnspan=3, padx=pad_x, pady=10)
        def handle_click_password(event):
            content_pw = password_wg.get()
            if(content_pw == "password"):
                password_wg.delete(0,END)
                password_wg.configure(show="*", foreground=ui_settings.widget_text_fg)
        password_wg.bind("<Button-1>", handle_click_password)
        password_wg.bind("<Key>", handle_click_password)
        #check function
        def check_cond(event):
            content_pw = password_wg.get()
            content_un = username_wg.get()
            if(len(content_pw) > 5 and len(content_un) > 0 and content_pw != "password"):
                login_button.config(state=NORMAL)
            else:
                login_button.config(state=DISABLED)
        root.bind("<Key>", check_cond)
        #remember name
        self.remember_name_var = BooleanVar()
        remember_name_checkbox = Checkbutton(root, var=self.remember_name_var, borderwidth=0, relief="flat", font=font_sec)
        remember_name_checkbox.config(background=ui_settings.primary_bg, activebackground=ui_settings.primary_bg, foreground="black", activeforeground="black")
        remember_name_checkbox.grid(row=4, columnspan=3, sticky=W, padx=pad_x)
        Label(root, text="remember username", font=font_sec, bg=ui_settings.primary_bg, fg=ui_settings.greyed_fg).grid(row=4, columnspan=3, sticky=W, padx=pad_x+20)
        #login button
        login_button = Button(root, state=DISABLED, text="Login", font=font, relief=ui_settings.button_style, borderwidth=int(border_width/3), width=ui_settings.login_size_x)
        def start_login_thread():
            ThreadPoolExecutor().submit(self.login_start, username_wg, password_wg, root)
        login_button.config(command=start_login_thread, background=ui_settings.button_primary_bg, activebackground=ui_settings.button_primary_bg, foreground=ui_settings.plain_text_fg, activeforeground=ui_settings.plain_text_fg, disabledforeground=ui_settings.widget_text_fg)
        login_button.grid(row=5, columnspan=3, pady=30, padx=pad_x)
        def start_login_bykey(event):
            if(login_button['state'] == NORMAL):
                start_login_thread()
        root.bind("<Return>", start_login_bykey)
        #login status
        Label(root, bg=ui_settings.primary_bg).grid(row=6, columnspan=3)
        #privacy policy
        privacy_button = Button(root, text="privacy policy", borderwidth=0, relief="flat", font=font_sec)
        privacy_button.config(background=ui_settings.primary_bg, activebackground=ui_settings.primary_bg, foreground=ui_settings.plain_text_fg, activeforeground=ui_settings.plain_text_fg)
        privacy_button.grid(row=7, columnspan=3, pady=10)
        #mainloop
        def terminate():
            root.destroy()
            wbdriver.driver.quit()
        root.protocol("WM_DELETE_WINDOW", terminate)
        root.mainloop()

