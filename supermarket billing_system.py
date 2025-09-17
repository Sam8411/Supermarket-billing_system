import os
from tkinter import *
from tkinter import messagebox
import math
import random

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#074463"
        title = Label(self.root, text="Billing Software", bd=12, relief=GROOVE, bg=bg_color,
                      fg="white", font=("times new roman", 30, "bold"), pady=2).pack(fill=X)

        # ================= Variables ====================
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()

        # Product totals
        self.total_medical_price = 0
        self.total_grocery_price = 0
        self.total_cold_drinks_price = 0

        # Taxes
        self.c_tax = 0
        self.g_tax = 0
        self.c_d_tax = 0
        self.total_bill = 0

        # ================= Customer Frame ====================
        F1 = LabelFrame(self.root, text="Customer Details", font=('times new roman', 15, 'bold'),
                        fg="gold", bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)

        cname_lbl = Label(F1, text="Customer Name", bg=bg_color, fg="white", font=("times new roman", 18, "bold"))
        cname_lbl.grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font="arial 15", bd=7, relief=GROOVE)
        cname_txt.grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="Customer Phone", bg=bg_color, fg="white", font=("times new roman", 18, "bold"))
        cphn_lbl.grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phone, font="arial 15", bd=7, relief=GROOVE)
        cphn_txt.grid(row=0, column=3, pady=5, padx=10)

        cbill_lbl = Label(F1, text="Bill Number", bg=bg_color, fg="white", font=("times new roman", 18, "bold"))
        cbill_lbl.grid(row=0, column=4, padx=20, pady=5)
        cbill_txt = Entry(F1, width=15, textvariable=self.search_bill, font="arial 15", bd=7, relief=GROOVE)
        cbill_txt.grid(row=0, column=5, pady=5, padx=10)

        bill_btn = Button(F1, text="Search by Bill", command=self.find_bill, width=12, bd=7,
                          font=('arial', 12, 'bold'), relief=GROOVE)
        bill_btn.grid(row=0, column=6, pady=5, padx=10)

        name_btn = Button(F1, text="Search by Name", command=self.find_by_name, width=15, bd=7,
                          font=('arial', 12, 'bold'), relief=GROOVE)
        name_btn.grid(row=0, column=7, pady=5, padx=10)

        # ================= Bill Area ====================
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=960, y=180, width=380, height=380)
        bill_title = Label(F5, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE)
        bill_title.pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # ================= Button Frame ====================
        btn_f = Frame(self.root, bd=7, relief=GROOVE)
        btn_f.place(x=0, y=560, relwidth=1, height=140)

        total_btn = Button(btn_f, text="Total", command=self.total, bg="cadetblue", fg="white", pady=15,
                           width=12, font="arial 13 bold").grid(row=0, column=0, padx=5, pady=5)

        genbill_btn = Button(btn_f, text="Generate Bill", command=self.bill_area, bg="cadetblue", fg="white",
                             pady=15, width=12, font="arial 13 bold").grid(row=0, column=1, padx=5, pady=5)

        clr_btn = Button(btn_f, text="Clear", command=self.clear_data, bg="cadetblue", fg="white", pady=15,
                         width=12, font="arial 13 bold").grid(row=0, column=2, padx=5, pady=5)

        exit_btn = Button(btn_f, text="Exit", command=self.root.destroy, bg="cadetblue", fg="white", pady=15,
                          width=12, font="arial 13 bold").grid(row=0, column=3, padx=5, pady=5)

        report_btn = Button(btn_f, text="Sales Report", command=self.daily_sales, bg="cadetblue", fg="white",
                            pady=15, width=12, font="arial 13 bold").grid(row=0, column=4, padx=5, pady=5)

        self.welcome_bill()

    # ============== Functions ====================

    def total(self):
        # dummy total for now
        self.total_bill = 500
        self.c_tax = 25

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWelcome to Billing Software\n")
        self.txtarea.insert(END, f"\nBill Number: {self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name: {self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number: {self.c_phone.get()}")
        self.txtarea.insert(END, "\n===================================")

    def bill_area(self):
        self.welcome_bill()
        self.txtarea.insert(END, f"\n\nProducts:\n Example Product\t Rs. {self.total_bill}")
        self.txtarea.insert(END, f"\n\nTotal Bil: Rs.{self.total_bill}")

        # save bill
        if not os.path.exists("bills"):
            os.mkdir("bills")
        bill_data = self.txtarea.get("1.0", END)
        with open(f"bills/{self.bill_no.get()}.txt", "w") as f:
            f.write(bill_data)

    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bills/{i}", "r")
                self.txtarea.delete("1.0", END)
                for d in f1:
                    self.txtarea.insert(END, d)
                f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No.")

    def find_by_name(self):
        present = "no"
        for i in os.listdir("bills/"):
            with open(f"bills/{i}", "r") as f:
                data = f.read()
                if self.c_name.get().lower() in data.lower():
                    self.txtarea.delete("1.0", END)
                    self.txtarea.insert(END, data)
                    present = "yes"
                    break
        if present == "no":
            messagebox.showerror("Error", "Customer not found")

    def daily_sales(self):
        total_sales = 0
        if not os.path.exists("bills"):
            messagebox.showinfo("Sales Report", "No bills available")
            return

        for file in os.listdir("bills/"):
            if file.endswith(".txt"):
                with open("bills/" + file, "r") as f:
                    data = f.read()
                    for line in data.split("\n"):
                        if "Total Bil:" in line:
                            try:
                                total_sales += float(line.split("Rs.")[-1])
                            except:
                                pass
        messagebox.showinfo("Daily Sales", f"Total Sales Today: Rs. {total_sales}")

    def clear_data(self):
        self.c_name.set("")
        self.c_phone.set("")
        self.bill_no.set(str(random.randint(1000, 9999)))
        self.search_bill.set("")
        self.txtarea.delete("1.0", END)
        self.welcome_bill()


root = Tk()
obj = Bill_App(root)
root.mainloop()
