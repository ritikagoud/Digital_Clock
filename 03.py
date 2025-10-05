import tkinter as tk
import time

root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x200")
root.resizable(False, False)


def time_date():
    current_time = time.strftime("%H:%M:%S %p")  
    current_date = time.strftime("%A, %d %B %Y")  
    
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    
    
    time_label.after(1000, time_date)

time_label = tk.Label(root, font=("Helvetica", 48, "bold"), bg="purple", fg="yellow")
time_label.pack(pady=10)


date_label = tk.Label(root, font=("Helvetica", 20, "italic"), bg="purple", fg="yellow")
date_label.pack()

time_date()
root.mainloop()
