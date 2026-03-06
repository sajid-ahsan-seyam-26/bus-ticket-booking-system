import tkinter as tk
from tkinter import ttk, messagebox

# price per seat
PRICE = 500

def book_ticket():
    name = name_entry.get()
    source = source_box.get()
    destination = dest_box.get()
    seats = seat_entry.get()

    if name == "" or seats == "":
        messagebox.showerror("Error", "Please fill all fields")
        return

    total = int(seats) * PRICE

    receipt = f"""
    -------- Bus Ticket --------
    Passenger : {name}
    From      : {source}
    To        : {destination}
    Seats     : {seats}
    Price/Seat: {PRICE} BDT
    ----------------------------
    Total     : {total} BDT
    ----------------------------
    """

    receipt_box.delete(1.0, tk.END)
    receipt_box.insert(tk.END, receipt)


# main window
root = tk.Tk()
root.title("Bus Ticket Booking System")
root.geometry("500x500")

title = tk.Label(root, text="Bus Ticket Booking System", font=("Arial",18,"bold"))
title.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Passenger Name").grid(row=0,column=0,padx=10,pady=5)
name_entry = tk.Entry(frame)
name_entry.grid(row=0,column=1)


tk.Label(frame, text="From").grid(row=1,column=0,padx=10,pady=5)
source_box = ttk.Combobox(frame, values=["Dhaka","Mymensingh","Chittagong","Sylhet"])
source_box.grid(row=1,column=1)
source_box.current(0)


tk.Label(frame, text="To").grid(row=2,column=0,padx=10,pady=5)
dest_box = ttk.Combobox(frame, values=["Dhaka","Mymensingh","Chittagong","Sylhet"])
dest_box.grid(row=2,column=1)
dest_box.current(1)


tk.Label(frame, text="Number of Seats").grid(row=3,column=0,padx=10,pady=5)
seat_entry = tk.Entry(frame)
seat_entry.grid(row=3,column=1)

# button
book_btn = tk.Button(root,text="Book Ticket",command=book_ticket,bg="green",fg="white",font=("Arial",12))
book_btn.pack(pady=10)

# receipt
tk.Label(root,text="Ticket Receipt",font=("Arial",14)).pack()

receipt_box = tk.Text(root,height=12,width=50)
receipt_box.pack()

root.mainloop()
