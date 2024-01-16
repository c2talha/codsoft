from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import pickle
import os

def save_contacts(contacts):
    with open("contacts.pickle", "wb") as file:
        pickle.dump(contacts, file)

def load_contacts():
    if os.path.exists("contacts.pickle"):
        with open("contacts.pickle", "rb") as file:
            contacts = pickle.load(file)
        return contacts
    return []

def add_contact():
    def save_contact():
        name = name_var.get()
        phone = phone_var.get()
        email = email_var.get()
        address = address_var.get()

        if name and phone and email and address:
            contact = {
                "name": name,
                "phone": phone,
                "email": email,
                "address": address
            }

            contacts = load_contacts()
            contacts.append(contact)

            save_contacts(contacts)

            messagebox.showinfo("Success", "Contact has been saved successfully.")
            add_contact_window.destroy()
        else:
            messagebox.showerror("Error", "All fields are required.")

    add_contact_window = Toplevel(root)
    add_contact_window.title("Add Contact")
    add_contact_window.geometry("500x600")
    add_contact_window.resizable(0, 0)
    add_contact_window.configure(bg="#3498db")  # Blue theme

    myFont = font.Font(family='Helvetica', size=16, weight='bold')

    name_label = Label(add_contact_window, text="Name:", fg="white", bg="#3498db", font=myFont)
    name_label.place(relx=0.5, rely=0.1, anchor=CENTER)

    name_var = StringVar()
    name_entry = Entry(add_contact_window, textvariable=name_var, font=myFont, bg="#2ecc71", fg="white", width=20)
    name_entry.place(relx=0.5, rely=0.2, anchor=CENTER)

    phone_label = Label(add_contact_window, text="Phone:", fg="white", bg="#3498db", font=myFont)
    phone_label.place(relx=0.5, rely=0.3, anchor=CENTER)

    phone_var = StringVar()
    phone_entry = Entry(add_contact_window, textvariable=phone_var, font=myFont, bg="#2ecc71", fg="white", width=20)
    phone_entry.place(relx=0.5, rely=0.4, anchor=CENTER)

    email_label = Label(add_contact_window, text="Email:", fg="white", bg="#3498db", font=myFont)
    email_label.place(relx=0.5, rely=0.5, anchor=CENTER)

    email_var = StringVar()
    email_entry = Entry(add_contact_window, textvariable=email_var, font=myFont, bg="#2ecc71", fg="white", width=20)
    email_entry.place(relx=0.5, rely=0.6, anchor=CENTER)

    address_label = Label(add_contact_window, text="Address:", fg="white", bg="#3498db", font=myFont)
    address_label.place(relx=0.5, rely=0.7, anchor=CENTER)

    address_var = StringVar()
    address_entry = Entry(add_contact_window, textvariable=address_var, font=myFont, bg="#2ecc71", fg="white", width=20)
    address_entry.place(relx=0.5, rely=0.8, anchor=CENTER)

    save_button = Button(add_contact_window, text="Save", bg="#2ecc71", fg="white", command=save_contact)
    save_button['font'] = myFont
    save_button.place(relx=0.5, rely=0.9, anchor=CENTER)

def view_contacts():
    view_contacts_window = Toplevel(root)
    view_contacts_window.title("View Contacts")
    view_contacts_window.geometry("500x600")
    view_contacts_window.resizable(0, 0)
    view_contacts_window.configure(bg="#3498db")  # Blue theme

    myFont = font.Font(family='Helvetica', size=16, weight='bold')

    contacts = load_contacts()

    if contacts:
        for index, contact in enumerate(contacts):
            name_label = Label(view_contacts_window, text=f"Name: {contact['name']}", fg="white", bg="#3498db", font=myFont)
            name_label.place(relx=0.5, rely=0.1 + (index * 0.1), anchor=CENTER)

            phone_label = Label(view_contacts_window, text=f"Phone: {contact['phone']}", fg="white", bg="#3498db", font=myFont)
            phone_label.place(relx=0.5, rely=0.15 + (index * 0.1), anchor=CENTER)

            email_label = Label(view_contacts_window, text=f"Email: {contact['email']}", fg="white", bg="#3498db", font=myFont)
            email_label.place(relx=0.5, rely=0.2 + (index * 0.1), anchor=CENTER)

            address_label = Label(view_contacts_window, text=f"Address: {contact['address']}", fg="white", bg="#3498db", font=myFont)
            address_label.place(relx=0.5, rely=0.25 + (index * 0.1), anchor=CENTER)
    else:
        no_contacts_label = Label(view_contacts_window, text="No contacts found.", fg="white", bg="#3498db", font=myFont)
        no_contacts_label.place(relx=0.5, rely=0.1, anchor=CENTER)
