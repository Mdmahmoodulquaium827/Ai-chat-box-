from tkinter import *
from tkinter import Label
from tkinter import messagebox
from PIL import Image,ImageTk
import customtkinter as ctk
import tkinter as tk
import random
from email_store import email_store
import otp
import sql_repo

from sib_api_v3_sdk import ApiClient, Configuration
from sib_api_v3_sdk.api.transactional_emails_api import TransactionalEmailsApi
from sib_api_v3_sdk.models import SendSmtpEmail

SENDINBLUE_API_KEY = ""




class Forget_pass(ctk.CTkFrame):
   def __init__(self, parent, controller):
      super().__init__(parent)
      self.email = tk.StringVar()
      self.otp = None
      self.configure(fg_color="#C6E2FF")

      #----------------------IMAGE PART-------------------------------

      self.phone_image = ctk.CTkImage(
         light_image=Image.open(
            r"E:\python\PythonProject\ Md Mahmood Ul Quaium\A_I_S_H_A\A_I_S_H_A\images\Forgetpass1.png"
         ),
         size=(520, 500)
      )

      self.lbl_img1 = ctk.CTkLabel(
         self,
         image=self.phone_image,
         text="",
         fg_color="#C6E2FF",
         width=520,
         height=500
      )
      self.lbl_img1.place(x=0, y=150)

      self.phone_image2 = ctk.CTkImage(
         light_image=Image.open(
            r"E:\python\PythonProject\ Md Mahmood Ul Quaium\A_I_S_H_A\A_I_S_H_A\images\Forgetpass2.png"
         ),
         size=(450, 500)
      )

      self.lbl_img2 = ctk.CTkLabel(
         self,
         image=self.phone_image2,
         text="",
         fg_color="#C6E2FF",
         width=450,
         height=500
      )
      self.lbl_img2.place(x=800, y=150)

      #----------------------forget Frame1------------------------------

      forget_frame = ctk.CTkFrame(self,fg_color="#C6E2FF",width=300,height=300)
      forget_frame.place(x=500,y=215)

      mail= ctk.CTkLabel(forget_frame,text="Email Address", font=("Andalus",15),bg_color="#C6E2FF",text_color="black").place(x=0,y=10)
      Email = ctk.CTkEntry(forget_frame,width=220,textvariable=self.email,font=("times new roman",20),bg_color="#C6E2FF").place(x=0,y=40)

      button = ctk.CTkButton(forget_frame,  text="RESET", font=("Arial Rounded MT Bold", 15),
                     bg_color="#C6E2FF", fg_color="black",text_color="white",
                     cursor="hand2",command=lambda: self.check_email(controller), width=160, height=30).place(x=30, y=90)

      #--------------------Forget frame2-------------
      forget_frame2 = ctk.CTkFrame(self, fg_color="#C6E2FF", width=400, height=180)
      forget_frame2.place(x=350, y=50)

      titel = ctk.CTkLabel(forget_frame2, text="FORGOT", font=("Comic Sans MS", 40, "bold"), fg_color="Slate Gray1", bg_color="black").place(x=0, y=0,relwidth=1)
      titel = ctk.CTkLabel(forget_frame2, text="YOUR PASSWORD", font=("Comic Sans MS", 40, "bold"), fg_color="Slate Gray1", bg_color="black").place(x=0, y=70, relwidth=1)

   def generate_otp(self, length=6):
      return str(random.randint(10**(length-1), 10**length - 1))

   def send_otp_email(self, to_email, otp):
      configuration = Configuration()
      configuration.api_key['api-key'] = SENDINBLUE_API_KEY
      api_instance = TransactionalEmailsApi(ApiClient(configuration))

      send_smtp_email = SendSmtpEmail(
         to=[{"email": to_email}],
         sender={"email": "squallenix12@gmail.com"},
         subject="Your OTP Code",
         html_content=f"<p>Your OTP code is <strong>{otp}</strong></p>"
      )
      try:
         api_response = api_instance.send_transac_email(send_smtp_email)
         print(api_response)
         return True
      except Exception as e:
         print("Error sending OTP:", e)
         return False

   def check_email(self, controller):
      user = sql_repo.SQLRepository.fetch_data(self.email.get())
      if user:
         # Generate new OTP
         otp = self.generate_otp()
         sent = self.send_otp_email(self.email.get(), otp)
         
         if sent:
               messagebox.showinfo("Email Found", "An OTP has been sent to your email.")
               state = email_store()
               state.sent_otp = otp
               state.verified_email = self.email.get()
               controller.show_frame("Otp")  
         else:
               messagebox.showerror("Error", "Failed to send OTP. Try again.")
      else:
         messagebox.showerror("Email Not Found", "The provided email does not exist.")


   