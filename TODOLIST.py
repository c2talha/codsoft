from tkinter import *
from tkinter import messagebox, simpledialog
import datetime

root = Tk()
root.title("To-Do List")
root.geometry("500x600")
root.config(bg="white")
root.resizable(False, False)

def add_item_with_datetime():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    item_text = entry.get()
    item_with_time = f"{current_time} - {item_text}"

    due_date = ask_due_date(item_text)
    if due_date:
        item_with_time += f" (Due: {due_date})"

    listbox.insert(END, item_with_time)
    entry.delete(0, END)

def ask_due_date(item_text):
    due_date = simpledialog.askstring("Input", f"Enter due date for '{item_text}' (YYYY-MM-DD HH:MM:SS):", parent=root)
    return due_date

def remove_item():
    listbox.delete(ANCHOR)

def clear_all():
    listbox.delete(0, END)

def save_all():
    try:
        with open("todolist.txt", "w") as f:
            list_tuple = listbox.get(0, END)
            for item in list_tuple:
                if item.endswith("\n"):
                    f.write(item)
                else:
                    f.write(item + "\n")
    except Exception as e:
        messagebox.showerror("Error", f"Error occurred: {e}")

def open_all():
    try:
        with open("todolist.txt", "r") as f:
            for line in f:
                listbox.insert(END, line)
    except FileNotFoundError:
        messagebox.showinfo("File Not Found", "No existing To-Do list found.")
    except Exception as e:
        messagebox.showerror("Error", f"Error occurred: {e}")

def exit_app():
    root.destroy()

def about():
    messagebox.showinfo("About", "This is a To-Do List application created by Muhammad Talha.")

my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Add Item", command=add_item_with_datetime)
file_menu.add_command(label="Remove Item", command=remove_item)
file_menu.add_command(label="Clear All", command=clear_all)
file_menu.add_command(label="Save All", command=save_all)
file_menu.add_command(label="Open All", command=open_all)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

help_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

listbox = Listbox(root, width=40, height=10, bg="black", fg="white", font=("Arial", 16), bd=0, highlightthickness=0)
listbox.pack(pady=10)

entry = Entry(root, font=("Arial", 20), width=24)
entry.pack(pady=10)

add_datetime_button = Button(root, text="Add Item with Date & Time", font=("Arial", 14), command=add_item_with_datetime)
add_datetime_button.pack(pady=10)

def update_time_date():
    now = datetime.datetime.now()
    formatted_date = now.strftime("%A, %B %d, %Y")
    formatted_time = now.strftime("%I:%M:%S %p")
    time_date_label.config(text=f"Today's Date: {formatted_date}\nCurrent Time: {formatted_time}")
    root.after(1000, update_time_date)

time_date_label = Label(root, text="", font=("Arial", 12), bg="white")
time_date_label.pack(pady=10)

update_time_date()

root.mainloop()