def search_contact():
    def search():
        contacts = load_contacts()

        for contact in contacts:
            if search_var.get() == contact['name'] or search_var.get() == contact['phone']:
                display_contact(contact)
                break
        else:
            display_no_contacts_error()

    def display_contact(contact):
        search_contact_window = Toplevel(root)
        search_contact_window.title("Search Contact")

        search_contact_window.geometry("500x600")
        search_contact_window.resizable(0, 0)
        search_contact_window.configure(bg="#3498db")  # Blue theme

        myFont = font.Font(family='Helvetica', size=16, weight='bold')

        name_label = Label(search_contact_window, text=f"Name: {contact['name']}", fg="white", bg="#3498db", font=myFont)
        name_label.place(relx=0.5, rely=0.1, anchor=CENTER)

        phone_label = Label(search_contact_window, text=f"Phone: {contact['phone']}", fg="white", bg="#3498db", font=myFont)
        phone_label.place(relx=0.5, rely=0.15, anchor=CENTER)

        email_label = Label(search_contact_window, text=f"Email: {contact['email']}", fg="white", bg="#3498db", font=myFont)
        email_label.place(relx=0.5, rely=0.2, anchor=CENTER)

        address_label = Label(search_contact_window, text=f"Address: {contact['address']}", fg="white", bg="#3498db", font=myFont)
        address_label.place(relx=0.5, rely=0.25, anchor=CENTER)

    def display_no_contacts_error():
        no_contacts_label = Label(search_contact_window, text="No contacts found.", fg="white", bg="#3498db", font=myFont)
        no_contacts_label.place(relx=0.5, rely=0.1, anchor=CENTER)

    search_contact_window = Toplevel(root)
    search_contact_window.title("Search Contact")

    search_contact_window.geometry("500x600")
    search_contact_window.resizable(0, 0)
    search_contact_window.configure(bg="#3498db")  # Blue theme

    myFont = font.Font(family='Helvetica', size=16, weight='bold')

    search_label = Label(search_contact_window, text="Search:", fg="white", bg="#3498db", font=myFont)
    search_label.place(relx=0.5, rely=0.1, anchor=CENTER)

    search_var = StringVar()
    search_entry = Entry(search_contact_window, textvariable=search_var, font=myFont, bg="#2ecc71", fg="white", width=20)
    search_entry.place(relx=0.5, rely=0.2, anchor=CENTER)

    search_button = Button(search_contact_window, text="Search", bg="#2ecc71", fg="white", command=search)
    search_button['font'] = myFont
    search_button.place(relx=0.5, rely=0.35, anchor=CENTER)

