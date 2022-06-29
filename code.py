from fnmatch import translate
from re import L
from tkinter import *
from turtle import right
from googletrans import Translator
from matplotlib import image
from matplotlib.pyplot import gray, grid, text
from pyparsing import anyCloseTag
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import pytesseract as pyt
import cv2
import matplotlib.pyplot as plt
from PIL import *
from PIL import Image , ImageTk
import smtplib

my_email = "tr4ns1atordm@gmail.com"
password = "Translate123"


pyt.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'



def transl (): 
    text = abc.get(1.0 , END)
    a = translator.translate(text, dest='en')
    bca.delete(1.0 , END)
    bca.insert(1.0,a.text)

def openfile():
    path = askopenfilename()
    image =Image.open(path)
    img=ImageTk.PhotoImage(image)
    view.create_image(5,10, image=img, anchor=NW)
    string = pyt.image_to_string(image)
    res = translator.translate(string, dest = 'ru')
    cda.delete(1.0 , END)
    cda.insert(1.0, res.text)
    messagebox.showinfo("all nice", "Translated")

def opentext():
    path = askopenfilename()
    f = open(path,'r')
    text1 = f.read()
    kda1.delete(1.0 , END)
    kda1.insert(1.0,text1)
    transa = translator.translate(text1, dest = 'ru')
    kda.delete(1.0 , END)
    kda.insert(1.0,transa.text)
    messagebox.showinfo("all nice", "Translated")

 
def sender ():
    email = entr.get()
    message = sts.get(1.0 , END)
    em="tr4ns1atordm@gmail.com"
    pw= "mhighpacfkynxbvv"
    connection = smtplib.SMTP("smtp.gmail.com",587)
    connection.starttls()
    connection.login(user=em , password = pw)
    connection.sendmail(from_addr = em , to_addrs = email , msg=message)
    connection.close()
    messagebox.showinfo("all nice", "Message sented")

def tab1_go():
    text=bca.get(1.0 , END)
    sts.insert(1.0,text)
    messagebox.showinfo("all nice", "Сообщение скопировано в другое окно")


def save1():
    f = open("text.txt", "w+")
    message = bca.get(1.0 , END)
    f.write(message)
    f.close()
    messagebox.showinfo("all nice", "SAVED")

def save2():
    f = open("text.txt", "w+")
    message = cda.get(1.0 , END)
    f.write(message)
    f.close()
    messagebox.showinfo("all nice", "SAVED")

def save3():
    f = open("text.txt", "w+")
    message = kda.get(1.0 , END)
    f.write(message)
    f.close()
    messagebox.showinfo("all nice", "SAVED")


def save4():
    f = open("text.txt", "w+")
    message = sts.get(1.0 , END)
    f.write(message)
    f.close()
    messagebox.showinfo("all nice", "SAVED")

window = Tk()
tab_control = ttk.Notebook(window)

window.title("Переводчик")

window.geometry('500x500')

translator = Translator()


tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control) 
tab4 = ttk.Frame(tab_control) 

tab_control.add(tab1, text='Перевод текста')
tab_control.add(tab2, text='Фотоперевод') 
tab_control.add(tab3, text='Перевод текстовых документов') 
tab_control.add(tab4, text='Поделиться')


    

lbl = Label (tab1, text="Русский")

btn = Button(tab1, text = "перевести" , command = transl)

button1 = Button(tab1,text="Поделиться" , command= tab1_go)

lbl1 = Label (tab1, text= "Английский") 

button2_tab1 = Button(tab1 , text = "Сохранить" , command = save1)
button2_tab1.place(relx=0.3 , y= 500 , anchor = CENTER)

abc = scrolledtext.ScrolledText(tab1)  
bca = scrolledtext.ScrolledText(tab1)  

lbl.place(relx=0.2 , y = 30 , anchor=CENTER)
lbl1.place(relx=0.8 , y=30 , anchor=CENTER)
btn.place(relx=0.5 , y = 300 , anchor=CENTER)
button1.place(relx=0.7 , y = 500 , anchor=CENTER)


abc.place( height = 300 , width=600, relx=0.2 , y=230 , anchor= CENTER  )  
bca.place(height = 300 , width= 600 ,relx=0.8 , y = 230 , anchor= CENTER )  




button_tab2 = Button(tab2 , text = "Загрузить файл" , command = openfile)



button_tab2.place(relx=0.1 , y= 40 , anchor = CENTER)


button3_tab2 = Button(tab2 , text = "Сохранить" , command = save2)
button3_tab2.place(relx=0.3 , y= 500 , anchor = CENTER)

cda = scrolledtext.ScrolledText(tab2)
cda.place( height = 300 , width=600, relx=0.7 , y=230 , anchor= CENTER  )  

view = Canvas(tab2)
view.place( width=600, height=300,relx=0.1,y = 90 )



kda1 = scrolledtext.ScrolledText(tab3)
kda1.place( height = 300 , width=600, relx=0.3 , y=230 , anchor= CENTER  ) 

kda = scrolledtext.ScrolledText(tab3)
kda.place( height = 300 , width=600, relx=0.7 , y=230 , anchor= CENTER  ) 


button_tab3 = Button(tab3 , text = "Открыть текстовый файл" , command = opentext)
button_tab3.place(relx=0.5 , y= 300 , anchor = CENTER)



button2_tab3 = Button(tab3 , text = "Сохранить" , command = save3)
button2_tab3.place(relx=0.3 , y= 500 , anchor = CENTER)



lbl_tab4 = Label (tab4, text= "Введите адрес получателя") 

lbl_tab4.place(relx=0.2 , y=30 , anchor=CENTER)


entr = Entry(tab4)
entr.place( height = 60 , width=200, relx=0.2 , y=130 , anchor= CENTER  )  


lbl2_tab4 = Label (tab4, text= "Введите сообщение") 

lbl2_tab4.place(relx=0.7 , y= 150, anchor=CENTER)

sts = scrolledtext.ScrolledText(tab4)
sts.place( height = 200 , width=500, relx=0.7 , y=300 , anchor= CENTER  )  



button_tab4 = Button(tab4 , text = "Отправить сообщение" , command = sender)
button2_tab4 = Button(tab4 , text = "Сохранить" , command = save4)
button2_tab4.place(relx=0.3 , y= 500 , anchor = CENTER)
button_tab4.place(relx=0.7 , y= 500 , anchor = CENTER)



tab_control.pack(expand=1, fill='both') 
window.mainloop()