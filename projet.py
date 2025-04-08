import tkinter as tk
import webbrowser

def my_link():
    link = mytext.get()
    webbrowser.open(link)

myframe = tk.Tk()
myframe.title("Web browser")
myframe.resizable(width=False,height=False)
myframe.geometry("500x300")

mylabel = tk.Label(myframe, text="Web browser", font="tahoma 20 bold")
mylabel.pack(pady=15)

mylabel = tk.Label(myframe, text="Write a link (exemple: www.google.com):", font="tahoma 10 bold")
mylabel.pack(pady=5)

mytext= tk.Entry(myframe, width=50)
mytext.pack(pady=10)


mybtn = tk.Button(myframe, text="Go to link", fg="white", bg="#0cab1e", font="Helvatica 10 bold", padx=7, pady=3, command=my_link )
mybtn.pack()


myframe.mainloop()