def update_contact():
    def search():
        contacts = load_contacts()

        for contact in contacts:
            if search_var.get() == contact['name'] or search_var.get() == contact['phone']:
                name_label = Label(update_contact_window, text="Name:", fg="white", bg="#3498db", font=myFont)
                name_label.place(relx=0.5, rely=0.1, anchor=CENTER)

                name_var.set(contact['name'])
                name_entry = Entry(update_contact_window, textvariable=name_var, font=myFont, bg="#2ecc71", fg="white", width=20)
                name_entry.place(relx=0.5, rely=0.2, anchor=CENTER)

                phone_label = Label(update_contact_window, text="Phone:", fg="white", bg="#3498db", font=myFont)
                phone_label.place(relx=0.5, rely=0.3, anchor=CENTER)

                phone_var.set(contact['phone'])
                phone_entry = Entry(update_contact_window, textvariable=phone_var, font=myFont, bg="#2ecc71", fg="white", width=20)
                phone_entry.place(relx=0.5, rely=0.4, anchor=CENTER)

                email_label = Label(update_contact_window, text="Email:", fg="white", bg="#3498db", font=myFont)
                email_label.place(relx=0.5, rely=0.5, anchor=CENTER)

                email_var.set(contact['email'])
                email_entry = Entry(update_contact_window, textvariable=email_var, font=myFont, bg="#2ecc71", fg="white", width=20)
                email_entry.place(relx=0.5, rely=0.6, anchor=CENTER)

                address_label = Label(update_contact_window, text="Address:", fg="white", bg="#3498db", font=myFont)
                address_label.place(relx=0.5, rely=0.7, anchor=CENTER)

                address_var.set(contact['address'])
                address_entry = Entry(update_contact_window, textvariable=address_var, font=myFont, bg="#2ecc71", fg="white", width=20)
                address_entry.place(relx=0.5, rely=0.8, anchor=CENTER)

                update_button = Button(update_contact_window, text="Update", bg="#2ecc71", fg="white", command=perform_update)
                update_button['font'] = myFont
                update_button.place(relx=0.5, rely=0.9, anchor=CENTER)

                # Hide the search button
                search_button.place_forget()
                break
        else:
            no_contacts_label = Label(update_contact_window, text="No contacts found.", fg="white", bg="#3498db", font=myFont)
            no_contacts_label.place(relx=0.5, rely=0.1, anchor=CENTER)

    def perform_update():
        name = name_var.get()
        phone = phone_var.get()
        email = email_var.get()
        address = address_var.get()

        if name and phone and email and address:
            updated_contact = {
                "name": name,
                "phone": phone,
                "email": email,
                "address": address
            }

            contacts = load_contacts()

            for i, contact in enumerate(contacts):
                if contact['name'] == search_var.get() or contact['phone'] == search_var.get():
                    contacts[i] = updated_contact
                    break

            save_contacts(contacts)

            messagebox.showinfo("Success", "Contact has been updated successfully.")
            update_contact_window.destroy()
        else:
            messagebox.showerror("Error", "All fields are required.")

    update_contact_window = Toplevel(root)
    update_contact_window.title("Update Contact")
    update_contact_window.geometry("500x600")
    update_contact_window.resizable(0, 0)
    update_contact_window.configure(bg="#3498db")  # Blue theme

    myFont = font.Font(family='Helvetica', size=16, weight='bold')

    search_label = Label(update_contact_window, text="Search:", fg="white", bg="#3498db", font=myFont)
    search_label.place(relx=0.5, rely=0.1, anchor=CENTER)

    search_var = StringVar()
    search_entry = Entry(update_contact_window, textvariable=search_var, font=myFont, bg="#2ecc71", fg="white", width=20)
    search_entry.place(relx=0.5, rely=0.2, anchor=CENTER)

    search_button = Button(update_contact_window, text="Search", bg="#2ecc71", fg="white", command=search)
    search_button['font'] = myFont
    search_button.place(relx=0.5, rely=0.35, anchor=CENTER)

    # Entry variables for contact information
    name_var = StringVar()
    phone_var = StringVar()
    email_var = StringVar()
    address_var = StringVar()

    root.update()

