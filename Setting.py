from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from customtkinter import *
from tkinter import ttk
import customtkinter as ctk


class setting(ctk.CTkFrame):
    def __init__(self,parent, controller):
        super().__init__(parent)
        self.configure(fg_color="white")


        seting = CTkLabel(self, text="Setting", font=("Helvetica", 25))
        seting.place(x=140, y=13)


        phone_image = ImageTk.PhotoImage(file=r"E:\python\PythonProject\ Md Mahmood Ul Quaium\A_I_S_H_A\A_I_S_H_A\images\rsz_setting.png")

        lbl_img1 = Label(self, image=phone_image,bg='white')
        lbl_img1.image = phone_image
        lbl_img1.place(x=330, y=10,height=50,width=50)

        theme_mode  = CTkLabel(self, text="⚫Theme Mode", font=("Helvetica", 15))
        theme_mode.place(x=25, y=90)

        list1 = ['Dark Mode','Default']

        theme_mode_listbox = ttk.Combobox(self,values=list1,state="readonly")
        theme_mode_listbox.place(x=360, y=210)
        theme_mode_listbox.set("Select Mode")

        theme_mode_listbox.place(x=210, y=145)

        def change_theme(event):
            chatbox = controller.frames["Chatbox"]
            chatbox.apply_chatbox_theme(theme_mode_listbox.get())

        theme_mode_listbox.bind("<<ComboboxSelected>>", change_theme)

        list2 = ['English','Bengali','Japanese',
                'Hindi','Urdu','Nepali','Mandarin Chinese','Indonesian ']
        translate  = CTkLabel(self, text="⚫Translate", font=("Helvetica", 15))
        translate.place(x=25, y=135)

        translate_Combobox = ttk.Combobox(self,values=list2,state="readonly")
        translate_Combobox.place(x=210, y=210)
        translate_Combobox.set("Select Language")

        change_pass  = CTkLabel(self, text="⚫ ", font=("Helvetica", 15))
        change_pass.place(x=25, y=175)
        change_pass_button=Button(self, command=lambda :controller.show_frame("Change_pass"),text="Change Password", font=("Helvetica", 15),bg="white", fg="cyan3", bd=0,
                            activebackground="white",activeforeground="cyan3",cursor="hand2").place(x=80,y=268)

        back = Button(self, text="<-Back", font=("Helvetica", 20,"bold"), bg="white", fg="cyan3", bd=0,command=lambda: controller.show_frame("Chatbox"),
                                    activebackground="white", activeforeground="cyan3", cursor="hand2").place(x=430,
                                                                                                              y=650)

        about  = CTkLabel(self, text="⚫ ", font=("Helvetica", 15))
        about.place(x=25, y=255)
        about_button=Button(self, text="About", font=("Helvetica", 15),bg="white", fg="cyan3", bd=0,
                          activebackground="white",activeforeground="cyan3",cursor="hand2").place(x=80,y=385)


        shortcut  = CTkLabel(self, text="⚫ Shortcuts", font=("Helvetica", 15))
        shortcut.place(x=25, y=300)
        shortcut_astn  = CTkLabel(self, text="Open assistant                        ctrl+space", font=("Helvetica", 12))
        shortcut_astn.place(x=75, y=330)
        shortcut_chatnewline  = CTkLabel(self, text="Chat new line                           enter", font=("Helvetica", 12))
        shortcut_chatnewline.place(x=75, y=355)

