from tkinter import *
from tkinter import Label
from tkinter import messagebox
from PIL import Image,ImageTk
import customtkinter as ctk
import tkinter as tk
from email_store import email_store

class Otp(ctk.CTkFrame):
    def __init__(self, parent, controller,sent_otp=None):
        super().__init__(parent)
        self.otp = tk.StringVar()
        self.verified_email = None
        self.sent_otp = sent_otp
        self.configure(fg_color="#C6E2FF")
        #----------------------IMAGE PART-------------------------------

        self.phone_image = ImageTk.PhotoImage(file=r"E:\python\PythonProject\ Md Mahmood Ul Quaium\A_I_S_H_A\A_I_S_H_A\images\otp1.png")
        self.lbl_img1=Label(self,image=self.phone_image,bg="#C6E2FF").place(x=0,y=500,width=520,height=500)

        self.phone_image2 = ImageTk.PhotoImage(file=r"E:\python\PythonProject\ Md Mahmood Ul Quaium\A_I_S_H_A\A_I_S_H_A\images\otp2.png")
        self.lbl_img2 = Label(self, image=self.phone_image2, bg="#C6E2FF").place(x=1460, y=500, width=450,height=500)


        #----------------------forget Frame1------------------------------

        Otp_frame = ctk.CTkLabel(self,bg_color="#C6E2FF",width=300,height=300)
        Otp_frame.place(x=500,y=215)

        otp= ctk.CTkLabel(Otp_frame,text="Authentication Code", font=("Andalus",15),bg_color="#C6E2FF",fg_color="#C6E2FF",text_color="black").place(x=0,y=10)
        
        otpp = ctk.CTkEntry(Otp_frame,textvariable=self.otp,font=("times new roman",20),bg_color="#C6E2FF",justify='center').place(x=0,y=40)

        button = ctk.CTkButton(Otp_frame,  text="VERIFY", font=("Arial Rounded MT Bold", 15),
                        bg_color="#C6E2FF", fg_color="black",text_color="white",
                        cursor="hand2",command=lambda: self.verify_otp(controller), width=180, height=30).place(x=50, y=90)

        reg = ctk.CTkLabel(Otp_frame,text_color="black", text="Didn't receive code?", font=("times new roman", 15), bg_color="#C6E2FF",
                    fg_color="#C6E2FF").place(x=40, y=150)
        request_code = ctk.CTkButton(Otp_frame, text="Request again", font=("times new roman", 15), bg_color="#C6E2FF", fg_color="#C6E2FF",text_color="white",hover_color="#C6E2FF").place(x=150, y=150)

        #--------------------Forget frame2-------------
        Otp_frame2 = Label(self, bd=0, relief=RIDGE, bg="#C6E2FF")
        Otp_frame2.place(x=350, y=80, width=400, height=150)

        titel = Label(Otp_frame2, text="ACCOUNT", font=("Comic Sans MS", 30, "bold"), bg="#C6E2FF", fg="black").place(x=0, y=0,relwidth=1)
        titel = Label(Otp_frame2, text="VERIFICATION", font=("Comic Sans MS", 30, "bold"), bg="#C6E2FF", fg="black").place(x=0, y=50, relwidth=1)

    def verify_otp(self, controller):
        state = email_store()
        if self.otp.get() == state.sent_otp:
            messagebox.showinfo("Success", "OTP verified! You can reset your password now.")
            controller.show_frame("Change_pass")
        else:
            messagebox.showerror("Error", "Invalid OTP. Try again.")