def delete_contact():
    def search():
        contacts = load_contacts()
        for contact in contacts:
            if search_var.get() == contact['name'] or search_var.get() == contact['phone']:
                display_contact(contact)
                break
        else:
            display_no_contacts_error()

    def display_contact(contact):
        delete_contact_window = Toplevel(root)
        delete_contact_window.title("Delete Contact")
        delete_contact_window.geometry("500x600")
        delete_contact_window.resizable(0, 0)
        delete_contact_window.configure(bg="#3498db")  # Blue theme

        myFont = font.Font(family='Helvetica', size=16, weight='bold')

        name_label = Label(delete_contact_window, text=f"Name: {contact['name']}", fg="white", bg="#3498db", font=myFont)
        name_label.place(relx=0.5, rely=0.1, anchor=CENTER)

        phone_label = Label(delete_contact_window, text=f"Phone: {contact['phone']}", fg="white", bg="#3498db", font=myFont)
        phone_label.place(relx=0.5, rely=0.15, anchor=CENTER)

        email_label = Label(delete_contact_window, text=f"Email: {contact['email']}", fg="white", bg="#3498db", font=myFont)
        email_label.place(relx=0.5, rely=0.2, anchor=CENTER)

        address_label = Label(delete_contact_window, text=f"Address: {contact['address']}", fg="white", bg="#3498db", font=myFont)
        address_label.place(relx=0.5, rely=0.25, anchor=CENTER)

        delete_button = Button(delete_contact_window, text="Delete", bg="#e74c3c", fg="white", command=lambda: delete(contact['name']))
        delete_button['font'] = myFont
        delete_button.place(relx=0.5, rely=0.9, anchor=CENTER)

    def display_no_contacts_error():
        no_contacts_label = Label(delete_contact_window, text="No contacts found.", fg="white", bg="#3498db", font=myFont)
        no_contacts_label.place(relx=0.5, rely=0.1, anchor=CENTER)

    def delete(name):
        contacts = load_contacts()
        contacts = [contact for contact in contacts if contact['name'] != name]
        save_contacts(contacts)
        messagebox.showinfo("Success", "Contact has been deleted successfully.")
        delete_contact_window.destroy()

    delete_contact_window = Toplevel(root)
    delete_contact_window.title("Delete Contact")
    delete_contact_window.geometry("500x600")
    delete_contact_window.resizable(0, 0)
    delete_contact_window.configure(bg="#3498db")  # Blue theme

    myFont = font.Font(family='Helvetica', size=16, weight='bold')

    search_label = Label(delete_contact_window, text="Search:", fg="white", bg="#3498db", font=myFont)
    search_label.place(relx=0.5, rely=0.1, anchor=CENTER)

    search_var = StringVar()
    search_entry = Entry(delete_contact_window, textvariable=search_var, font=myFont, bg="#2ecc71", fg="white", width=20)
    search_entry.place(relx=0.5, rely=0.2, anchor=CENTER)

    search_button = Button(delete_contact_window, text="Search", bg="#2ecc71", fg="white", command=search)
    search_button['font'] = myFont
    search_button.place(relx=0.5, rely=0.35, anchor=CENTER)

root = Tk()
root.title("Contact Book Application")
root.geometry("800x600")
root.resizable(0, 0)
root.configure(bg="#3498db") # Blue theme

myFont = font.Font(family='Helvetica', size=20, weight='bold')
add_button = Button(root, text="Add Contact", bg="#2980b9", fg="white", command=add_contact)
add_button['font'] = myFont
add_button.place(relx=0.5, rely=0.1, anchor=CENTER)

view_button = Button(root, text="View Contacts", bg="#2980b9", fg="white", command=view_contacts)
view_button['font'] = myFont
view_button.place(relx=0.5, rely=0.2, anchor=CENTER)

search_button = Button(root, text="Search Contact", bg="#2980b9", fg="white", command=search_contact)
search_button['font'] = myFont
search_button.place(relx=0.5, rely=0.3, anchor=CENTER)

update_button = Button(root, text="Update Contact", bg="#2980b9", fg="white", command=update_contact)
update_button['font'] = myFont
update_button.place(relx=0.5, rely=0.4, anchor=CENTER)

delete_button = Button(root, text="Delete Contact", bg="#2980b9", fg="white", command=delete_contact)
delete_button['font'] = myFont
delete_button.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()