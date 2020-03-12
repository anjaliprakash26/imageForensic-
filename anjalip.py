from tkinter import *
from PIL import Image
from PIL.ExifTags import TAGS
import random
import time
from tkinter import messagebox

#-------------------Top Window----------------------------------------------------------------------------------------------------
 
root1 =Tk()
root1.geometry("900x600+0+0")
root1.title("Image Forensic")
root1.configure(bg="#D3D3D3") 

Tops = Frame(root1,bg="white",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)

lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="IMAGE FORENSIC APPLICATION",fg="Black",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)
 
localtime=time.asctime(time.localtime(time.time()))

lblinfo = Label(Tops, font=( 'aria' ,30, ),text=localtime,fg="steel blue",anchor=W)
lblinfo.grid(row=4,column=0)

button1 = Button(root1, padx=16,pady=8, bd=10 ,font=('ariel' ,16,'bold'),width=10, text="       EXIT", bg="red",command=root1.destroy,anchor=W)
button1.pack()

 
#---------------------Top Window Closed------------------------------------------------------------------------------------------

#--------------------working window-----------------------------------------------------------------------------------------------


def window():
    top=Toplevel()
    top.geometry("890x580+0+0")
    top.title("metadata")
    top.config(bg="#D3D3D3")
    top.resizable(0,0)
    Tops = Frame(top,bg="white",width = 1600,height=50,relief=SUNKEN)
    Tops.pack()

    #roo.mainloop()

    f1 = Frame(top,width = 900,height=700,relief=SUNKEN)
    f1.pack(side=LEFT)
 

    localtime=time.asctime(time.localtime(time.time())) 
    lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="META DATA FINDER",fg="#000080",bd=15,anchor='w')
    lblinfo.grid(row=0,column=0)
    lblinfo = Label(Tops, font=( 'aria' ,20, ),text=localtime,fg="steel blue",anchor=W)
    lblinfo.grid(row=1,column=0)


 
    def qexit():
        root.destroy()
 
        btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="red",command=qexit)
        btnexit.grid(row=9, column=2)



    def get_exif(fn):
        ret ={}
        i = Image.open(fn)
        info = i._getexif()
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            ret[decoded] = value 
        return ret


    def image():
    
        fie=(get_exif("C:/Users/USER/Desktop/Project/PGDCSL.jpg"))
        msg=messagebox.showinfo("Sucess Image Meta Data",fie)
        #print(fie)
        #roo = Tk()
        #roo.geometry("600x220+0+0")
        #roo.title("MetaData")
     
        #roo.mainloop()

    def audio():
        roo = Tk()
        roo.geometry("600x220+0+0")
        roo.title("Audio MetaData")
     
        #roo.mainloop()

    def video():
        roo = Tk()
        roo.geometry("600x220+0+0")
        roo.title("Video MetaData")
        #roo.mainloop()
        #roo.mainloop()
    btnimage=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="IMAGE", bg="blue",command=image)
    btnimage.grid(row=8, column=2)
    btnimage.pack()
    btnaudio=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="AUDIO", bg="green",command=audio)
    #btnaudio.grid(row=7, column=2)
    btnaudio.pack()
    btnvideo=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="VIDEO", bg="purple",command=video)
    #btnvideo.grid(row=6, column=2)
    btnvideo.pack()
    root1.mainloop()

    
button = Button(root1, padx=16, pady=8, bd=10, font=('aria', 16,'bold'),width=10, fg="black",bg="green",text="     START",anchor=W,command=window)
button.pack()
root1.mainloop()
 


