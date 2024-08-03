from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector
import re
from tkinter import Tk, Button, Toplevel



def main():
    win=Tk()
    app=login(win)
    win.mainloop()



class login:
    def __init__(self,root):
        self.root=root 
        self.root.title("Login Form")
        self.root.geometry("1600x900+0+0")
        
        self.new_window = None
        
        
        # Load the background image
        bg_image = Image.open(r"D:\Library Management System\lms_back1.png")
        # Resize the image to fit the window size
        bg_image = bg_image.resize((1600, 900), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(bg_image)
        
        lbl_bg = Label(self.root, image=self.bg)
        # Place the image to cover the entire window
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)
        
        frame=Frame(self.root,bg="black")
        #frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        frame.place(x=610,y=170,width=340,height=450)
        
        # self.Center(direction=wx.VERTICAL)
        
        img1=Image.open(r"D:\Library Management System\user-avatar-red-icon-vector-8825308.jpg")
        img1=img1.resize((100,100),Image.BILINEAR)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)
        
        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=110)
        
        #LABLE
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)
        
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)
        
        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)
        
        self.password=ttk.Entry(frame,font=("times new roman",15,"bold"),show="*")
        self.password.place(x=40,y=250,width=270)
        
        #ICON IMAGES
        img2=Image.open(r"D:\Library Management System\9187604.png")
        img2=img2.resize((25,25),Image.BILINEAR)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=323,width=25,height=25)
        
        img3=Image.open(r"D:\Library Management System\lock1.jpg")
        img3=img3.resize((25,25),Image.BILINEAR)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=395,width=25,height=25)
        
        #LOGINBUTTON
        loginbtn=Button(frame,command=self.loginbtn,text="Login",font=("times new roman",10,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)
        
        #REGISTRATIONBUTTON
        registerbtn=Button(frame,command=self.register_window,text="New User Register",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)
        
        #PASSWORDBUTTON
        forgetpasswordbtn=Button(frame,command=self.forgot_password_window,text="Forget Password",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgetpasswordbtn.place(x=10,y=370,width=160)
        
        
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
        
    def loginbtn(self):
        self.new_window=Toplevel(self.root)
        if self.txtuser.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All field Required")
        elif self.txtuser.get()=="Saurabh" and self.password.get()=="1234":
            messagebox.showinfo("Success", "Login Sucessfully")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="mydata")
            mycursor=conn.cursor()
            mycursor.execute("select * from register where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.password.get()
                
                                                        ))
            
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Usename and Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only Admin")
                if open_main>0:
                    self.new_window=Toplevel(self.new_window)
                    self.app=LibraryManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
                    
            conn.commit()
            conn.close()
    #RESET
    def reset_pass(self):
        if self.combo_securiy_Q.get()=="Select":
            messagebox.showerror("Error","Select security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error", "Plase enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error", "Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="mydata")
            mycursor=conn.cursor()
            query=("SELECT * FROM register WHERE email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_securiy_Q.get(),self.txt_security.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error", "Plaese enter correct Answer",parent=self.root2)
            else:
                query=("UPDATE register SET password=%s WHERE email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                mycursor.execute(query,value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset ,plaese login new password",parent=self.root2)
                self.root2.destroy()
            
        
    
    
    
    
    
    
    #FORGET PASSWORD
            
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter Email to Reset Password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="mydata")
            mycursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            #print(row)
            
            if row==None:
                messagebox.showerror("Error","Please Enter Valid UserName")
            else:
                conn.close()
                self.root2=Tk()
                #self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")
                
                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)
                
                security_Q = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white", fg="black")
                security_Q.place(x=50, y=80)

                self.combo_securiy_Q = ttk.Combobox(self.root2,font=("times new roman", 15, "bold"), state="readonly")
                self.combo_securiy_Q["values"] = ("Select", "Your Birth Place", "Your School Name", "Your Childhood Name")
                self.combo_securiy_Q.place(x=50, y=110, width=250)
                self.combo_securiy_Q.current(0)

                security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
                security_A.place(x=50, y=150)

                self.txt_security = ttk.Entry(self.root2,font=("times new roman", 15,"bold"))
                self.txt_security.place(x=50, y=180, width=250)
                
                new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
                new_password.place(x=50, y=220)

                self.txt_newpass = ttk.Entry(self.root2,font=("times new roman", 15,"bold"))
                self.txt_newpass.place(x=50, y=250,width=250)
                
                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)
                
                
                        
                
                
            
            
            
