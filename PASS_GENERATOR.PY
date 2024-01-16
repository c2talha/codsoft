from tkinter import *
import random
import pyperclip
import string
import webbrowser

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x400")
        self.root.resizable(0, 0)
        self.root.config(bg="white")

        # define variables
        self.pass_str = StringVar()
        self.pass_len = IntVar()
        self.pass_str.set("")
        self.pass_len.set(0)

        # heading
        title = Label(self.root, text="Password Generator", font=(
            "times new roman", 20, "bold"), bg="white", fg="blue")
        title.place(x=0, y=0, relwidth=1)

        # password length
        pass_label = Label(self.root, text="Password Length: ", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        pass_label.place(x=20, y=60)
        
        pass_entry = Entry(self.root, textvariable=self.pass_len, font=(
            "times new roman", 15, "bold"), bg="lightgray", fg="black")
        pass_entry.place(x=200, y=60, width=150, height=30)

        # password label
        pass_label = Label(self.root, text="Password: ", font=(
            "times new roman", 15, "bold"), bg="white", fg="black")
        pass_label.place(x=20, y=100)

        pass_entry = Entry(self.root, textvariable=self.pass_str, font=(
            "times new roman", 15, "bold"), bg="lightgray", fg="black")
        pass_entry.place(x=200, y=100, width=150, height=30)

        # generate button
        btn_generate = Button(self.root, text="Generate", font=(
            "times new roman", 15, "bold"), bg="lightgreen", fg="black", command=self.generate_password)
        btn_generate.place(x=20, y=140, width=150, height=30)

        # copy button
        btn_copy = Button(self.root, text="Copy", font=(
            "times new roman", 15, "bold"), bg="lightgreen", fg="black", command=self.copy_password)
        btn_copy.place(x=200, y=140, width=150, height=30)

        # exit button
        btn_exit = Button(self.root, text="Exit", font=(
            "times new roman", 15, "bold"), bg="lightgreen", fg="black", command=self.exit)
        btn_exit.place(x=20, y=180, width=330, height=30)
        
        # LinkedIn button
        btn_linkedin = Button(self.root, text="LinkedIn", font=(
            "times new roman", 15, "bold"), bg="lightblue", fg="black", command=self.open_linkedin)
        btn_linkedin.place(x=20, y=220, width=150, height=30)

        # GitHub button
        btn_github = Button(self.root, text="GitHub", font=(
            "times new roman", 15, "bold"), bg="lightblue", fg="black", command=self.open_github)
        btn_github.place(x=200, y=220, width=150, height=30)

        # author name
        author = Label(self.root, text="Created by: Muhammad Talha", font=(
            "times new roman", 15, "bold"), bg="white", fg="red")
        author.place(x=20, y=260)

    def generate_password(self):
        password = []
        for i in range(0, self.pass_len.get()):
            password.append(random.choice(string.ascii_letters + string.digits + string.punctuation))
        self.pass_str.set("".join(password))

    def copy_password(self):
        pyperclip.copy(self.pass_str.get())

    def exit(self):
        self.root.destroy()

    def open_linkedin(self):
        linkedin_url = "https://linkedin.com/in/muhammad-tlhah"
        webbrowser.open_new_tab(linkedin_url)

    def open_github(self):
        github_url = "https://github.com/c2talha"
        webbrowser.open_new_tab(github_url)

root = Tk()
obj = PasswordGenerator(root)
root.mainloop()
