from tkinter import *
from PIL import ImageTk, Image
import ui_settings
import profiledata
import userdata
import promotion_ui
import os
import threading
import wbdriver

class dashboard_ui_class:

    def __init__(self):
        self.font = ui_settings.make_font("Arial Black", 12)
        self.font_sec = ui_settings.make_font("Arial Black", 9)
        self.border_width = 10
        self.pad_x = 30
        self.promo = promotion_ui.promotion()

    def dashboard_(self):
        font = self.font 
        font_sec = self.font_sec
        border_width = self.border_width 
        pad_x = self.pad_x 
        profiledata.collect_pub_data()
        profiledata.get_profilepicture()
        #root settings
        self.root2 = Tk()
        root2 = self.root2
        root2.geometry(ui_settings.dashboard_size)   
        root2.resizable(0,0)
        root2.wm_iconbitmap(default=os.path.join(os.path.dirname(__file__), "graphics/icon.ico"))
        root2.configure(background=ui_settings.primary_bg)
        root2.title("Dashboard")
        root2.grid_columnconfigure(0, weight=1, uniform="fred")
        #data
        line = Image.open(os.path.join(os.path.dirname(__file__), "graphics/line.png"))
        line.convert('RGBA')
        background = Image.new('RGB', line.size, root2['background'])
        background.paste(line, mask=line)
        line = ImageTk.PhotoImage(master=root2, image=background)
        pp = Image.open(os.path.join(os.path.dirname(__file__),"pp.png"))
        pp = pp.resize((100,100))
        pp.convert('RGBA')
        img = ImageTk.PhotoImage(master=root2, image=pp)
        #ui
        #
        #divisor
        div0 = Label(root2, bg=ui_settings.primary_bg)
        div0.grid(row=0, columnspan=3)
        #bglabel
        Label(root2, bg=ui_settings.entry_bg).grid(rowspan=1, columnspan=3, sticky=N+S+W+E, padx=int(pad_x/2), pady=5)
        #profilepicture
        profilepicture_wg = Label(root2, image=img, relief="flat", borderwidth=3, bg=ui_settings.button_primary_bg)
        profilepicture_wg.image = img
        profilepicture_wg.grid(row=1, column=0, sticky=W, pady=15, padx=pad_x)
        #profilename
        profilename_wg = Label(root2, text="Profile: "+userdata.username, borderwidth=5, relief="flat")
        profilename_wg.config(font=font_sec, bg=ui_settings.entry_bg, fg=ui_settings.widget_text_fg)
        profilename_wg.grid(row=1, column=0, sticky=E+N, pady=15, padx=pad_x+(pad_x/5))
        #bigdivisor
        div1 = Label(root2, image=line, bg=ui_settings.primary_bg)
        div1.image = line
        div1.grid(row=2, columnspan=3, padx=15)
        #Abonnenten
        fl_wg = Label(root2, width=ui_settings.dashboard_size_x, borderwidth=border_width, relief="flat", text=profiledata.follower_number, bg=ui_settings.entry_bg, fg=ui_settings.widget_text_fg, font=font)
        fl_wg.grid(row=3, columnspan=3, pady=10, padx=pad_x)
        #divisor
        div2 = Label(root2, image=line, bg=ui_settings.primary_bg)
        div2.image = line
        div2.grid(row=4, columnspan=3, padx=40)
        #Abonniert
        fls_wg = Label(root2, width=ui_settings.dashboard_size_x, borderwidth=border_width, relief="flat", text=profiledata.follows_number, bg=ui_settings.entry_bg, fg=ui_settings.widget_text_fg, font=font)
        fls_wg.grid(row=5, columnspan=3, pady=10, padx=pad_x)
        #divisor
        div3 = Label(root2, image=line, bg=ui_settings.primary_bg)
        div3.image = line
        div3.grid(row=6, columnspan=3, padx=40)
        #content
        content_wg = Label(root2, width=ui_settings.dashboard_size_x, borderwidth=border_width, relief="flat", text=profiledata.content_number, bg=ui_settings.entry_bg, fg=ui_settings.widget_text_fg, font=font)
        content_wg.grid(row=7, columnspan=3, pady=10, padx=pad_x)
        #bigdivisor
        div3 = Label(root2, image=line, bg=ui_settings.primary_bg)
        div3.image = line
        div3.grid(row=8, columnspan=3, padx=15)
        #promotion button
        def start_promo():
            if(userdata.promotion_flag == False):
                threading.Thread(target=lambda: promotion_ui.promotion().promotion_()).start()
                userdata.promotion_flag = True
        promo_button = Button(root2, command=start_promo, width=ui_settings.dashboard_size_x, text="Start Promotion", font=font, relief=ui_settings.button_style, borderwidth=int(border_width/3))
        promo_button.config(background=ui_settings.button_primary_bg, activebackground=ui_settings.button_primary_bg, foreground=ui_settings.plain_text_fg, activeforeground=ui_settings.plain_text_fg)
        promo_button.grid(row=9, columnspan=3, pady=22, padx=int(pad_x/2))
        #mainloop
        root2.protocol("WM_DELETE_WINDOW", self.terminate)
        root2.mainloop()

    def terminate(self):
        self.root2.destroy()
        wbdriver.driver.quit()

