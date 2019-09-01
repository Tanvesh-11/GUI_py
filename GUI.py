# Tanvesh Bhattad
from Tkinter import *
import smtplib
from email.MIMEImage import MIMEImage
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import encoders
import imghdr
import os
from subprocess import *
from PIL import ImageTk
from PIL import Image
import cv2
import subprocess
root=Tk()
root.title("BMI Measurement System")
send_email='eh.feedbacksystem@gmail.com'
send_pass='endress123'
v=StringVar()
#e=Text(root, width=28, height=1, font="Times 20")
#e.grid(row=1, column=1)
entry_widget = Entry(root)
entry_widget.grid(row=1, column=1)
v=entry_widget.get()
msg = MIMEMultipart()
#msg='/home/pi/testpic.png'
#msg='testpic.png'
img=ImageTk.PhotoImage(Image.open("companylogo.png"))
panel=Label(root,image=img)
panel.grid(row=1,column=0)
camera=Frame(root)
bmitest=Frame(root)
def func():
    proc = Popen("two.py", stdout=PIPE, shell=True)
    proc = proc.communicate()
    top.insert(END, proc)
top = Text(bmitest, width=38, height=10, font=("Courier", 16))
bottom = Button(root, text="CALCULATE YOUR BMI", font=("Times",13,"bold"),bg="blue",fg="white", command=func)
btn= Button(root, text="CLEAR SCREEN", font=("Times",13,"bold"),bg="blue",fg="white", command=lambda: top.delete(1.0,END))
top.grid(row=0,column=1)
bottom.grid(row=3,column=1)
btn.grid(row=3,column=0)
cap = cv2.VideoCapture(0)
cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 422)
cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 412)
cv2.namedWindow('cam', cv2.cv.CV_WINDOW_AUTOSIZE)
lmain = Label(camera)
lmain.pack()
def showframe():
    _,frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(1, showframe)
showframe()
camera.grid(row=2,column=0)
bmitest.grid(row=2,column=1)
def printtest():
    screenshot = "/home/pi/testpic.png"
    subprocess.call(["scrot","-d", "1", screenshot])
    #subprocess.call(["lp", "-d","Canon_CP1000", "testpic.png"])
pnt=Button(root, text="PRINT",font=("Times",13,"bold"),bg="blue",fg="white", command=printtest)
pnt.grid(row=0, column=0)
e=Label(root, text="Enter Your Name:", anchor="w", font="Times 18",bg="blue",fg="white")
e.grid(row=4, column=4)
root.configure(background="white")
def get_users_data(filename):
    user_email = [" "]
    with open(filename,'r') as user_file:
        user_email=user_file.read()
    return user_email
def mail():
    try:
        v= entry_widget.get()
        print("v")
        print(v)
        with open('/home/pi/testpic.png', 'rb') as f:
                        #mime.add_header('X-Attachment-Id','0')
                #mime.add_header('Content-ID','<0>')
            mime = MIMEBase('image', 'png', filename='testpic.png')
            mime.set_payload(f.read())
            f.close()
            mime.add_header('Content-Disposition', 'attachment', filename='testpic.png')
            encoders.encode_base64(mime)
            msg.attach(mime)
            server=smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(send_email, send_pass)
            server.sendmail(send_email,v,msg.as_string())
            server.close()
            entry_widget.delete(0, 'end')
    except Exception as e:
        print(e)
            #a=messagebox.askokcancel("Error","Read instructions")
#action_button = Button(root)
#action_button.configure(text='send mail',command=mail)
#action_button.grid(row=0,column=2)
mailbtn=Button(root, text="SendMail",font=("Times",13,"bold"),bg="blue",fg="white", command=mail)
mailbtn.grid(row=0,column=1)

root.mainloop()
