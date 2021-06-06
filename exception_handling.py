from tkinter import *
from tkinter import messagebox


class ExceptionHandleGUI:
    def __init__(self, master):
        # Window setup
        self.master = master
        self.master.geometry('300x120')
        self.master.title('Exception Handling')
        self.master.config(bg='#222')

        # Amount in account label and entry
        self.lbl_amount = Label(self.master, text='Please enter amount in you account', font='monospace 10', bg='#222',
                                fg='white')
        self.entry_amount = Entry(self.master, width=21)
        self.lbl_amount.pack()
        self.entry_amount.pack()

        # Verification button
        self.btn_verify = Button(self.master, text='Check qualification', bg='#FF69B4', font='monospace 10', width=18,
                                 command=self.qualify)
        self.btn_verify.pack()

        # Show window
        self.master.mainloop()

    def qualify(self):      # Checks if amount is over or under 3000 to see if you qualify for malaysia trip
        try:
            amount = int(self.entry_amount.get())  # gets amount
            if amount < 0:  # if value is negative, raise exception
                raise ValueError

            if amount < 3000:
                messagebox.showerror('Sorry', 'You do not qualify to go to Malaysia')

            if amount >= 3000:
                messagebox.showinfo('Good news', 'Congratulations. You qualify to go to Malaysia')

        except ValueError:  # used to trap invalid variable type and negative amounts
            messagebox.showwarning(message='Invalid amount')


# instantiation
member_area = Tk()
ExceptionHandleGUI(member_area)
