from tkinter import *
import speedtest

def speedcheck():
    root=speedtest.Speedtest()
    root.get_servers()
    down=str(round(root.download()/(10**6),3))+'mbps'
    up=str(round(root.download()/(10**6),3))+'mbps'
    label_down.config(text=down)
    label_up.config(text=up)
root=Tk()
root.title('internet speed test')
root.geometry('500x400')
root.config(bg='yellow')

label=Label(root,text='Internet Speed Test',font=('Time New Roman',20,'bold'),bg='yellow')
label.place(x=130,y=10)

label=Label(root,text='download speed',font=('Time New Roman',20,'bold'),bg='yellow')
label.place(x=140,y=70)
label_down=Label(root,text='00',font=('Time New Roman',20,'bold'),bg='yellow')
label_down.place(x=200,y=110)
label=Label(root,text='upload speed',font=('Time New Roman',20,'bold'),bg='yellow')
label.place(x=150,y=160)
label_up=Label(root,text='00',font=('Time New Roman',20,'bold'),bg='yellow')
label_up.place(x=200,y=200)

button=Button(root,text='check speed',font=('Time New Roman',10,'bold'),relief=RAISED,bg='red',command=speedcheck)
button.place(x=180,y=240)

root.mainloop()