from tkinter import *
from tkinter import ttk
import ui_settings
import profiledata
import userdata
import promo
from PIL import ImageTk,Image
import os
import time
import threading
import make_list_ui
from concurrent.futures import ThreadPoolExecutor

class promotion:

    def __init__(self):
        self.font = ui_settings.make_font("Arial Black", 11)
        self.font_sec = ui_settings.make_font("Arial Black", 8)
        self.pad_x = 15
        self.threads = []
    
    def promotion_(self):
        self.root3 = Tk()
        root3 = self.root3
        root3.geometry(ui_settings.promo_size)   
        root3.resizable(0,0)
        root3.wm_iconbitmap(default=os.path.join(os.path.dirname(__file__), "graphics/icon.ico"))
        root3.configure(background=ui_settings.primary_bg)
        root3.title("Promotion")
        root3.grid_columnconfigure(0, weight=1, uniform="fred")
        #data
        pad_x = self.pad_x
        line = Image.open(os.path.join(os.path.dirname(__file__), "graphics/line.png"))
        line.convert('RGBA')
        background = Image.new('RGB', line.size, root3['background'])
        background.paste(line, mask=line)
        line = ImageTk.PhotoImage(master=root3, image=background)
        #ui
        #
        #checkbox Like,Follow,Comment
        self.likeFollowComment_var = BooleanVar()
        likeFollowComment_box = Checkbutton(root3, var=self.likeFollowComment_var, font=self.font)
        likeFollowComment_box.config(background=ui_settings.primary_bg, foreground="black", activebackground=ui_settings.primary_bg, activeforeground="black")
        likeFollowComment_box.grid(row=0, column=0, sticky=W, padx=pad_x, pady=3)
        a1 = Label(root3, font=self.font, text="Follow, Like and Comment")
        a1.config(background=ui_settings.primary_bg, foreground=ui_settings.plain_text_fg)
        a1.grid(row=0, column=0, sticky=W, padx=pad_x*3, pady=3)
        #checkbox direct messaging
        self.direct_messaging_var = BooleanVar()
        direct_messaging_box = Checkbutton(root3, var=self.direct_messaging_var, font=self.font)
        direct_messaging_box.config(background=ui_settings.primary_bg, foreground="black", activebackground=ui_settings.primary_bg, activeforeground="black")
        direct_messaging_box.grid(row=1, column=0, sticky=W, padx=pad_x, pady=3)
        a2 = Label(root3, font=self.font, text="Direct Messaging")
        a2.config(background=ui_settings.primary_bg, foreground=ui_settings.plain_text_fg)
        a2.grid(row=1, column=0, sticky=W, padx=pad_x*3, pady=3)
        #checkbox unfollow_acc
        self.unfollow_acc_var = BooleanVar()
        unfollow_acc_box = Checkbutton(root3, var=self.unfollow_acc_var, font=self.font)
        unfollow_acc_box.config(background=ui_settings.primary_bg, foreground="black", activebackground=ui_settings.primary_bg, activeforeground="black")
        unfollow_acc_box.grid(row=3, column=0, sticky=W, padx=pad_x, pady=3)
        a3 = Label(root3, font=self.font, text="Unfollow")
        a3.config(background=ui_settings.primary_bg, foreground=ui_settings.plain_text_fg)
        a3.grid(row=3, column=0, sticky=W, padx=pad_x*3, pady=3)
        #divisor
        div = Label(root3, image=line, bg=ui_settings.primary_bg)
        div.image = line
        div.grid(row=4, columnspan=3, padx=10)
        #hashtag Button
        def hashtag_content_func():
            if(userdata.content_flag == False):
                userdata.content_flag = True
                make_list_ui.make_list_("hashtags").make_list_func()
        hashtag_bt = Button(root3, font=self.font, text="Set Hashtags", relief="flat", width=ui_settings.promo_size_x)
        hashtag_bt.config(command = hashtag_content_func,background=ui_settings.button_sec_bg, activebackground=ui_settings.button_sec_bg, foreground=ui_settings.widget_text_fg, activeforeground=ui_settings.widget_text_fg)
        hashtag_bt.grid(row=5, columnspan=3,  pady=10, padx=pad_x*2)
        #Comment Button
        def comment_content_func():
            if(userdata.content_flag == False):
                userdata.content_flag = True
                make_list_ui.make_list_("comments").make_list_func()
        comment_bt = Button(root3, font=self.font, text="Set Comments", relief="flat", width=ui_settings.promo_size_x)
        comment_bt.config(command = comment_content_func, background=ui_settings.button_sec_bg, activebackground=ui_settings.button_sec_bg, foreground=ui_settings.widget_text_fg, activeforeground=ui_settings.widget_text_fg)
        comment_bt.grid(row=6, columnspan=3,  pady=10, padx=pad_x*2)
        #dm Button
        def direcmessages_content_func():
            if(userdata.content_flag == False):
                userdata.content_flag = True
                make_list_ui.make_list_("direct messages").make_list_func()
        dm_bt = Button(root3, font=self.font, text="Set Direct Messages", relief="flat", width=ui_settings.promo_size_x)
        dm_bt.config(command = direcmessages_content_func, background=ui_settings.button_sec_bg, activebackground=ui_settings.button_sec_bg, foreground=ui_settings.widget_text_fg, activeforeground=ui_settings.widget_text_fg)
        dm_bt.grid(row=7, columnspan=3, pady=10, padx=pad_x*2)
        #divisor
        div2 = Label(root3, image=line, bg=ui_settings.primary_bg)
        div2.image = line
        div2.grid(row=8, columnspan=3, padx=10)
        #interaction amount
        interaction_wg = Entry(root3, show="", font=self.font_sec, borderwidth=8, relief="flat", width=ui_settings.promo_size_x)
        interaction_wg.config(background=ui_settings.entry_bg, foreground=ui_settings.greyed_fg)
        interaction_wg.insert(0,"Number of Interactions")
        interaction_wg.grid(row=9, columnspan=3, padx=pad_x*8, pady=10)
        def handle_click_interaction_wg(event):
            content_iw = interaction_wg.get()
            if(content_iw == "Number of Interactions"):
                interaction_wg.delete(0,END)
                interaction_wg.configure(foreground=ui_settings.widget_text_fg)
        interaction_wg.bind("<Button-1>", handle_click_interaction_wg)
        interaction_wg.bind("<Key>", handle_click_interaction_wg)
        #start button
        def start_prom():
            job_list = [self.likeFollowComment_var.get(), self.direct_messaging_var.get(), self.unfollow_acc_var.get()]
            interaction_number = interaction_wg.get()
            if(not interaction_number.isdigit()):
                interaction_number = 0
            else:
                interaction_number = int(interaction_number)
            if(job_list == [0,0,0]):
                self.set_pg_text("please select at least one of the options above")
                return
            if(userdata.hashtags ==[] or userdata.comments == []):
                self.set_pg_text("please set hashtags and comments")
                return
            if(interaction_number <= 0):
                self.set_pg_text("please set a number of interactions")
                return
            if((userdata.hashtags == [] or [elem for elem in userdata.hashtags if elem == " "] != []) and job_list[0]):
                self.set_pg_text("unvalid hashtags")
                return
            if((userdata.comments == [] or [elem for elem in userdata.comments if elem == " "] != []) and job_list[0]):
                self.set_pg_text("unvalid comments")
                return
            if((userdata.direct_messages == [] or [elem for elem in userdata.direct_messages if elem == " "] != []) and job_list[1]):
                self.set_pg_text("unvalid direct messages")
                return
            if(userdata.promo_running_flag == False):
                t1 = threading.Thread(target=lambda: promo.promo_func(userdata.hashtags, userdata.comments, interaction_number, job_list, self.pg_wg, self.pg_var, self.progressbar_wg))
                self.threads.append(t1)
                userdata.promo_running_flag = True
                t1.start()
        start_bt = Button(root3, state=NORMAL, text="Start", font=self.font, relief="flat", width=ui_settings.promo_size_x)
        start_bt.config(command = start_prom, background=ui_settings.button_primary_bg, activebackground=ui_settings.button_primary_bg, foreground=ui_settings.plain_text_fg, activeforeground=ui_settings.plain_text_fg)
        start_bt.grid(row=10, columnspan=3, padx=pad_x*2, pady=10)
        #divisor
        div3 = Label(root3, image=line, bg=ui_settings.primary_bg)
        div3.image = line
        div3.grid(row=11, columnspan=3, padx=10)
        #progressbar label
        self.pg_wg = Label(root3, text='Press "Start" to begin your Promotion', font=self.font_sec, width=ui_settings.promo_size_x)
        self.pg_wg.config(background=ui_settings.primary_bg, foreground=ui_settings.plain_text_fg)
        self.pg_wg.grid(row=12, columnspan=3, padx=pad_x, pady=5)
        #progressbar
        s = ttk.Style()
        s.configure("red.Horizontal.TProgressbar", background=ui_settings.primary_bg, foreground=ui_settings.greyed_fg)
        self.pg_var = DoubleVar()
        self.progressbar_wg = ttk.Progressbar(root3, style="red.Horizontal.TProgressbar", length=ui_settings.promo_size_x, mode="determinate", maximum=1, value=0, variable=self.pg_var)
        self.progressbar_wg.grid(row=13, columnspan=3, padx=pad_x*2, pady=10)
        #general check
        def gen_check(event):
            content_iw = interaction_wg.get()
            if([elem for elem in content_iw if not elem.isdigit()] != []):
                interaction_wg.delete(len(interaction_wg.get())-1,END)
        root3.bind("<Key>", gen_check)
        #mainloop
        root3.protocol("WM_DELETE_WINDOW", self.terminate)
        root3.mainloop()
    
    def set_pg_value(self, pg_value):
        print(pg_value)
        self.pg_var.set(pg_value)

    def set_pg_text(self, tx):
        self.pg_wg.config(text=tx)

    def terminate(self):
        userdata.promotion_flag = False
        userdata.promo_running_flag = False
        self.root3.destroy()
        for thread in self.threads:
            thread.join()



