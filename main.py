#imports
import pyperclip
import pyshorteners
from tkinter import *

canvas = Tk()
canvas.geometry ("500x600")
canvas.title("URL Shortener")
canvas.configure (bg="#49A")
url = StringVar()
url_address = StringVar()

#URL shortener
def urlshort():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)

#copying the url
def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)
#GUI
enter_your_url = Label(canvas, text = "Enter your url", font = "poppins")
enter_your_url.pack(pady=10)
url = Entry(canvas, textvariable=url, font="poppins")
url.pack()
button1 = Button(text = "Generate short url", command = urlshort)
button1.pack(pady=7)
textfield = Entry(textvariable = url_address).pack(pady=5)

button2 = Button(text ="Copy URL", command = copyurl)
button2.pack(pady=5)




canvas.mainloop()

