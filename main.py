from tkinter import *
from tkinter import messagebox


class UI:
    def __init__(self, master):

        # window setup
        self.master = master
        self.master.title('Authentication')
        self.master.geometry('400x200')
        self.master.config(bg='#222')

        # window heading
        self.lbl_subheading = Label(self.master, text='Enter login details', font='monospace 12', fg='white', bg='#222')
        self.lbl_subheading.place(x=105, y=10)

        # User label and entry
        self.lbl_user = Label(self.master, text='Username', font='monospace 10', fg='white', bg='#222')
        self.entry_user = Entry(self.master)
        self.entry_user.place(x=150, y=58)
        self.lbl_user.place(x=80, y=60)

        # Password label and entry
        self.lbl_pass = Label(self.master, text='Password', font='monospace 10', fg='white', bg='#222')
        self.entry_pass = Entry(self.master)
        self.lbl_pass.place(x=80, y=90)
        self.entry_pass.place(x=150, y=88)

        # Login button
        self.btn_log = Button(self.master, text='Login', font='monospace 10', bg='#FF69B4', command=self.login)
        self.btn_log.place(x=165, y=130)

        self.data = {'Zoe': 'wavywave99', 'Adam': 'bighead64', 'dekapaan': 'dayon', 'Brent': 'wasabinotaste'}

        self.master.mainloop()

    def login(self):  # checks if username and password are valid
        try:
            user = self.entry_user.get()
            password = self.entry_pass.get()

            # Makes sure no empty fields are accepted
            if user == '':
                raise KeyError
            if password == '':
                raise ValueError

            # if username and password are correct, login proceeds
            if user in self.data:
                if password == self.data[user]:
                    self.master.destroy()
                    import exception_handling
                else:  # if password incorrect, raise exception
                    raise ValueError
            else:  # if user doesn't exist, raise exception
                raise KeyError

        except ValueError:  # exception for incorrect or invalid password entry
            if self.entry_pass.get() == "":
                messagebox.showerror('Error', 'Password field empty')
            else:
                messagebox.showerror('Error', 'Incorrect Password')

        except KeyError:  # exception for incorrect or invalid username entry
            if self.entry_user.get() == '':
                messagebox.showerror("Error", 'Username field empty')
            else:
                messagebox.showerror('Error', "Username doesn't exist")


# instantiation
root = Tk()
UI(root)
