from tkinter import *
import tkinter as tk
from tkinter import Label
from tkinter import messagebox
from PIL import Image,ImageTk
import customtkinter as ctk

import sql_repo

class Signup(ctk.CTkFrame):
   def __init__(self, parent, controller):
      super().__init__(parent)
      self.check=tk.BooleanVar()
      self.username = tk.StringVar()
      self.email = tk.StringVar()
      self.gender = tk.StringVar()
      self.password = tk.StringVar()
      self.confirm_password = tk.StringVar()
      self.date_of_birth = tk.StringVar()
      #----------------------IMAGE PART-------------------------------

      self.phone_image = ImageTk.PhotoImage(file=r"E:\python\PythonProject\ Md Mahmood Ul Quaium\A_I_S_H_A\A_I_S_H_A\images\pcpic.png")
      self.lbl_img1=Label(self,image=self.phone_image,bg="black",bd=0).place(x=950,y=129,width=720,height=703)


      #----------------------Login Frame------------------------------

      signupFrame = ctk.CTkLabel(self,bg_color="black",width=475,height=467)
      signupFrame.place(x=160,y=86,)

      titel = ctk.CTkLabel(signupFrame,text="CREATE AN ACCOUNT",text_color="white",font=("Comic Sans MS",20,"bold"),bg_color="black",fg_color="black").place(x=30,y=40,relwidth=1)

      username= ctk.CTkLabel(signupFrame,text_color="white",text="Username", font=("Andalus", 15),bg_color="black",fg_color="black").place(x=30,y=100)
      
      user = ctk.CTkEntry(signupFrame,textvariable=self.username,font=("times new roman",15),width=200,corner_radius=15,bg_color="black")
      user.place(x=30,y=130)

      mail = ctk.CTkLabel(signupFrame, text_color="white",text="Email Address", font=("Andalus", 15), bg_color="black", fg_color="black").place(x=30, y=170)
      
      email = ctk.CTkEntry(signupFrame,bg_color="black",textvariable=self.email,font=("times new roman",15),width=200,corner_radius=15)
      email.place(x=30,y=200)

      Birthday = ctk.CTkLabel(signupFrame, text_color="white",text="Date of birth", font=("Andalus", 15), bg_color="black", fg_color="black").place(x=30, y=230)

      birthday = ctk.CTkEntry(signupFrame, textvariable=self.date_of_birth, font=("times new roman", 15), bg_color="black").place(x=30,y=260)

      Gender = ctk.CTkLabel(signupFrame, text_color="white",text="Gender", font=("Andalus", 15), bg_color="black", fg_color="black").place(x=270, y=100)

      gen = ctk.CTkEntry(signupFrame,textvariable=self.gender, font=("times new roman", 15), bg_color="black").place(x=270, y=130)

      password = ctk.CTkLabel(signupFrame,text_color="white", text="Password", font=("Andalus", 15), bg_color="black", fg_color="black").place(x=270,y=160)

      pas = ctk.CTkEntry(signupFrame,width=200, corner_radius=15,textvariable=self.password, font=("times new roman", 15),bg_color="black").place(x=270, y=190)

      Comfirm_password = ctk.CTkLabel(signupFrame, text_color="white",text="Confirm Password", font=("Andalus", 15), bg_color="black", fg_color="black").place(x=270,y=220)
      
      Cpas = ctk.CTkEntry(signupFrame,width=200, corner_radius=15,textvariable=self.confirm_password, font=("times new roman", 15),bg_color="black").place(x=270, y=250)

      Checkbutton(
      signupFrame,
      text="I agree to the Terms & Conditions",
      variable=self.check,
      bg="black",
      fg="white",
      activebackground="black",
      activeforeground="white",
      selectcolor="gray20",   
      font=("Arial Rounded MT Bold",10)
      ).place(x=250, y=500)


      ctk.CTkButton(
      signupFrame,
      command=lambda: self.signup_action(controller),
      font=("Arial Rounded MT Bold",15),
      bg_color="black",
      fg_color="cyan3",
      text_color="black",
      text="Sign Up",
      cursor="hand2",
      width=180,
      height=30
      ).place(x=160,y=390,)
   def signup_action(self, controller):
      if not self.check.get():
         messagebox.showerror(
               "Error",
               "You must agree to the Terms & Conditions"
         )
         return
      if not sql_repo.SQLRepository.fetch_data( self.email.get())is None:
         messagebox.showerror(
               "Error",
               "Email already exists"
         )
         return
      if self.password.get() != self.confirm_password.get():
         messagebox.showerror(
               "Error",
               "Passwords do not match"
         )
         return
      sql_repo.SQLRepository.insert_data( self.username.get(), self.email.get(), self.date_of_birth.get(), self.gender.get(), self.password.get())
      messagebox.showinfo(
               "Success",
               "Account created successfully"
         )
      controller.show_frame("Login")