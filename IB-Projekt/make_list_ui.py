from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import os
import ui_settings
import login
import time
import userdata
import load_set_data
import threading
import emoji_converter
from concurrent.futures import ThreadPoolExecutor 

class make_list_:

    def __init__(self, content_id):
        self.content_id = content_id
        self.root4 = Tk()
        self.id = ""
        if(content_id == "hashtags"):
            self.id = userdata.hashtags
        if(content_id == "comments"):
            self.id = userdata.comments
        if(content_id == "direct messages"):
            self.id = userdata.direct_messages
        self.font = ui_settings.make_font("Arial", 13)
        self.font_sec = ui_settings.make_font("Arial", 10)
        self.emoji_flag = False
        self.content = []

    def make_list_func(self):
        root4 = self.root4
        Grid.rowconfigure(root4, 0, weight=1)
        Grid.columnconfigure(root4, 0, weight=1)
        root4.geometry(ui_settings.list_size)   
        root4.resizable(1,0)
        root4.wm_iconbitmap(default=os.path.join(os.path.dirname(__file__), "graphics/icon.ico"))
        root4.configure(background=ui_settings.primary_bg)
        root4.title(self.content_id)
        root4.grid_columnconfigure(0, weight=1, uniform="fred")
        #ui
        #
        #display
        scrollbar = Scrollbar(root4)
        scrollbar.grid(row=0, column=2, sticky=N+S+E)
        listbox = Listbox(root4, yscrollcommand=scrollbar.set)
        for elem in self.id:
            listbox.insert(END, str(elem))
        listbox.grid(row=0, columnspan=2, sticky=W+E+N+S)
        scrollbar.config(command=listbox.yview)
        listbox.config(background=ui_settings.primary_bg, foreground=ui_settings.plain_text_fg, font=self.font)
        #entry
        add_content_wg = Entry(root4, show="", font=self.font_sec, borderwidth=8, relief="flat", width=ui_settings.promo_size_x)
        add_content_wg.config(background=ui_settings.entry_bg, foreground=ui_settings.greyed_fg)
        add_content_wg.insert(0,"add content")
        add_content_wg.grid(row=2, columnspan=3, sticky=E+W+N+S)
        def handle_click_content_wg(event):
            content_iw = add_content_wg.get()
            if(content_iw == "add content"):
                add_content_wg.delete(0,END)
                add_content_wg.configure(foreground=ui_settings.widget_text_fg)
        add_content_wg.bind("<Button-1>", handle_click_content_wg)
        add_content_wg.bind("<Key>", handle_click_content_wg)
        #emojis
        boxlist = []
        def show_emojis():
            if(self.emoji_flag == False):
                emojilist = Listbox(root4, width=0)
                boxlist.append(emojilist)
                self.emoji_flag = True
                for elem in userdata.emojis:
                    emojilist.insert(END, userdata.emojis[elem])
                emojilist.grid(row=0, rowspan=3, column=3, sticky=N+S)
                emojilist.config(background=ui_settings.primary_bg, foreground=ui_settings.plain_text_fg, font=self.font)
            else:
                self.emoji_flag = False
                for elem in boxlist:
                    elem.destroy()
        def insert_emoji(event):
            if(self.emoji_flag):
                res = boxlist[0].curselection()
                if(res != ()):
                    handle_click_content_wg(event)
                    add_content_wg.insert(END, list(userdata.emojis.values())[res[0]])
                    boxlist[0].selection_clear(0,END)
            else:
                return
        #emoji button
        emoji_button = Button(root4, text="😂", borderwidth=0, relief="flat")
        emoji_button.config(command=show_emojis, background=ui_settings.button_primary_bg, activebackground=ui_settings.button_primary_bg)
        emoji_button.grid(row=2, column=2, sticky=E+W+S+N)
        root4.bind("<Button-1>", insert_emoji)
        #add content
        def add_content(event):
            content = str(add_content_wg.get())
            if(content=="" or content=="add content"):
                return
            else:
                self.content.append(emoji_converter.emoji_to_text(content))
                listbox.insert(END,content)
                add_content_wg.delete(0,END)
        root4.bind("<Return>", add_content)
        #delete
        def delete_selection(event):
            sel = listbox.curselection()
            if(sel == ()):
                return
            else:
                listbox.delete(sel[0], sel[0])
        root4.bind("<BackSpace>", delete_selection)
        #makeloop
        def terminate():
            try:
                if(userdata.promo_running_flag == False):
                    content = ["~".join(userdata.hashtags), "~".join(userdata.comments), "~".join(userdata.direct_messages)]
                    if(self.content_id == "hashtags"):
                        content = ["~".join(self.content), "~".join(userdata.comments), "~".join(userdata.direct_messages)]
                    if(self.content_id == "comments"):
                        content = ["~".join(userdata.hashtags), "~".join(self.content), "~".join(userdata.direct_messages)]
                    if(self.content_id == "direct messages"):
                        content = ["~".join(userdata.hashtags), "~".join(userdata.comments), "~".join(self.content)]
                    load_set_data.set_data(content)
                    load_set_data.get_data()
            except Exception:
                pass
            userdata.content_flag = False
            root4.destroy()
        root4.protocol("WM_DELETE_WINDOW", terminate)
        root4.mainloop()

make_list_("hashtags").make_list_func()