class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        
        # VARIABLES
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()
        self.var_check = IntVar()
        
        self.bg = ImageTk.PhotoImage(file=r"D:\Library Management System\regsbackground_resize.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)
        
        # MAINFRAME
        frame = Frame(self.root, bg="white")
        frame.place(x=420, y=240, width=680, height=500)
        
        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="black", bg="white")
        register_lbl.place(x=35, y=20)
        
        # LABEL AND ENTRY
        
        # ROW1
        fname = Label(frame, text="First Name", font=("times new roman", 16, "bold"), bg="white")
        fname.place(x=50, y=100)
        
        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        fname_entry.place(x=50, y=130, width=250)

        l_name = Label(frame, text="Last Name", font=("times new roman", 16, "bold"), bg="white")
        l_name.place(x=370, y=100)
        
        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15,"bold"))
        self.txt_lname.place(x=370, y=130, width=250)
        
        # ROW2
        contact = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white", fg="black")
        contact.place(x=50, y=170)
        
        self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15))
        self.txt_contact.place(x=50, y=200, width=250)
        
        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=170)
        
        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15))
        self.txt_email.place(x=370, y=200, width=250)

        # ROW3
        security_Q = Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_Q.place(x=50, y=240)

        self.combo_securiy_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_securiy_Q["values"] = ("Select", "Your Birth Place", "Your School Name", "Your Childhood Name")
        self.combo_securiy_Q.place(x=50, y=270, width=250)
        self.combo_securiy_Q.current(0)

        security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_A.place(x=370, y=240)

        self.txt_security = ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15))
        self.txt_security.place(x=370, y=270, width=250)
        
        # ROW4
        pswd = Label(frame, text="Password ", font=("times new roman", 15, "bold"), bg="white", fg="black")
        pswd.place(x=50, y=310)
        
        self.txt_pswd = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15), show="*")
        self.txt_pswd.place(x=50, y=340, width=250)
        
        confirm_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        confirm_pswd.place(x=370, y=310)
        self.txt_confirm_pswd = ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman", 15), show="*")
        self.txt_confirm_pswd.place(x=370, y=340, width=250)
        
        # CHECKBUTTON
        chechbtn = Checkbutton(frame, variable=self.var_check, text="I Agree with the terms and Conditions", font=("times new roman", 12, "bold"), onvalue=1, offvalue=0)
        chechbtn.place(x=40, y=380)
        
        # BUTTONS
        img = Image.open(r"D:\Library Management System\registerbtn.jpg")
        img = img.resize((200, 55), Image.BILINEAR)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, image=self.photoimage, command=self.register_data, borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"))
        b1.place(x=22, y=427, width=200)
        
        img1 = Image.open(r"D:\Library Management System\loginnow1.jpg")
        img1 = img1.resize((200, 117), Image.BILINEAR)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1, command=self.return_login, borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"))
        b1.place(x=338, y=410, width=200)
        
    # FUNCTION
    def register_data(self):
        # Validate first name
        if not self.var_fname.get().isalpha():
            messagebox.showerror("Error", "First name must contain only alphabets")
            return
        
        # Validate last name
        if not self.var_lname.get().isalpha():
            messagebox.showerror("Error", "Last name must contain only alphabets")
            return
        
        # Validate contact number
        if not re.match(r"^\d{10}$", self.var_contact.get()):
            messagebox.showerror("Error", "Contact number must be a 10-digit number")
            return
        
        # Validate email
        if not re.match(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", self.var_email.get()):
            messagebox.showerror("Error", "Invalid email address")
            return
        

        # Validate password
        password = self.var_pass.get()
        if len(password) < 12 or not re.search(r'[A-Z]', password) or not re.search(r'[^a-zA-Z0-9]', password):
            messagebox.showerror("Error", "Password must be at least 12 characters long, contain a capital letter and a special character")
            return
        
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password & confirm password must be the same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to our terms and conditions")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="1234", database="mydata")
            mycursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.var_email.get(),)
            mycursor.execute(query, value)
            row = mycursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "User Already Exists")
            else:
                mycursor.execute("INSERT INTO register VALUES(%s, %s, %s, %s, %s, %s, %s)", (
                    self.var_fname.get(),
                    self.var_lname.get(), 
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()
                ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Registration successful")
            
    def return_login(self):
        self.root.destroy()

            
            
            
class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1550x850+0+0")
        
        
        
        
        #************VARIABLE DECLEARATION**************************
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.auther_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook=StringVar()
        self.lateratefine_var=StringVar()
        self.dateoverdue=StringVar()
        self.finalprice=StringVar()

        
        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="black",fg="#90EE90",bd=20,
                       relief=RIDGE,font=("time new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)
        
        
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1550,height=410)
        
        # ***************DATA FRAME LEFT************************
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("time new roman",15,"bold"),padx=2,pady=6)
        DataFrameLeft.place(x=0,y=5,width=860,height=370)
        
        lblMemebr=Label(DataFrameLeft,bg="powder blue",textvariable=self.member_var,text="Member Type:",font=("time new roman",13,"bold"),padx=2,pady=6)
        lblMemebr.grid(row=0,column=0,sticky=W)
        
        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("arial",13,"bold"),width=27,state="readonly")
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.grid(row=0,column=1)
        
        lblPRN_NO=Label(DataFrameLeft,font=("arial",12,"bold"),text="PRN NO:",padx=4,bg="powder blue")
        lblPRN_NO.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.prn_var,width=29)
        txtPRN_NO.grid(row=1,column=1)
        
        lblTitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="ID No:",padx=2,pady=4,bg="powder blue")
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.id_var,width=29)
        txtTitle.grid(row=2,column=1)
        
        lblFirstName=Label(DataFrameLeft,font=("arial",12,"bold"),text="FirstName",padx=2,pady=6,bg="powder blue")
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.firstname_var,width=29)
        txtFirstName.grid(row=3,column=1)
        
        lblLastName=Label(DataFrameLeft,font=("arial",12,"bold"),text="LastName",padx=2,pady=6,bg="powder blue")
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.lastname_var,width=29)
        txtLastName.grid(row=4,column=1)
        
        lblAddress1=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address1",padx=2,pady=6,bg="powder blue")
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address1_var,width=29)
        txtAddress1.grid(row=5,column=1)
        
        lblAddress2=Label(DataFrameLeft,font=("arial",12,"bold"),text="Address2",padx=2,pady=6,bg="powder blue")
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.address2_var,width=29)
        txtAddress2.grid(row=6,column=1)
        
        lblPostCode=Label(DataFrameLeft,font=("arial",12,"bold"),text="Post Code",padx=2,pady=6,bg="powder blue")
        lblPostCode.grid(row=7,column=0,sticky=W)
        lblPostCode=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.postcode_var,width=29)
        lblPostCode.grid(row=7,column=1)
        
        lblMobile=Label(DataFrameLeft,font=("arial",12,"bold"),text="Mobile No:",padx=2,pady=6,bg="powder blue")
        lblMobile.grid(row=8,column=0,sticky=W)
        lblMobile=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.mobile_var,width=29)
        lblMobile.grid(row=8,column=1)
        
        lblBookId=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book Id:",padx=2,pady=6,bg="powder blue")
        lblBookId.grid(row=0,column=2,sticky=W)
        lblBookId=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.bookid_var,width=29)
        lblBookId.grid(row=0,column=3)
        
        lblBookTitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book Title:",padx=2,pady=6,bg="powder blue")
        lblBookTitle.grid(row=1,column=2,sticky=W)
        lblBookTitle=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.booktitle_var,width=29)
        lblBookTitle.grid(row=1,column=3)
        
        lblAuther=Label(DataFrameLeft,font=("arial",12,"bold"),text="Auther Name:",padx=2,pady=6,bg="powder blue")
        lblAuther.grid(row=2,column=2,sticky=W)
        lblAuther=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.auther_var,width=29)
        lblAuther.grid(row=2,column=3)
        
        # lblAuther=Label(DataFrameLeft,font=("arial",12,"bold"),text="Auther Name:",padx=2,pady=6,bg="powder blue")
        # lblAuther.grid(row=2,column=2,sticky=W)
        # lblAuther=Entry(DataFrameLeft,font=("arial",12,"bold"),width=29)
        # lblAuther.grid(row=2,column=3)
        
        lblDateBorrowed=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Borrowed:",padx=2,pady=6,bg="powder blue")
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        lblDateBorrowed=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.dateborrowed_var,width=29)
        lblDateBorrowed.grid(row=3,column=3,sticky=W)
        
        lblDateDue=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Due:",padx=2,pady=6,bg="powder blue")
        lblDateDue.grid(row=4,column=2,sticky=W)
        lblDateDue=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.datedue_var,width=29)
        lblDateDue.grid(row=4,column=3,sticky=W)
        
        lblDaysOnBook=Label(DataFrameLeft,font=("arial",12,"bold"),text="Days On Book:",padx=2,pady=6,bg="powder blue")
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        lblDaysOnBook=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.daysonbook,width=29)
        lblDaysOnBook.grid(row=5,column=3,sticky=W)
        
        lbllateReturnFine=Label(DataFrameLeft,font=("arial",12,"bold"),text="Late Return Fine:",padx=2,pady=6,bg="powder blue")
        lbllateReturnFine.grid(row=6,column=2,sticky=W)
        lbllateReturnFine=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.lateratefine_var,width=29)
        lbllateReturnFine.grid(row=6,column=3,sticky=W)
        
        lblOvedate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Over Due:",padx=2,pady=6,bg="powder blue")
        lblOvedate.grid(row=7,column=2,sticky=W)
        lblOvedate=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.dateoverdue,width=29)
        lblOvedate.grid(row=7,column=3,sticky=W)
        
        lblActualPrice=Label(DataFrameLeft,font=("arial",12,"bold"),text="Actual Price:",padx=2,pady=6,bg="powder blue")
        lblActualPrice.grid(row=8,column=2,sticky=W)
        lblActualPrice=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.finalprice,width=29)
        lblActualPrice.grid(row=8,column=3,sticky=W)
        
        
        
        #****************DATAFRAME RIGHT************************************
        DataFrameRight=LabelFrame(frame,bd=12,padx=20,relief=RIDGE,bg="powder blue",
                                    font=("arial",12,"bold"),text="Book Details")
        DataFrameRight.place(x=870,y=5,width=580,height=368)
        
        
        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)
        
        listScroolbar=Scrollbar(DataFrameRight)
        listScroolbar.grid(row=0,column=1,sticky="ns")
        
        listBooks=['Fluent Python','Learning Python','Python for Data Analysis','Head First Python','Think Python',
                   'Dive Into Python 3','Python in a Nutshell','Python for Everybody','Effective Java','Head First Java',
                   'Thinking in Java','Java EE 7 Essentials','Spring in Action','Programming in C','C Primer Plus','Head First C',
                   'Effective C++','Effective STL','Python for Data Analysis','Applied Predictive Modeling','A Probabilistic Perspective',
                   'Machine Learning Yearning','Machine Learning for Hackers']
        
        
        def select_Book(event=""):
            selected_index = listBox.curselection()
            if selected_index:  
                values = str(listBox.get(selected_index))
                print(values)  

                if values == "Fluent Python":
                    self.bookid_var.set("BKID-P1")
                    self.booktitle_var.set("Programming")  
                    self.auther_var.set("Luciano Ramalho")

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set(15)
                    self.lateratefine_var.set("₹50")
                    self.dateoverdue.set("NO")
                    self.finalprice.set("₹749")
                elif values == "Learning Python":
                    self.bookid_var.set("BKID-P2")
                    self.booktitle_var.set("Programming")  
                    self.auther_var.set(" Mark Lutz")  

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set(15)
                    self.lateratefine_var.set("₹50")
                    self.dateoverdue.set("NO")
                    self.finalprice.set("₹989")
                elif values == "Python for Data Analysis":
                    self.bookid_var.set("BKID-P3")
                    self.booktitle_var.set("Programming")  
                    self.auther_var.set("Wes McKinney")  

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set(15)
                    self.lateratefine_var.set("₹50")
                    self.dateoverdue.set("NO")
                    self.finalprice.set("₹765")
                elif values == "Head First Python":
                    self.bookid_var.set("BKID-P4")
                    self.booktitle_var.set("Programming")  
                    self.auther_var.set("Paul Barry")  

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set(15)
                    self.lateratefine_var.set("₹50")
                    self.dateoverdue.set("NO")
                    self.finalprice.set("₹678")
                elif values == "Think Python":
                    self.bookid_var.set("BKID-P5")
                    self.booktitle_var.set("Programming")  
                    self.auther_var.set("Allen B. Downey")  

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set(15)
                    self.lateratefine_var.set("₹50")
                    self.dateoverdue.set("NO")
                    self.finalprice.set("₹988")
                elif values == "Dive Into Python 3":
                    self.bookid_var.set("BKID-P6")
                    self.booktitle_var.set("Programming")  
                    self.auther_var.set("Mark Pilgrim")  

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set(15)
                    self.lateratefine_var.set("₹50")
                    self.dateoverdue.set("NO")
                    self.finalprice.set("₹1395")
                elif values == "Python in a Nutshelli":
                    self.bookid_var.set("BKID-7")
                    self.booktitle_var.set("Programming")  
                    self.auther_var.set("Alex Martelli")  

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set(15)
                    self.lateratefine_var.set("₹50")
                    self.dateoverdue.set("NO")
                    self.finalprice.set("₹1258")
                elif values == "Python for Everybody":
                    self.bookid_var.set("BKID-8")
                    self.booktitle_var.set("Programming")  
                    self.auther_var.set("Charles Severance")  

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set(15)
                    self.lateratefine_var.set("₹50")
                    self.dateoverdue.set("NO")
                    self.finalprice.set("₹1958")
                elif values == "Effective Java":
                    self.bookid_var.set("BKID-J1")
                    self.booktitle_var.set("Programming")  
                    self.auther_var.set("Joshua Bloch")  

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set(15)
                    self.lateratefine_var.set("₹50")
                    self.dateoverdue.set("NO")
                    self.finalprice.set("₹2120")
                elif values == "Head First Java":
                    self.bookid_var.set("BKID-J2")
                    self.booktitle_var.set("Programming")  
                    self.auther_var.set("Kathy Sierra and Bert Bates") 

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set(15)
                    self.lateratefine_var.set("₹50")
                    self.dateoverdue.set("NO")
                    self.finalprice.set("₹1896")
                elif values == "Thinking in Java":
                    self.bookid_var.set("BKID-J3")
                    self.booktitle_var.set("Programming")  
                    self.auther_var.set("Bruce Eckel")  

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set(15)
                    self.lateratefine_var.set("₹50")
                    self.dateoverdue.set("NO")
                    self.finalprice.set("₹1493")
                elif values == "Java Cookbook":
                    self.bookid_var.set("BKID-J4")
                    self.booktitle_var.set("Programming")  
                    self.auther_var.set("Ian F. Darwin")  

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set(15)
                    self.lateratefine_var.set("₹50")
                    self.dateoverdue.set("NO")
                    self.finalprice.set("₹1358")
                elif values == "Java EE 7 Essentials":
                    self.bookid_var.set("BKID-J5")
                    self.booktitle_var.set("Programming")  
                    self.auther_var.set(" Arun Gupta")  

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set(15)
                    self.lateratefine_var.set("₹50")
                    self.dateoverdue.set("NO")
                    self.finalprice.set("₹1700")
                elif values == "Spring in Action":
                    self.bookid_var.set("BKID-J6")
                    self.booktitle_var.set("Programming")  
                    self.auther_var.set("Craig Walls")  

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set(15)
                    self.lateratefine_var.set("₹50")
                    self.dateoverdue.set("NO")
                    self.finalprice.set("₹1890")
                elif values == "Programming in C":
                    self.bookid_var.set("BKID-C1")
                    self.booktitle_var.set("Programming")  
                    self.auther_var.set("Stephen G. Kochan")  

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set(15)
                    self.lateratefine_var.set("₹50")
                    self.dateoverdue.set("NO")
                    self.finalprice.set("₹738")
                elif values == "C Primer Plus":
                    self.bookid_var.set("BKID-C2")
                    self.booktitle_var.set("Programming")  
                    self.auther_var.set("Stephen Prata")  

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set(15)
                    self.lateratefine_var.set("₹50")
                    self.dateoverdue.set("NO")
                    self.finalprice.set("₹499")
                elif values == "Effective C++":
                    self.bookid_var.set("BKID-C++1")
                    self.booktitle_var.set("Programming")  
                    self.auther_var.set("Scott Meyers")  

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set(15)
                    self.lateratefine_var.set("₹50")
                    self.dateoverdue.set("NO")
                    self.finalprice.set("₹2758")
                elif values == "Effective STL":
                    self.bookid_var.set("BKID-C++2")
                    self.booktitle_var.set("Programming")  
                    self.auther_var.set("Scott Meyers")  

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set(15)
                    self.lateratefine_var.set("₹50")
                    self.dateoverdue.set("NO")
                    self.finalprice.set("₹2508")
                #
                elif values == "Python for Data Analysis":
                    self.bookid_var.set("BKID-DA1")
                    self.booktitle_var.set("Data Analysis")  
                    self.auther_var.set("Wes McKinney")  

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set(15)
                    self.lateratefine_var.set("₹150")
                    self.dateoverdue.set("NO")
                    self.finalprice.set("₹1389")
                elif values == "Applied Predictive Modeling":
                    self.bookid_var.set("BKID-DA2")
                    self.booktitle_var.set("Data Analysis")  
                    self.auther_var.set("Max Kuhn and Kjell Johnson")  

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set(15)
                    self.lateratefine_var.set("₹15")
                    self.dateoverdue.set("NO")
                    self.finalprice.set("₹508")
                elif values == "A Probabilistic Perspective":
                    self.bookid_var.set("BKID-ML1")
                    self.booktitle_var.set("Machine Learning")  
                    self.auther_var.set("Kevin P. Murphy")  

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set(15)
                    self.lateratefine_var.set("₹225")
                    self.dateoverdue.set("NO")
                    self.finalprice.set("₹1508")
                elif values == "Machine Learning Yearning":
                    self.bookid_var.set("BKID-ML2")
                    self.booktitle_var.set("Machine Learning")  
                    self.auther_var.set("Andrew Ng")  

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set(15)
                    self.lateratefine_var.set("₹350")
                    self.dateoverdue.set("NO")
                    self.finalprice.set("₹5208")
                elif values == "Machine Learning for Hackers":
                    self.bookid_var.set("BKID-ML3")
                    self.booktitle_var.set("Machine Learning")  
                    self.auther_var.set("Drew Conway and John Myles White")  

                    d1 = datetime.datetime.today()
                    d2 = datetime.timedelta(days=15)
                    d3 = d1 + d2
                    self.dateborrowed_var.set(d1)
                    self.datedue_var.set(d3)
                    self.daysonbook.set(15)
                    self.lateratefine_var.set("₹195")
                    self.dateoverdue.set("NO")
                    self.finalprice.set("₹2798")
                
                else:
                    print("no")

                
        
        
        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",select_Book)
        listBox.grid(row=0,column=0,padx=4)
        listScroolbar.config(command=listBox.yview)
        
        for item in listBooks:
            listBox.insert(END,item)
            
        
        #***************BUTTON FRAME********************
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=530,width=1550,height=70)
        
        btnAddData=Button(Framebutton,command=self.add_data,text="ADD DATA",font=("arial",12,"bold"),width=23,bg="red",fg="white")
        btnAddData.grid(row=0,column=0)
        
        btnAddData=Button(Framebutton,command=self.showData,text="SHOW DATA",font=("arial",12,"bold"),width=23,bg="red",fg="white")
        btnAddData.grid(row=0,column=1)
        
        btnAddData=Button(Framebutton,command=self.update,text="UPDATE",font=("arial",12,"bold"),width=23,bg="red",fg="white")
        btnAddData.grid(row=0,column=2)
        
        btnAddData=Button(Framebutton,command=self.delete,text="DELETE",font=("arial",12,"bold"),width=23,bg="red",fg="white")
        btnAddData.grid(row=0,column=3)
        
        btnAddData=Button(Framebutton,command=self.reset,text="RESET",font=("arial",12,"bold"),width=23,bg="red",fg="white")
        btnAddData.grid(row=0,column=4)
        
        btnAddData=Button(Framebutton,command=self.iExit,text="EXIT",font=("arial",12,"bold"),width=23,bg="red",fg="white")
        btnAddData.grid(row=0,column=5) 
        
        #***************INFORMATION FRAME********************
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="cyan")
        FrameDetails.place(x=0,y=600,width=1530,height=195)
        
        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1470,height=170)
        
        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","title","firstname","lastname",
                                                            "address1","address2","postid","mobile","bookid",
                                                            "booktitle","auther","dateborrowed","datedue","days",
                                                            "latereturnfine","dateoverdue","finalprice"),
                                                             xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        
        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PNR No.")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address1",text="Address1")
        self.library_table.heading("address2",text="Address2")
        self.library_table.heading("postid",text="Post ID:")
        self.library_table.heading("mobile",text="Mobile Number")
        self.library_table.heading("bookid",text="Book ID:")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("auther",text="Auther")
        self.library_table.heading("dateborrowed",text="Date Of Borrowed")
        self.library_table.heading("datedue",text="Date Due")
        self.library_table.heading("days",text="Days On Book")
        self.library_table.heading("latereturnfine",text="Late Return Fine")
        self.library_table.heading("dateoverdue",text="Date Over Due")
        self.library_table.heading("finalprice",text="Final Price")
        
        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)
        
        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("auther",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)
        
        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        
        
    def add_data(self):
        if (not self.member_var.get() or not self.prn_var.get() or not self.id_var.get() or
                not self.firstname_var.get() or not self.lastname_var.get() or not self.address1_var.get() or
                not self.postcode_var.get() or not self.mobile_var.get() or not self.bookid_var.get() or
                not self.booktitle_var.get() or not self.auther_var.get() or not self.dateborrowed_var.get() or
                not self.datedue_var.get() or not self.daysonbook.get() or not self.lateratefine_var.get() or
                not self.dateoverdue.get() or not self.finalprice.get()):
            messagebox.showerror("Error", "All fields are mandatory")
            return
        
        id_no = self.id_var.get()
        if not re.match("^[0-9]{5}", id_no):
            messagebox.showerror("Error","ID should be 5-digit or 6-digit")
            return

            
        if not re.match("^[a-zA-Z]*$", self.firstname_var.get()):
            messagebox.showerror("Error", "Please enter a valid first name (only letters allowed)")
            return
        if not re.match("^[a-zA-Z]*$", self.lastname_var.get()):
            messagebox.showerror("Error", "Please enter a valid last name (only letters allowed)")
            return
        
        pin_code = self.postcode_var.get()
        if not re.match("^[0-9]{6}$", pin_code):
            messagebox.showerror("Error", "Please enter a 6-digit pin code")
            return

        
        mobile_number = self.mobile_var.get()
        if not re.match("^[0-9]{10}$", mobile_number):
            messagebox.showerror("Error", "Please enter a 10-digit mobile number")
            return
        
        
        
        conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM library WHERE ID = %s", (self.id_var.get(),))
        rows = my_cursor.fetchall()
        if rows:
            messagebox.showerror("Error", "ID number already exists")
            conn.close()
            return
        my_cursor.execute("INSERT INTO library VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                 self.member_var.get(),
                                                                                                                 self.prn_var.get(),
                                                                                                                 self.id_var.get(),
                                                                                                                 self.firstname_var.get(),
                                                                                                                 self.lastname_var.get(),
                                                                                                                 self.address1_var.get(),
                                                                                                                 self.address2_var.get(),
                                                                                                                 self.postcode_var.get(),
                                                                                                                 self.mobile_var.get(),
                                                                                                                 self.bookid_var.get(),
                                                                                                                 self.booktitle_var.get(),
                                                                                                                 self.auther_var.get(),
                                                                                                                 self.dateborrowed_var.get(),
                                                                                                                 self.datedue_var.get(),
                                                                                                                 self.daysonbook.get(),
                                                                                                                 self.lateratefine_var.get(),
                                                                                                                 self.dateoverdue.get(),
                                                                                                                 self.finalprice.get()
                                                                                                            ))
        
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success","Member Has Been inserted sucessfully")
        
        
    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set Member=%s,ID=%s,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,PostId=%s,Mobile=%s,Bookid=%s,BookTitle=%s,Auther=%s,DateOfBorrowed=%s,DateDue=%s,DaysOnBook=%s,LateReturnFine=%s,DateOverDue=%s,FinalPrice=%s where PRN_NO=%s",(
            
                                                                                                                 self.member_var.get(),
                                                                                                                 
                                                                                                                 self.id_var.get(),
                                                                                                                 self.firstname_var.get(),
                                                                                                                 self.lastname_var.get(),
                                                                                                                 self.address1_var.get(),
                                                                                                                 self.address2_var.get(),
                                                                                                                 self.postcode_var.get(),
                                                                                                                 self.mobile_var.get(),
                                                                                                                 self.bookid_var.get(),
                                                                                                                 self.booktitle_var.get(),
                                                                                                                 self.auther_var.get(),
                                                                                                                 self.dateborrowed_var.get(),
                                                                                                                 self.datedue_var.get(),
                                                                                                                 self.daysonbook.get(),
                                                                                                                 self.lateratefine_var.get(),
                                                                                                                 self.dateoverdue.get(),
                                                                                                                 self.finalprice.get(),
                                                                                                                 self.prn_var.get()
                                                                                                                 
                                                                                        ))
        
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()
        
        messagebox.showinfo("Sucess","Member Has been Updated")
        
        
        
        
        
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.auther_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook.set(row[14]),
        self.lateratefine_var.set(row[15]),
        self.dateoverdue.set(row[16]),
        self.finalprice.set(row[17])
        
    def showData(self):
        self.txtBox.insert(END,"Member Type\t\t"+self.member_var.get()+ "\n")
        self.txtBox.insert(END,"PRN No:\t\t"+self.prn_var.get()+ "\n")
        self.txtBox.insert(END,"ID No:\t\t"+self.id_var.get()+ "\n")
        self.txtBox.insert(END,"FirstName\t\t"+self.firstname_var.get()+ "\n")
        self.txtBox.insert(END,"LastName\t\t"+self.lastname_var.get()+ "\n")
        self.txtBox.insert(END,"Address1\t\t"+self.address1_var.get()+ "\n")
        self.txtBox.insert(END,"Address2\t\t"+self.address2_var.get()+ "\n")
        self.txtBox.insert(END,"Post Code\t\t"+self.postcode_var.get()+ "\n")
        self.txtBox.insert(END,"Mobile No:\t\t"+self.mobile_var.get()+ "\n")
        self.txtBox.insert(END,"Book ID:\t\t"+self.bookid_var.get()+ "\n")
        self.txtBox.insert(END,"Book Title\t\t"+self.booktitle_var.get()+ "\n")
        self.txtBox.insert(END,"Auther\t\t"+self.auther_var.get()+ "\n")
        self.txtBox.insert(END,"DateBorrowed:\t\t"+self.dateborrowed_var.get()+ "\n")
        self.txtBox.insert(END,"DateDue\t\t"+self.datedue_var.get()+ "\n")
        self.txtBox.insert(END,"DaysOnBook\t\t"+self.daysonbook.get()+ "\n")
        self.txtBox.insert(END,"LateRateFine\t\t"+self.lateratefine_var.get()+ "\n")
        self.txtBox.insert(END,"DateOverDue\t\t"+self.dateoverdue.get()+ "\n")
        self.txtBox.insert(END,"FinalPrice\t\t"+self.finalprice.get()+ "\n")
        
    def reset(self):
        self.member_var.set("")
        self.prn_var.set("")
        self.id_var.set(""),
        self.firstname_var.set("")
        self.lastname_var.set("")
        self.address1_var.set("")
        self.address2_var.set("")
        self.postcode_var.set("")
        self.mobile_var.set("")
        self.bookid_var.set("")
        self.booktitle_var.set("")
        self.auther_var.set("")
        self.dateborrowed_var.set("")
        self.datedue_var.set("")
        self.daysonbook.set("")
        self.lateratefine_var.set("")
        self.dateoverdue.set("")
        self.finalprice.set("")
        self.txtBox.delete("1.0",END)
        
    def iExit(self):
        iExit=messagebox.askyesno("Library management System","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return
        
    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First Select the member")
        else:
             conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="mydata")
             my_cursor=conn.cursor()
             query="DELETE FROM library WHERE PRN_NO=%s"
             value=(self.prn_var.get(),)
             my_cursor.execute(query,value)

             
             conn.commit()
             self.fetch_data()
             self.reset()
             conn.close()
             
             messagebox.showinfo("Sucess","Member has been deleted")
if __name__=="__main__":
    main()
            
        
        


        
        

        


        
        
        
        
        
        
        
        
        
        
        
        
        
        
