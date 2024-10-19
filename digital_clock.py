import tkinter as tk
from time import strftime
root=tk.Tk()
root.title("Digital Clock")
def time():
    time_string=strftime('%H:%M: %S  %p \n %D')
    label.config(text=time_string)
    label.after(1000,time)
    
label=tk.Label(root,font=('calibri',70,'bold'),background='black',foreground='red')
label.pack(anchor='center')
time()
root.mainloop()