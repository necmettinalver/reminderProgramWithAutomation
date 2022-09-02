#!/usr/bin/env python
# coding: utf-8

# In[79]:


from tkinter import *
from tkcalendar import DateEntry
from tkinter import messagebox
from email.message import EmailMessage
import ssl
import smtplib
import os

email_sender = 'Your-Email@gmail.com'
email_password = 'Your-password'

def send():
    last_message=''
    try:
        if var.get():
            #if len(reminder_option.get())==1:
                #typeR='General'
            #else:
                #typeR=reminder_option.get()
            typeR=reminder_option.get() if not(len(reminder_option.get())==1) else 'General'
            date=reminder_date_entry.get()
            message=text_field.get('1.0','end')
            
            if var.get()==1:
                last_message+='Your data has been successfully saved to the system.'

                with open('Reminder.txt','w') as txt:
                    txt.write('{} in the category, {} to history ve "{}" reminder with note'.format(
                    typeR,date,message))
                    txt.close()

            elif var.get()==2:
                last_message+='Your data will be sent to you via E-mail.'
                if (var1.get()==1 or var2.get()==1 or var3.get()==1):
                    print(os.path.dirname(os.path.abspath(__file__)))
                    path_py=os.path.dirname(os.path.abspath(__file__))
                    path_bat=path_py + "\\automation.txt"
                    os.startfile(path_bat)

                else:
                    em=EmailMessage()
                    em['From']=email_sender
                    em['To']=email_sender
                    em['subject']=typeR
                    em.set_content('{} in the category, {} to history ve "{}" reminder with note'.format(
                        typeR,date,message))

                    context = ssl.create_default_context()
                    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
                        smtp.login(email_sender,email_password)
                        smtp.sendmail(email_sender,email_sender,em.as_string())
                    
            messagebox.showinfo("Successful process",last_message)
        else:
            last_message='Make sure the required fields are filled!'
            messagebox.showwarning("Failed process.",last_message)
    except:
            last_message='Error found!'
            messagebox.showerror("Failed process.",last_message)
    finally:
        master.destroy()

master = Tk()
canvas = Canvas(master,height=450,width=750)
canvas.pack()

#creating fields
frame_top=Frame(master,bg='#2a333c')
frame_top.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.18)

frame_left=Frame(master,bg='#2a333c')
frame_left.place(relx=0.01,rely=0.20,relwidth=0.36,relheight=0.78)

frame_right=Frame(master,bg='#2a333c')
frame_right.place(relx=0.38,rely=0.20,relwidth=0.61,relheight=0.78)

#created reminder type mesage label
reminder_label= Label(frame_top,bg='#2a333c',fg='white',text='Reminder Type:',font='Verdana 12 bold')
reminder_label.pack(padx=10,pady=10,side=LEFT)

#reminder type selection field created
reminder_option=StringVar(frame_top)
reminder_option.set("\t")
reminder_dropdown_menu=OptionMenu(frame_top,
                                  reminder_option,
                                 'Birthday',
                                  'Shopping',
                                  'Salary')
reminder_dropdown_menu.pack(padx=10,pady=10,side=LEFT)

#date field created
reminder_date_entry = DateEntry(frame_top,width=12,background='purple',foreground='white',borderwidth=1,locale='de_DE')
reminder_date_entry._top_cal.overrideredirect(False)
reminder_date_entry.pack(padx=10,pady=10,side=RIGHT)

#date mesage label created
reminder_date_label= Label(frame_top,bg='#2a333c',fg='white',text='Reminder date:',font='Verdana 12 bold')
reminder_date_label.pack(padx=10,pady=10,side=RIGHT)

#
Label(frame_left,bg='#2a333c',fg='white',text='Hatırlatma Yöntemi',font='Verdana 12 bold').pack(padx=10,pady=10,anchor=NW)

#
var=IntVar()
R1=Radiobutton(frame_left,text='Save to System',variable=var,value=1,bg='#2a333c',fg='white',selectcolor='#1d2126',font='Verdana 12 bold')
R1.pack(anchor=NW,pady=5,padx=15)

R2=Radiobutton(frame_left,text='Send to E-mail',variable=var,value=2,bg='#2a333c',fg='white',selectcolor='#1d2126',font='Verdana 12 bold')
R2.pack(anchor=NW,pady=5,padx=15)

#
var1=IntVar()
C1=Checkbutton(frame_left,text='Bir hafta önce',variable=var1,onvalue=1,offvalue=0,bg='#2a333c',selectcolor='#1d2126',fg='white',font='Verdana 12 bold')
C1.pack(anchor=NW,pady=5,padx=25)

var2=IntVar()
C2=Checkbutton(frame_left,text='A week ago',variable=var2,onvalue=1,offvalue=0,bg='#2a333c',selectcolor='#1d2126',fg='white',font='Verdana 12 bold')
C2.pack(anchor=NW,pady=5,padx=25)

var3=IntVar()
C3=Checkbutton(frame_left,text='The Same Day',variable=var3,onvalue=1,offvalue=0,bg='#2a333c',selectcolor='#1d2126',fg='white',font='Verdana 12 bold')
C3.pack(anchor=NW,pady=5,padx=25)

#
Label(frame_right,bg='#2a333c',fg='white',text='Reminder message',font='Verdana 12 bold').pack(padx=10,pady=10,anchor=NW)
text_field = Text(frame_right,height=16,width=50)
text_field.tag_configure('style',foreground='#2a333c',font=('Verdana',7,'bold'))
text_field.pack()

first_text='Write there...'
text_field.insert(END,first_text,'style')

#
send_button=Button(frame_right,text='Send',command=send)
send_button.pack(anchor=S,pady=5,padx=25)


#for continuous operation of the screen.
master.mainloop()


# In[ ]:




