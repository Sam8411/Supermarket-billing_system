import os
import random
from tkinter import *
from tkinter import messagebox


class SuperMarketBilling:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Supermarket Billing System")
        bg_color = "#074463"

        # Title
        title = Label(self.root, text="Supermarket Billing System", bd=12, relief=GROOVE,
                      bg=bg_color, fg="white", font=("times new roman", 30, "bold"), pady=2).pack(fill=X)

        # ================= Variables ====================
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        self.search_bill = StringVar()
        self.bill_no.set(str(random.randint(1000, 9999)))

        # Grocery items (10)
        self.grocery_items = {
            "Rice": IntVar(), "Wheat": IntVar(), "Sugar": IntVar(), "Oil": IntVar(),
            "Salt": IntVar(), "Dal": IntVar(), "Atta": IntVar(), "Besan": IntVar(),
            "Maida": IntVar(), "Rava": IntVar()
        }

        # Cold drinks (10)
        self.drink_items = {
            "Pepsi": IntVar(), "Coke": IntVar(), "Fanta": IntVar(), "Sprite": IntVar(),
            "Thumbs Up": IntVar(), "7Up": IntVar(), "Mountain Dew": IntVar(), "Mirinda": IntVar(),
            "Slice": IntVar(), "Appy Fizz": IntVar()
        }

        # Medical items (10)
        self.medical_items = {
            "Paracetamol": IntVar(), "Crocin": IntVar(), "Disprin": IntVar(), "Vicks": IntVar(),
            "Savlon": IntVar(), "Dettol": IntVar(), "Hand Sanitizer": IntVar(), "Volini": IntVar(),
            "Bandage": IntVar(), "D-Cold": IntVar()
        }

        # Prices
        self.prices = {
            # groceries
            "Rice": 60, "Wheat": 50, "Sugar": 40, "Oil": 120, "Salt": 20,
            "Dal": 80, "Atta": 55, "Besan": 70, "Maida": 45, "Rava": 50,

            # cold drinks
            "Pepsi": 40, "Coke": 40, "Fanta": 35, "Sprite": 35,
            "Thumbs Up": 40, "7Up": 35, "Mountain Dew": 45, "Mirinda": 35,
            "Slice": 30, "Appy Fizz": 30,

            # medical
            "Paracetamol": 20, "Crocin": 25, "Disprin": 15, "Vicks": 50,
            "Savlon": 70, "Dettol": 90, "Hand Sanitizer": 100, "Volini": 120,
            "Bandage": 10, "D-Cold": 30
        }

        # ================= Customer Frame ====================
        F1 = LabelFrame(self.root, text="Customer Details", font=('times new roman', 15, 'bold'),
                        fg="gold", bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)

        Label(F1, text="Name", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=0, padx=20, pady=5)
        Entry(F1, width=15, textvariable=self.c_name, font="arial 15", bd=7, relief=GROOVE).grid(row=0, column=1, pady=5, padx=10)

        Label(F1, text="Phone", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        Entry(F1, width=15, textvariable=self.c_phone, font="arial 15", bd=7, relief=GROOVE).grid(row=0, column=3, pady=5, padx=10)

        Label(F1, text="Bill No.", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        Entry(F1, width=15, textvariable=self.search_bill, font="arial 15", bd=7, relief=GROOVE).grid(row=0, column=5, pady=5, padx=10)

        Button(F1, text="Search Bill", command=self.find_bill, width=12, bd=7,
               font=('arial', 12, 'bold')).grid(row=0, column=6, pady=5, padx=10)

        Button(F1, text="Search Name", command=self.find_by_name, width=12, bd=7,
               font=('arial', 12, 'bold')).grid(row=0, column=7, pady=5, padx=10)

        # ================= Product Frames ====================
        self.create_product_frame("Groceries", self.grocery_items, 0, 180)
        self.create_product_frame("Cold Drinks", self.drink_items, 325, 180)
        self.create_product_frame("Medical", self.medical_items, 650, 180)

        # ================= Bill Area ====================
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=960, y=180, width=380, height=380)
        Label(F5, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # ================= Button Frame ====================
        btn_f = Frame(self.root, bd=7, relief=GROOVE)
        btn_f.place(x=0, y=560, relwidth=1, height=140)

        Button(btn_f, text="Total", command=self.total, bg="cadetblue", fg="white", pady=15,
               width=12, font="arial 13 bold").grid(row=0, column=0, padx=5, pady=5)

        Button(btn_f, text="Generate Bill", command=self.bill_area, bg="cadetblue", fg="white", pady=15,
               width=12, font="arial 13 bold").grid(row=0, column=1, padx=5, pady=5)

        Button(btn_f, text="Clear", command=self.clear_data, bg="cadetblue", fg="white", pady=15,
               width=12, font="arial 13 bold").grid(row=0, column=2, padx=5, pady=5)

        Button(btn_f, text="Exit", command=self.root.destroy, bg="cadetblue", fg="white", pady=15,
               width=12, font="arial 13 bold").grid(row=0, column=3, padx=5, pady=5)

        Button(btn_f, text="Sales Report", command=self.daily_sales, bg="cadetblue", fg="white", pady=15,
               width=12, font="arial 13 bold").grid(row=0, column=4, padx=5, pady=5)

        self.welcome_bill()

    # ================= Helper Functions ====================
    def create_product_frame(self, title, items, x, y):
        frame = LabelFrame(self.root, text=title, font=('times new roman', 15, 'bold'),
                           fg="gold", bg="#074463")
        frame.place(x=x, y=y, width=325, height=380)

        for idx, (item, var) in enumerate(items.items()):
            Label(frame, text=item, font=("times new roman", 12, "bold"),
                  bg="#074463", fg="white").grid(row=idx, column=0, padx=10, pady=5, sticky="w")
            Entry(frame, width=10, textvariable=var, font="arial 12", bd=5, relief=GROOVE).grid(row=idx, column=1, padx=10, pady=5)

    def total(self):
        self.total_bill = 0
        for category in [self.grocery_items, self.drink_items, self.medical_items]:
            for item, var in category.items():
                qty = var.get()
                if qty > 0:
                    self.total_bill += qty * self.prices[item]

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWelcome to Supermarket\n")
        self.txtarea.insert(END, f"\nBill No: {self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer: {self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone: {self.c_phone.get()}")
        self.txtarea.insert(END, "\n==============================\n")
        self.txtarea.insert(END, "Item\tQty\tPrice\n")
        self.txtarea.insert(END, "==============================\n")

    def bill_area(self):
        self.total()
        self.welcome_bill()

        for category in [self.grocery_items, self.drink_items, self.medical_items]:
            for item, var in category.items():
                qty = var.get()
                if qty > 0:
                    price = qty * self.prices[item]
                    self.txtarea.insert(END, f"{item}\t{qty}\t{price}\n")

        self.txtarea.insert(END, "==============================\n")
        self.txtarea.insert(END, f"Total Bill:\t\t{self.total_bill}\n")
        self.txtarea.insert(END, "==============================\n")

        # Save Bill
        if not os.path.exists("bills"):
            os.mkdir("bills")
        bill_data = self.txtarea.get("1.0", END)
        with open(f"bills/{self.bill_no.get()}.txt", "w") as f:
            f.write(bill_data)

    def find_bill(self):
        if not os.path.exists("bills"):
            messagebox.showerror("Error", "No bills found")
            return
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                with open(f"bills/{i}", "r") as f:
                    self.txtarea.delete("1.0", END)
                    self.txtarea.insert(END, f.read())
                present = "yes"
                break
        if present == "no":
            messagebox.showerror("Error", "Bill not found")

    def find_by_name(self):
        if not os.path.exists("bills"):
            messagebox.showerror("Error", "No bills found")
            return
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
        report = "====== Daily Sales Report ======\n\n"
        if not os.path.exists("bills"):
            messagebox.showinfo("Sales Report", "No bills available")
            return
        for file in os.listdir("bills/"):
            if file.endswith(".txt"):
                with open("bills/" + file, "r") as f:
                    data = f.read()
                    for line in data.split("\n"):
                        if "Total Bill:" in line:
                            try:
                                amt = float(line.split()[-1])
                                total_sales += amt
                                report += f"{file[:-4]} => Rs. {amt}\n"
                            except:
                                pass
        report += f"\nGrand Total: Rs. {total_sales}"
        messagebox.showinfo("Daily Sales", report)

    def clear_data(self):
        self.c_name.set("")
        self.c_phone.set("")
        self.bill_no.set(str(random.randint(1000, 9999)))
        self.search_bill.set("")
        for category in [self.grocery_items, self.drink_items, self.medical_items]:
            for var in category.values():
                var.set(0)
        self.txtarea.delete("1.0", END)
        self.welcome_bill()


# ================= Run Program =================
root = Tk()
obj = SuperMarketBilling(root)
root.mainloop()
