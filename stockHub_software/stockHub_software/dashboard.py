
from tkinter import *
from tkinter import messagebox
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sqlite3
import mplcursors

class Main:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x1000+10+0")
        self.root.title("InventoryHub Software")

        self.root.config(bg="white")

        # Load the icon image (GIF or PNG only)
        try:
            self.icon_title = PhotoImage(file="images/icons8-cart.gif")  # Ensure path is correct
        except Exception as e:
            print(f"Error loading image: {e}")
            self.icon_title = None

        # Title background bar
        title_bar = Label(self.root, bg="#ff66a3")
        title_bar.place(x=0, y=0, relwidth=1, height=70)

        # Display the icon image if loaded successfully
        if self.icon_title:
            icon_label = Label(self.root, image=self.icon_title, bg="#ff66a3")
            icon_label.place(x=10, y=5)  # Adjust the x-coordinate to move the icon to the left

        # Display the title text
        title = Label(self.root, text="InventoryHub Software", font=("times new roman", 40, "bold"),
                      bg="#ff66a3", fg="black", anchor="w", padx=10)  # Add padding to separate text from the image
        title.place(x=70, y=0, relwidth=1, height=70)  # Start text after the icon

        # Logout button
        btn_logout = Button(self.root, text="Logout", font=("times new roman", 15, "bold"), bg="blue", cursor="hand2", fg="white")
        btn_logout.place(x=1300, y=10, height=50, width=150)    

        # Left menu frame and logo image
        try:
            self.menulogo = Image.open("images/inventory_management.jpg")  # Ensure path is correct

            # Resize the image with correct resampling method (LANCZOS) and aspect ratio
            width, height = self.menulogo.size
            aspect_ratio = width / height
            new_width = 250
            new_height = int(new_width / aspect_ratio)  # Adjust height to maintain aspect ratio

            self.menulogo = self.menulogo.resize((new_width, new_height), Image.Resampling.LANCZOS)
            self.menulogo = ImageTk.PhotoImage(self.menulogo)
        except Exception as e:
            print(f"Error loading menu logo: {e}")
            self.menulogo = None

        left_menu = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        left_menu.place(x=0, y=75, width=230, height=690)

        # Display menu logo if loaded successfully
        if self.menulogo:
            lbl_menulogo = Label(left_menu, image=self.menulogo)
            lbl_menulogo.pack(side=TOP, fill=X)

        lbl_menu = Label(left_menu, text="Menu", compound=LEFT, font=("times new roman", 32, "bold"),
                         bg="#00FF00", fg="white")
        lbl_menu.pack(side=TOP, fill=X)

        # Add a spacer frame for the gap between "Menu" and "Higher_host"
        spacer = Frame(left_menu, height=25, bg="white")  # Adjust height for the gap
        spacer.pack(side=TOP)

        # Higher_host button
        btn_employee = Button(left_menu, text="Employee", font=("times new roman", 22, "bold"),
                              bg="white", fg="black", bd=3, cursor="hand2", command=self.employee_management)
        btn_employee.pack(side=TOP, fill=X)


        # Supplier button
        btn_Supplier = Button(left_menu, text="Supplier", font=("times new roman", 22, "bold"),
                              bg="white", fg="black", cursor="hand2", command=self.supplier_management)
        btn_Supplier.pack(side=TOP, fill=X)

        # Category button
        btn_category = Button(left_menu, text="Category", font=("times new roman", 22, "bold"),
                              bg="white", fg="black", bd=3, cursor="hand2", command=self.category_management)
        btn_category.pack(side=TOP, fill=X)

        # Product and sales button
        btn_product = Button(left_menu, text="Product", font=("times new roman", 22, "bold"),
                             bg="white", fg="black", bd=3, cursor="hand2",command=self.product_management)
        btn_product.pack(side=TOP, fill=X)

        btn_sales = Button(left_menu, text="Sales", font=("times new roman", 22, "bold"),
                           bg="white", fg="black", bd=3, cursor="hand2",command=self.sales_management)
        btn_sales.pack(side=TOP, fill=X)

        # Employee button
        
        # Exit button
        btn_Exit = Button(left_menu, text="Exit", font=("times new roman", 22, "bold"),
                          bg="white", fg="black", bd=3, cursor="hand2")
        btn_Exit.pack(side=TOP, fill=X)

        # Footer label
        lbl_footer = Label(self.root, text="Stock Hub Software | Developed By Chirag \nFor any Technical Issue, contact: 9023748132",
                           font=("times new roman", 12, "bold"), bg="#483C32", fg="white")
        lbl_footer.pack(side=BOTTOM, fill=X)

    def employee_management(self):
        self.new_window = Toplevel(self.root)
        self.new_window.title("Employee Management")
        self.new_window.geometry("1300x900+120+30")
        self.new_window.config(bg="white")

        # Database connection
        self.conn = sqlite3.connect('inventory_management.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                emp_no INTEGER PRIMARY KEY,
                name TEXT,
                gender TEXT,
                contact_no TEXT,
                email TEXT,
                dob TEXT,
                doj TEXT,
                password TEXT,
                user_type TEXT,
                address TEXT,
                salary REAL
            )
        ''')
        self.conn.commit()

        # Search Frame
        search_frame = LabelFrame(self.new_window, text="Search Employee", font=("times new roman", 12, "bold"), bd=3, relief=RIDGE, bg="white")
        search_frame.place(x=10, y=10, width=800, height=70)

        # Search by
        lbl_search = Label(search_frame, text="Search By:", font=("times new roman", 15, "bold"), bg="white")
        lbl_search.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        self.search_by = StringVar()
        search_combo = ttk.Combobox(search_frame, textvariable=self.search_by, font=("times new roman", 13), state="readonly")
        search_combo['values'] = ("Name", "Contact No")
        search_combo.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        self.search_txt = StringVar()
        txt_search = Entry(search_frame, textvariable=self.search_txt, font=("times new roman", 13), bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        btn_search = Button(search_frame, text="Search", font=("times new roman", 13, "bold"), bg="#4CAF50", fg="white", command=self.search_employee)
        btn_search.grid(row=0, column=3, padx=5, pady=5)

        btn_show_all = Button(search_frame, text="Show All", font=("times new roman", 13, "bold"), bg="#4CAF50", fg="white", command=self.fetch_data)
        btn_show_all.grid(row=0, column=4, padx=5, pady=5)

        # Employee Details Frame
        details_frame = LabelFrame(self.new_window, text="Employee Details", font=("times new roman", 12, "bold"), bd=2, relief=RIDGE, bg="white")
        details_frame.place(x=10, y=90, width=1180, height=300)

        # Emp No.
        lbl_emp_no = Label(details_frame, text="Emp No.:", font=("times new roman", 13, "bold"), bg="white")
        lbl_emp_no.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        self.emp_no = StringVar()
        txt_emp_no = Entry(details_frame, textvariable=self.emp_no, font=("times new roman", 13), bd=5, relief=GROOVE)
        txt_emp_no.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        # Name
        lbl_name = Label(details_frame, text="Name:", font=("times new roman", 13, "bold"), bg="white")
        lbl_name.grid(row=0, column=3, padx=10, pady=10, sticky=W)

        self.name = StringVar()
        txt_name = Entry(details_frame, textvariable=self.name, font=("times new roman", 13), bd=5, relief=GROOVE)
        txt_name.grid(row=0, column=4, padx=10, pady=10, sticky=W)

        # Gender
        lbl_gender = Label(details_frame, text="Gender:", font=("times new roman", 13, "bold"), bg="white")
        lbl_gender.grid(row=0, column=5, padx=10, pady=10, sticky=W)

        self.gender = StringVar()
        gender_combo = ttk.Combobox(details_frame, textvariable=self.gender, font=("times new roman", 13), state="readonly")
        gender_combo['values'] = ("Male", "Female", "Other")
        gender_combo.grid(row=0, column=6, padx=10, pady=10, sticky=W)

        # Contact No.
        lbl_contact_no = Label(details_frame, text="Contact No.:", font=("times new roman", 13, "bold"), bg="white")
        lbl_contact_no.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        self.contact_no = StringVar()
        txt_contact_no = Entry(details_frame, textvariable=self.contact_no, font=("times new roman", 13), bd=5, relief=GROOVE)
        txt_contact_no.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        # Email
        lbl_email = Label(details_frame, text="Email:", font=("times new roman", 13, "bold"), bg="white")
        lbl_email.grid(row=2, column=5, padx=10, pady=10, sticky=W)

        self.email = StringVar()
        txt_email = Entry(details_frame, textvariable=self.email, font=("times new roman", 13), bd=5, relief=GROOVE)
        txt_email.grid(row=2, column=6, padx=10, pady=10, sticky=W)

        # D.O.B
        lbl_dob = Label(details_frame, text="D.O.B:", font=("times new roman", 13, "bold"), bg="white")
        lbl_dob.grid(row=1, column=3, padx=10, pady=10, sticky=W)

        self.dob = StringVar()
        txt_dob = Entry(details_frame, textvariable=self.dob, font=("times new roman", 13), bd=5, relief=GROOVE)
        txt_dob.grid(row=1, column=4, padx=10, pady=10, sticky=W)

        # D.O.J
        lbl_doj = Label(details_frame, text="D.O.J:", font=("times new roman", 13, "bold"), bg="white")
        lbl_doj.grid(row=1, column=5, padx=10, pady=10, sticky=W)

        self.doj = StringVar()
        txt_doj = Entry(details_frame, textvariable=self.doj, font=("times new roman", 13), bd=5, relief=GROOVE)
        txt_doj.grid(row=1, column=6, padx=10, pady=10, sticky=W)

        # Password
        lbl_password = Label(details_frame, text="Password:", font=("times new roman", 13, "bold"), bg="white")
        lbl_password.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        self.password = StringVar()
        txt_password = Entry(details_frame, textvariable=self.password, font=("times new roman", 13), bd=5, relief=GROOVE)
        txt_password.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        # User Type
        lbl_user_type = Label(details_frame, text="User Type:", font=("times new roman", 13, "bold"), bg="white")
        lbl_user_type.grid(row=3, column=0, padx=10, pady=10, sticky=W)

        self.user_type = StringVar()
        user_type_combo = ttk.Combobox(details_frame, textvariable=self.user_type, font=("times new roman", 13), state="readonly")
        user_type_combo['values'] = ("Admin", "Employee")
        user_type_combo.grid(row=3, column=1, padx=10, pady=10, sticky=W)

        # Address
        lbl_address = Label(details_frame, text="Address:", font=("times new roman", 13, "bold"), bg="white")
        lbl_address.grid(row=3, column=5, padx=10, pady=10, sticky=W)

        self.address = StringVar()
        txt_address = Entry(details_frame, textvariable=self.address, font=("times new roman", 13), bd=5, relief=GROOVE)
        txt_address.grid(row=3, column=6, padx=10, pady=10, sticky=W)

        # Salary
        lbl_salary = Label(details_frame, text="Salary:", font=("times new roman", 13, "bold"), bg="white")
        lbl_salary.grid(row=2, column=3, padx=10, pady=10, sticky=W)

        self.salary = StringVar()
        txt_salary = Entry(details_frame, textvariable=self.salary, font=("times new roman", 13), bd=5, relief=GROOVE)
        txt_salary.grid(row=2, column=4, padx=10, pady=10, sticky=W)

        # Buttons Frame
        btn_frame = Frame(details_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=10, y=220, width=1150, height=50)

        btn_save = Button(btn_frame, text="Save", font=("times new roman", 13, "bold"), bg="#4CAF50", fg="white", command=self.save_employee)
        btn_save.grid(row=0, column=0, padx=10, pady=5)

        btn_update = Button(btn_frame, text="Update", font=("times new roman", 13, "bold"), bg="#008CBA", fg="white", command=self.update_employee)
        btn_update.grid(row=0, column=1, padx=10, pady=5)

        btn_delete = Button(btn_frame, text="Delete", font=("times new roman", 13, "bold"), bg="#f44336", fg="white", command=self.delete_employee)
        btn_delete.grid(row=0, column=2, padx=10, pady=5)

        btn_clear = Button(btn_frame, text="Clear", font=("times new roman", 13, "bold"), bg="#555555", fg="white", command=self.clear_fields)
        btn_clear.grid(row=0, column=3, padx=10, pady=5)

        # Employee List Frame
        list_frame = Frame(self.new_window, bd=3, relief=RIDGE)
        list_frame.place(x=10, y=400, width=1180, height=300)

        scroll_x = Scrollbar(list_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(list_frame, orient=VERTICAL)

        self.employee_list = ttk.Treeview(list_frame, columns=("emp_no", "name", "gender", "contact_no", "email", "dob", "doj", "password", "user_type", "address", "salary"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.employee_list.xview)
        scroll_y.config(command=self.employee_list.yview)

        self.employee_list.heading("emp_no", text="Emp No.")
        self.employee_list.heading("name", text="Name")
        self.employee_list.heading("gender", text="Gender")
        self.employee_list.heading("contact_no", text="Contact No.")
        self.employee_list.heading("email", text="Email")
        self.employee_list.heading("dob", text="D.O.B")
        self.employee_list.heading("doj", text="D.O.J")
        self.employee_list.heading("password", text="Password")
        self.employee_list.heading("user_type", text="User Type")
        self.employee_list.heading("address", text="Address")
        self.employee_list.heading("salary", text="Salary")

        self.employee_list['show'] = 'headings'

        self.employee_list.column("emp_no", width=100)
        self.employee_list.column("name", width=150)
        self.employee_list.column("gender", width=100)
        self.employee_list.column("contact_no", width=150)
        self.employee_list.column("email", width=200)
        self.employee_list.column("dob", width=100)
        self.employee_list.column("doj", width=100)
        self.employee_list.column("password", width=150)
        self.employee_list.column("user_type", width=100)
        self.employee_list.column("address", width=200)
        self.employee_list.column("salary", width=100)

        self.employee_list.pack(fill=BOTH, expand=1)

        self.fetch_data()



    def save_employee(self):
        if self.emp_no.get() == "" or self.name.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                self.cursor.execute('''
                    INSERT INTO employees (emp_no, name, gender, contact_no, email, dob, doj, password, user_type, address, salary)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    self.emp_no.get(),
                    self.name.get(),
                    self.gender.get(),
                    self.contact_no.get(),
                    self.email.get(),
                    self.dob.get(),
                    self.doj.get(),
                    self.password.get(),
                    self.user_type.get(),
                    self.address.get(),
                    self.salary.get()
                ))
                self.conn.commit()
                self.fetch_data()
                self.clear_fields()
                messagebox.showinfo("Success", "Employee saved successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Error saving employee: {e}")

    def update_employee(self):
        if self.emp_no.get() == "" or self.name.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                self.cursor.execute('''
                    UPDATE employees SET
                    name=?, gender=?, contact_no=?, email=?, dob=?, doj=?, password=?, user_type=?, address=?, salary=?
                    WHERE emp_no=?
                ''', (
                    self.name.get(),
                    self.gender.get(),
                    self.contact_no.get(),
                    self.email.get(),
                    self.dob.get(),
                    self.doj.get(),
                    self.password.get(),
                    self.user_type.get(),
                    self.address.get(),
                    self.salary.get(),
                    self.emp_no.get()
                ))
                self.conn.commit()
                self.fetch_data()
                self.clear_fields()
                messagebox.showinfo("Success", "Employee updated successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Error updating employee: {e}")

    def delete_employee(self):
        if self.emp_no.get() == "":
            messagebox.showerror("Error", "Employee number is required")
        else:
            try:
                self.cursor.execute('DELETE FROM employees WHERE emp_no=?', (self.emp_no.get(),))
                self.conn.commit()
                self.fetch_data()
                self.clear_fields()
                messagebox.showinfo("Success", "Employee deleted successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Error deleting employee: {e}")

    def clear_fields(self):
        self.emp_no.set("")
        self.name.set("")
        self.gender.set("")
        self.contact_no.set("")
        self.email.set("")
        self.dob.set("")
        self.doj.set("")
        self.password.set("")
        self.user_type.set("")
        self.address.set("")
        self.salary.set("")

    def fetch_data(self):
        self.cursor.execute("SELECT * FROM employees")
        rows = self.cursor.fetchall()
        if len(rows) != 0:
            self.employee_list.delete(*self.employee_list.get_children())
            for row in rows:
                self.employee_list.insert('', END, values=row)

    def search_employee(self):

        if self.search_by.get() == "" or self.search_txt.get() == "":
            messagebox.showerror("Error", "Select search by and enter search text")
        else:
            try:
                if self.search_by.get() == "Name":
                    self.cursor.execute("SELECT * FROM employees WHERE name LIKE ?", ('%' + self.search_txt.get() + '%',))
                elif self.search_by.get() == "Contact No":
                    self.cursor.execute("SELECT * FROM employees WHERE contact_no LIKE ?", ('%' + self.search_txt.get() + '%',))
                rows = self.cursor.fetchall()
                if len(rows) != 0:
                    self.employee_list.delete(*self.employee_list.get_children())
                    for row in rows:
                        self.employee_list.insert('', END, values=row)
                else:
                    messagebox.showinfo("No Result", "No matching records found")
            except Exception as e:
          
                messagebox.showerror("Error", f"Error searching employee: {e}")

    def supplier_management(self):
     self.supplier_window = Toplevel(self.root)
     self.supplier_window.title("Supplier Management")
     self.supplier_window.geometry("1300x700+120+30")
     self.supplier_window.config(bg="white")
 
     # Database connection
     self.conn = sqlite3.connect('inventory_management.db')
     self.cursor = self.conn.cursor()
     self.cursor.execute('''
         CREATE TABLE IF NOT EXISTS suppliers (
             invoice_no TEXT PRIMARY KEY,
             supplier_name TEXT,
             contact TEXT,
             description TEXT
         )
     ''')
     self.conn.commit()
 
     # Heading
     heading = Label(self.supplier_window, text="Supplier Details", font=("times new roman", 30, "bold"), 
                     bg="#ff66a3", fg="white")
     heading.pack(fill=X)
 
     # Left Frame for Entry Fields
     left_frame = Frame(self.supplier_window, bd=3, relief=RIDGE, bg="white")
     left_frame.place(x=10, y=70, width=600, height=600)
 
     # Labels and Entry Fields
     labels = ["Invoice No.", "Supplier Name", "Contact", "Description"]
     self.supplier_entries = {}
 
     for i, text in enumerate(labels):
         Label(left_frame, text=text + ":", font=("times new roman", 15, "bold"), bg="white").grid(row=i, column=0, padx=10, pady=10, sticky=W)
         if text == "Description":
             self.supplier_entries[text] = Text(left_frame, font=("times new roman", 12), bd=2, relief=GROOVE, width=40, height=5)
         else:
             self.supplier_entries[text] = Entry(left_frame, font=("times new roman", 12), bd=2, relief=GROOVE, width=30)
         self.supplier_entries[text].grid(row=i, column=1, padx=10, pady=10, sticky=W)
 
     # Buttons
     btn_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
     btn_frame.place(x=10, y=300, width=570, height=50)
 
     buttons = [
         ("Save", "#4CAF50", self.save_supplier),
         ("Update", "#008CBA", self.update_supplier),
         ("Delete", "#f44336", self.delete_supplier),
         ("Clear", "#555555", self.clear_supplier_fields)
     ]
 
     for i, (text, color, command) in enumerate(buttons):
         Button(btn_frame, text=text, width=10, font=("times new roman", 12, "bold"), 
               bg=color, fg="white", command=command).grid(row=0, column=i, padx=10, pady=5)
 
     # Right Frame for Search and Table
     right_frame = Frame(self.supplier_window, bd=3, relief=RIDGE, bg="white")
     right_frame.place(x=620, y=70, width=660, height=600)
 
     # Search Frame
     search_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
     search_frame.place(x=10, y=10, width=640, height=60)
 
     Label(search_frame, text="Search by Contact:", font=("times new roman", 13, "bold"), bg="white").grid(row=0, column=0, padx=10, pady=10, sticky=W)
 
     self.search_contact = Entry(search_frame, font=("times new roman", 13), bd=2, relief=GROOVE, width=25)
     self.search_contact.grid(row=0, column=1, padx=10, pady=10, sticky=W)
 
     btn_search = Button(search_frame, text="Search", width=10, font=("times new roman", 12, "bold"), 
                        bg="#4CAF50", fg="white", command=self.search_supplier)
     btn_search.grid(row=0, column=2, padx=10, pady=5)
 
     btn_show_all = Button(search_frame, text="Show All", width=10, font=("times new roman", 12, "bold"), 
                          bg="#4CAF50", fg="white", command=self.fetch_suppliers)
     btn_show_all.grid(row=0, column=3, padx=10, pady=5)
 
     # Table Frame
     table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
     table_frame.place(x=10, y=80, width=640, height=500)
 
     scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
     scroll_y = Scrollbar(table_frame, orient=VERTICAL)
 
     self.supplier_table = ttk.Treeview(
         table_frame,
         columns=("invoice_no", "supplier_name", "contact", "description"),
         xscrollcommand=scroll_x.set,
         yscrollcommand=scroll_y.set
     )
 
     scroll_x.pack(side=BOTTOM, fill=X)
     scroll_y.pack(side=RIGHT, fill=Y)
     scroll_x.config(command=self.supplier_table.xview)
     scroll_y.config(command=self.supplier_table.yview)
 
     columns = ("invoice_no", "supplier_name", "contact", "description")
     for col in columns:
         self.supplier_table.heading(col, text=col.replace('_', ' ').title())
         self.supplier_table.column(col, width=150, anchor=CENTER)
 
     self.supplier_table["show"] = "headings"
     self.supplier_table.pack(fill=BOTH, expand=1)
     self.supplier_table.bind("<ButtonRelease-1>", self.fill_supplier_entries_from_table)
 
     # Initialize data
     self.fetch_suppliers()

    def fetch_suppliers(self):
     
         self.cursor.execute("SELECT * FROM suppliers")
         rows = self.cursor.fetchall()
         if len(rows)!=0:
          self.supplier_table.delete(*self.supplier_table.get_children())
          for row in rows:
             self.supplier_table.insert('', END, values=row)

    def save_supplier(self):
     invoice_no = self.supplier_entries["Invoice No."].get()
     supplier_name = self.supplier_entries["Supplier Name"].get()
     contact = self.supplier_entries["Contact"].get()
     description = self.supplier_entries["Description"].get("1.0", END).strip()

     if not invoice_no or not supplier_name or not contact:
        messagebox.showerror("Error", "Invoice No., Supplier Name, and Contact are required")
     else:
        try:
            self.cursor.execute('''
                INSERT INTO suppliers (invoice_no, supplier_name, contact, description)
                VALUES (?, ?, ?, ?)
            ''', (invoice_no, supplier_name, contact, description))
            self.conn.commit()
            self.fetch_suppliers()
            self.clear_supplier_fields()
            messagebox.showinfo("Success", "Supplier saved successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Error saving supplier: {e}")

    def update_supplier(self):
     invoice_no = self.supplier_entries["Invoice No."].get()
     supplier_name = self.supplier_entries["Supplier Name"].get()
     contact = self.supplier_entries["Contact"].get()
     description = self.supplier_entries["Description"].get("1.0", END).strip()

     if not invoice_no or not supplier_name or not contact:
        messagebox.showerror("Error", "Invoice No., Supplier Name, and Contact are required")
     else:
        try:
            self.cursor.execute('''
                UPDATE suppliers SET
                supplier_name=?, contact=?, description=?
                WHERE invoice_no=?
            ''', (supplier_name, contact, description, invoice_no))
            self.conn.commit()
            self.fetch_suppliers()
            messagebox.showinfo("Success", "Supplier updated successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Error updating supplier: {e}")

    def delete_supplier(self):
     invoice_no = self.supplier_entries["Invoice No."].get()
     if not invoice_no:
         messagebox.showerror("Error", "Invoice No. is required")
     else:
         try:
             self.cursor.execute('DELETE FROM suppliers WHERE invoice_no=?', (invoice_no,))
             self.conn.commit()
             self.fetch_suppliers()
             self.clear_supplier_fields()
             messagebox.showinfo("Success", "Supplier deleted successfully")
         except Exception as e:
             messagebox.showerror("Error", f"Error deleting supplier: {e}")

    def clear_supplier_fields(self):
     for entry in self.supplier_entries.values():
         if isinstance(entry, Text):
             entry.delete("1.0", END)
         else:
             entry.delete(0, END)

    def search_supplier(self):
     contact = self.search_contact.get()
     if not contact:
         messagebox.showerror("Error", "Please enter a contact number to search")
     else:
         try:
             self.cursor.execute("SELECT * FROM suppliers WHERE contact LIKE ?", ('%' + contact + '%',))
             rows = self.cursor.fetchall()
             self.supplier_table.delete(*self.supplier_table.get_children())
             for row in rows:
                 self.supplier_table.insert('', END, values=row)
             if rows:
                 self.fill_supplier_entries(rows[0])  # Fill first matching result
         except Exception as e:
             messagebox.showerror("Error", str(e))

    def fill_supplier_entries(self, data):
     self.clear_supplier_fields()
     self.supplier_entries["Invoice No."].insert(0, data[0])
     self.supplier_entries["Supplier Name"].insert(0, data[1])
     self.supplier_entries["Contact"].insert(0, data[2])
     self.supplier_entries["Description"].insert("1.0", data[3])

    def fill_supplier_entries_from_table(self, event):
      selected_row = self.supplier_table.focus()
      if selected_row:
        data = self.supplier_table.item(selected_row)['values']
        self.fill_supplier_entries(data)
 
    def category_management(self):
     self.category_window = Toplevel(self.root)
     self.category_window.title("Manage Product Category")
     self.category_window.geometry("500x400+200+200")
     self.category_window.config(bg="pink")
 
     # Database connection
     self.conn = sqlite3.connect('inventory_management.db')
     self.cursor = self.conn.cursor()
     self.cursor.execute('''
         CREATE TABLE IF NOT EXISTS categories (
             c_id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT UNIQUE
         )
     ''')
     self.conn.commit()
 
     # Title
     title = Label(self.category_window, text="Manage Product Category", font=("times new roman", 20, "bold"), 
                  bg="#ff66a3", fg="white")
     title.pack(fill=X)
 
     # Entry Frame
     entry_frame = Frame(self.category_window, bd=3, relief=RIDGE, bg="white")
     entry_frame.place(x=10, y=50, width=480, height=100)
 
     # Category Name Label and Entry
     Label(entry_frame, text="Category Name:", font=("times new roman", 15, "bold"), bg="white").grid(row=0, column=0, padx=10, pady=10)
     self.category_name = Entry(entry_frame, font=("times new roman", 15), bd=2, relief=GROOVE)
     self.category_name.grid(row=0, column=1, padx=10, pady=10)
 
     # Buttons Frame
     btn_frame = Frame(entry_frame, bd=2, relief=RIDGE, bg="white")
     btn_frame.place(x=10, y=60, width=460, height=40)
 
     # Add Button
     btn_add = Button(btn_frame, text="Add", width=10, font=("times new roman", 12, "bold"), 
                      bg="#4CAF50", fg="white", command=self.add_category)
     btn_add.grid(row=0, column=0, padx=10, pady=5)
 
     # Delete Button
     btn_delete = Button(btn_frame, text="Delete", width=10, font=("times new roman", 12, "bold"), 
                         bg="#f44336", fg="white", command=self.delete_category)
     btn_delete.grid(row=0, column=1, padx=10, pady=5)
 
     # Table Frame
     table_frame = Frame(self.category_window, bd=3, relief=RIDGE, bg="white")
     table_frame.place(x=10, y=160, width=480, height=220)
 
     # Scrollbars
     scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
     scroll_y = Scrollbar(table_frame, orient=VERTICAL)
 
     # Treeview Table
     self.category_table = ttk.Treeview(
         table_frame,
         columns=("c_id", "name"),
         xscrollcommand=scroll_x.set,
         yscrollcommand=scroll_y.set
     )
 
     # Configure Scrollbars
     scroll_x.config(command=self.category_table.xview)
     scroll_y.config(command=self.category_table.yview)
 
     # Pack Scrollbars
     scroll_x.pack(side=BOTTOM, fill=X)
     scroll_y.pack(side=RIGHT, fill=Y)
 
     # Configure Table Columns
     self.category_table.heading("c_id", text="C.ID")
     self.category_table.heading("name", text="Category Name")
     self.category_table.column("c_id", width=50, anchor=CENTER)
     self.category_table.column("name", width=200, anchor=CENTER)
 
     self.category_table["show"] = "headings"
 
     # Pack Table
     self.category_table.pack(fill=BOTH, expand=1)
 
     # Bind Table Click Event
     self.category_table.bind("<ButtonRelease-1>", self.fill_category_entry)
 
     # Initialize Data
     self.fetch_categories()

    def fetch_categories(self):
     try:
        self.cursor.execute("SELECT * FROM categories")
        rows = self.cursor.fetchall()
        self.category_table.delete(*self.category_table.get_children())
        for row in rows:
            self.category_table.insert('', END, values=row)
     except Exception as e:
        messagebox.showerror("Error", f"Error fetching categories: {e}")

    def add_category(self):
     name = self.category_name.get().strip()
     if not name:
        messagebox.showerror("Error", "Category Name is required")
     else:
        try:
            self.cursor.execute("INSERT INTO categories (name) VALUES (?)", (name,))
            self.conn.commit()
            self.fetch_categories()
            self.category_name.delete(0, END)
            messagebox.showinfo("Success", "Category added successfully")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Category already exists")
        except Exception as e:
            messagebox.showerror("Error", f"Error adding category: {e}")

    def delete_category(self):
     name = self.category_name.get().strip()
     if not name:
        messagebox.showerror("Error", "Category Name is required")
     else:
        try:
            self.cursor.execute("DELETE FROM categories WHERE name=?", (name,))
            self.conn.commit()
            self.fetch_categories()
            self.category_name.delete(0, END)
            messagebox.showinfo("Success", "Category deleted successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Error deleting category: {e}")

    def fill_category_entry(self, event):
     selected_row = self.category_table.focus()
     if selected_row:
        data = self.category_table.item(selected_row)['values']
        self.category_name.delete(0, END)
        self.category_name.insert(0, data[1])  # Fill only the category name

    def product_management(self):
     self.product_window = Toplevel(self.root)
     self.product_window.title("Product Management")
     self.product_window.geometry("1300x700+120+30")
     self.product_window.config(bg="red")
 
     # Database connection
     self.conn = sqlite3.connect('inventory_management.db')
     self.cursor = self.conn.cursor()
     self.cursor.execute('''
         CREATE TABLE IF NOT EXISTS product (
             p_id INTEGER PRIMARY KEY AUTOINCREMENT,
             category TEXT,
             supplier TEXT,
             name TEXT,
             price REAL,
             qty INTEGER,
             Date TEXT
         )
     ''')
     self.conn.commit()
 
     # Title
     title = Label(self.product_window, text="Product Management", font=("times new roman", 30, "bold"), 
                  bg="#ff66a3", fg="white")
     title.pack(fill=X)
 
     # Left Frame for Entry Fields
     left_frame = Frame(self.product_window, bd=3, relief=RIDGE, bg="white")
     left_frame.place(x=10, y=70, width=600, height=600)
 
     # Labels and Entry Fields
     labels = ["Category", "Supplier", "Name", "Price", "QTY","Date"]
     self.product_entries = {}
 
     for i, text in enumerate(labels):
         Label(left_frame, text=text + ":", font=("times new roman", 15, "bold"), bg="white").grid(row=i, column=0, padx=10, pady=10, sticky=W)
         if text == "Category" or text == "Supplier":
             self.product_entries[text] = ttk.Combobox(left_frame, font=("times new roman", 12), state="readonly", width=27)
             if text == "Category":
                 self.product_entries[text]['values'] = self.fetch_categories()
             else:
                 self.product_entries[text]['values'] = self.fetch_suppliers()
         else:
             self.product_entries[text] = Entry(left_frame, font=("times new roman", 12), bd=2, relief=GROOVE, width=30)
         self.product_entries[text].grid(row=i, column=1, padx=10, pady=10, sticky=W)
 
     # Buttons
     btn_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
     btn_frame.place(x=10, y=300, width=570, height=50)
 
     buttons = [
         ("Save", "#4CAF50", self.save_product),
         ("Update", "#008CBA", self.update_product),
         ("Delete", "#f44336", self.delete_product),
         ("Clear", "#555555", self.clear_product_fields)
     ]
 
     for i, (text, color, command) in enumerate(buttons):
         Button(btn_frame, text=text, width=10, font=("times new roman", 12, "bold"), 
               bg=color, fg="white", command=command).grid(row=0, column=i, padx=10, pady=5)
 
     # Right Frame for Search and Table
     right_frame = Frame(self.product_window, bd=3, relief=RIDGE, bg="white")
     right_frame.place(x=620, y=70, width=660, height=600)
 
     # Search Frame
     search_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
     search_frame.place(x=10, y=10, width=640, height=60)
 
     Label(search_frame, text="Search by:", font=("times new roman", 13, "bold"), bg="white").grid(row=0, column=0, padx=10, pady=10, sticky=W)
 
     self.search_by = ttk.Combobox(search_frame, font=("times new roman", 13), state="readonly", width=15)
     self.search_by['values'] = ("Category", "Supplier")
     self.search_by.grid(row=0, column=1, padx=5)
 
     self.search_txt = Entry(search_frame, font=("times new roman", 13), bd=2, relief=GROOVE, width=25)
     self.search_txt.grid(row=0, column=2, padx=5)
 
     btn_search = Button(search_frame, text="Search", width=10, font=("times new roman", 12, "bold"), 
                        bg="#4CAF50", fg="white", command=self.search_product)
     btn_search.grid(row=0, column=3, padx=5)
 
     btn_show_all = Button(search_frame, text="Show All", width=10, font=("times new roman", 12, "bold"), 
                          bg="#4CAF50", fg="white", command=self.fetch_products)
     btn_show_all.grid(row=0, column=4, padx=5)
 
     # Table Frame
     table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
     table_frame.place(x=10, y=80, width=640, height=500)
 
     scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
     scroll_y = Scrollbar(table_frame, orient=VERTICAL)
 
     self.product_table = ttk.Treeview(
         table_frame,
         columns=("p_id", "category", "supplier", "name", "price", "qty","Date"),
         xscrollcommand=scroll_x.set,
         yscrollcommand=scroll_y.set
     )
 
     scroll_x.pack(side=BOTTOM, fill=X)
     scroll_y.pack(side=RIGHT, fill=Y)
     scroll_x.config(command=self.product_table.xview)
     scroll_y.config(command=self.product_table.yview)
 
     columns = ("p_id", "category", "supplier", "name", "price", "qty","Date")
     for col in columns:
         self.product_table.heading(col, text=col.replace('_', ' ').title())
         self.product_table.column(col, width=100, anchor=CENTER)
 
     self.product_table["show"] = "headings"
     self.product_table.pack(fill=BOTH, expand=1)
     self.product_table.bind("<ButtonRelease-1>", self.fill_product_entries_from_table)
 
     # Initialize data
     self.fetch_products()

    def fetch_categories(self):
     self.cursor.execute("SELECT name FROM categories")
     return [row[0] for row in self.cursor.fetchall()]

    def fetch_suppliers(self):
     self.cursor.execute("SELECT supplier_name FROM suppliers")
     return [row[0] for row in self.cursor.fetchall()]

    def save_product(self):
     category = self.product_entries["Category"].get()
     supplier = self.product_entries["Supplier"].get()
     name = self.product_entries["Name"].get()
     price = self.product_entries["Price"].get()
     qty = self.product_entries["QTY"].get()
     Date = self.product_entries["Date"].get()

     if not category or not supplier or not name or not price or not qty or not Date:
         messagebox.showerror("Error", "All fields are required")
     else:
         try:
             self.cursor.execute('''
                 INSERT INTO product (category, supplier, name, price, qty, Date)
                 VALUES (?, ?, ?, ?, ?, ?)
             ''', (category, supplier, name, price, qty, Date))
             self.conn.commit()
             self.fetch_products()
             self.clear_product_fields()
             messagebox.showinfo("Success", "Product saved successfully")
         except Exception as e:
             messagebox.showerror("Error", f"Error saving product: {e}")

    def update_product(self):
     p_id = self.product_table.item(self.product_table.focus())['values'][0]
     category = self.product_entries["Category"].get()
     supplier = self.product_entries["Supplier"].get()
     name = self.product_entries["Name"].get()
     price = self.product_entries["Price"].get()
     qty = self.product_entries["QTY"].get()
     Date = self.product_entries["Date"].get()


     if not p_id or not category or not supplier or not name or not price or not qty:
         messagebox.showerror("Error", "All fields are required")
     else:
         try:
             self.cursor.execute('''
                 UPDATE product SET
                 category=?, supplier=?, name=?, price=?, qty=? ,Date =?
                 WHERE p_id=?
             ''', (category, supplier, name, price, qty, p_id, Date))
             self.conn.commit()
             self.fetch_products()
             messagebox.showinfo("Success", "Product updated successfully")
         except Exception as e:
             messagebox.showerror("Error", f"Error updating product: {e}")

    def delete_product(self):
     p_id = self.product_table.item(self.product_table.focus())['values'][0]
     if not p_id:
         messagebox.showerror("Error", "Select a product to delete")
     else:
         try:
             self.cursor.execute("DELETE FROM product WHERE p_id=?", (p_id,))
             self.conn.commit()
             self.fetch_products()
             self.clear_product_fields()
             messagebox.showinfo("Success", "Product deleted successfully")
         except Exception as e:
             messagebox.showerror("Error", f"Error deleting product: {e}")

    def clear_product_fields(self):
     for entry in self.product_entries.values():
         if isinstance(entry, ttk.Combobox):
             entry.set('')
         else:
             entry.delete(0, END)

    def fetch_products(self):
     self.cursor.execute("SELECT * FROM product")
     rows = self.cursor.fetchall()
     self.product_table.delete(*self.product_table.get_children())
     for row in rows:
         self.product_table.insert('', END, values=row)

    def search_product(self):
     search_by = self.search_by.get()
     search_txt = self.search_txt.get()
     if not search_by or not search_txt:
         messagebox.showerror("Error", "Select search by and enter search text")
     else:
         try:
             if search_by == "Category":
                 self.cursor.execute("SELECT * FROM product WHERE category LIKE ?", ('%' + search_txt + '%',))
             else:
                 self.cursor.execute("SELECT * FROM product WHERE supplier LIKE ?", ('%' + search_txt + '%',))
             rows = self.cursor.fetchall()
             self.product_table.delete(*self.product_table.get_children())
             for row in rows:
                 self.product_table.insert('', END, values=row)
         except Exception as e:
             messagebox.showerror("Error", f"Error searching product: {e}")

    def fill_product_entries_from_table(self, event):
     selected_row = self.product_table.focus()
     if selected_row:
         data = self.product_table.item(selected_row)['values']
         self.product_entries["Category"].set(data[1])
         self.product_entries["Supplier"].set(data[2])
         self.product_entries["Name"].delete(0, END)
         self.product_entries["Name"].insert(0, data[3])
         self.product_entries["Price"].delete(0, END)
         self.product_entries["Price"].insert(0, data[4])
         self.product_entries["QTY"].delete(0, END)
         self.product_entries["QTY"].insert(0, data[5])
         self.product_entries["Date"].delete(0, END)
         self.product_entries["Date"].insert(0,data[6])
         

    def sales_management(self):
        self.sales_window = Toplevel(self.root)
        self.sales_window.title("Sales Management")
        self.sales_window.geometry("1300x800+120+30")
        self.sales_window.config(bg="yellow")

        # Database connection
        self.conn = sqlite3.connect('inventory_management.db')
        self.cursor = self.conn.cursor()

        # Fetch unique dates and categories
        self.cursor.execute("SELECT DISTINCT Date FROM product ORDER BY Date DESC")
        dates = [row[0] for row in self.cursor.fetchall()]

        self.cursor.execute("SELECT DISTINCT category FROM product")
        categories = [row[0] for row in self.cursor.fetchall()]

        # Date and Category Selection Frame
        selection_frame = Frame(self.sales_window, bd=3, relief=RIDGE, bg="white")
        selection_frame.place(x=10, y=10, width=1280, height=60)

        Label(selection_frame, text="Select Date:", font=("times new roman", 12, "bold"), bg="white").grid(row=0, column=0, padx=10, pady=10)
        self.selected_date = StringVar()
        date_combo = ttk.Combobox(selection_frame, textvariable=self.selected_date, font=("times new roman", 12), state="readonly")
        date_combo['values'] = dates
        date_combo.grid(row=0, column=1, padx=10, pady=10)

        Label(selection_frame, text="Select Category:", font=("times new roman", 12, "bold"), bg="white").grid(row=0, column=2, padx=10, pady=10)
        self.selected_category = StringVar()
        category_combo = ttk.Combobox(selection_frame, textvariable=self.selected_category, font=("times new roman", 12), state="readonly")
        category_combo['values'] = categories
        category_combo.grid(row=0, column=3, padx=10, pady=10)

        btn_show_charts = Button(selection_frame, text="Show Product Charts", font=("times new roman", 12, "bold"),
                                bg="#4CAF50", fg="white", command=self.show_product_charts)
        btn_show_charts.grid(row=0, column=4, padx=10, pady=10)

        btn_category_chart = Button(selection_frame, text="Category Chart", font=("times new roman", 12, "bold"),
                                   bg="#008CBA", fg="white", command=self.show_category_chart)
        btn_category_chart.grid(row=0, column=5, padx=10, pady=10)

        # Chart Container Frame with Scrollbars
        self.chart_container = Frame(self.sales_window, bg="white")
        self.chart_container.place(x=10, y=80, width=1280, height=680)

        # Create Canvas and Scrollbars
        self.canvas = Canvas(self.chart_container, bg="white")
        scroll_x = Scrollbar(self.chart_container, orient=HORIZONTAL, command=self.canvas.xview)
        scroll_y = Scrollbar(self.chart_container, orient=VERTICAL, command=self.canvas.yview)
        self.scrollable_frame = Frame(self.canvas, bg="white")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        # Pack scrollbars and canvas
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Show default charts when the page opens
        self.show_default_charts()

    def show_default_charts(self):
        # Clear previous content
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        # Fetch default data (latest date and first category)
        self.cursor.execute("SELECT DISTINCT Date FROM product ORDER BY Date DESC LIMIT 1")
        default_date = self.cursor.fetchone()[0]

        self.cursor.execute("SELECT DISTINCT category FROM product LIMIT 1")
        default_category = self.cursor.fetchone()[0]

        # Set default values in dropdowns
        self.selected_date.set(default_date)
        self.selected_category.set(default_category)

        # Show default charts
        self.show_product_charts()
        self.show_category_chart()

    def show_product_charts(self):
        # Clear previous content
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        selected_date = self.selected_date.get()
        selected_category = self.selected_category.get()

        if not selected_date or not selected_category:
            messagebox.showerror("Error", "Please select both date and category")
            return

        # Fetch product-wise sales data for the selected date and category
        self.cursor.execute('''
            SELECT name, SUM(qty) as total_qty, SUM(price * qty) as total_sales
            FROM product
            WHERE Date = ? AND category = ?
            GROUP BY name
        ''', (selected_date, selected_category))
        product_data = self.cursor.fetchall()

        if not product_data:
            messagebox.showinfo("No Data", f"No sales data found for {selected_date} and {selected_category}")
            return

        # Prepare data
        products = [row[0] for row in product_data]
        quantities = [row[1] for row in product_data]
        sales = [row[2] for row in product_data]

        # Create figures
        fig1, ax1 = plt.subplots(figsize=(10, 5))
        bars = ax1.bar(products, quantities, color='#4CAF50', label='Quantity Sold', picker=True)
        ax1.set_title(f"Product-wise Quantity Sold - {selected_date} ({selected_category})", fontsize=14, pad=20)
        ax1.set_xlabel("Product Name", fontsize=12)
        ax1.set_ylabel("Quantity Sold", fontsize=12)
        ax1.tick_params(axis='x', rotation=45)
        ax1.legend()
        ax1.grid(True, linestyle='--', alpha=0.7)

        # Add hover effect to bars using mplcursors
        cursor1 = mplcursors.cursor(bars, hover=True)
        cursor1.connect(
            "add", lambda sel: sel.annotation.set_text(
                f"Product: {products[sel.target.index]}\nQuantity Sold: {quantities[sel.target.index]}"
            )
        )

        # Add click event to bars
        def on_bar_click(event):
            for bar in bars:
                if bar.contains(event)[0]:
                    index = bars.index(bar)
                    messagebox.showinfo("Product Info", f"Product: {products[index]}\nQuantity Sold: {quantities[index]}")

        fig1.canvas.mpl_connect('pick_event', on_bar_click)

        fig2, ax2 = plt.subplots(figsize=(10, 5))
        explode = [0.1] * len(products)  # Explode effect for pie chart
        wedges, texts, autotexts = ax2.pie(sales, labels=products, autopct='%1.1f%%', explode=explode,
                                           colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'], startangle=90,
                                           wedgeprops={'picker': True})
        ax2.set_title(f"Sales Distribution - {selected_date} ({selected_category})", fontsize=14, pad=20)

        # Add hover effect to pie slices using mplcursors
        cursor2 = mplcursors.cursor(wedges, hover=True)
        cursor2.connect(
            "add", lambda sel: sel.annotation.set_text(
                f"Product: {products[sel.target.index]}\nSales: ₹{sales[sel.target.index]:.2f}"
            )
        )

        # Add click event to pie slices
        def on_pie_click(event):
            for wedge in wedges:
                if wedge.contains(event)[0]:
                    index = wedges.index(wedge)
                    messagebox.showinfo("Product Info", f"Product: {products[index]}\nSales: ₹{sales[index]:.2f}")

        fig2.canvas.mpl_connect('pick_event', on_pie_click)

        # Embed charts in Tkinter
        chart1 = FigureCanvasTkAgg(fig1, master=self.scrollable_frame)
        chart1.get_tk_widget().pack(pady=20, padx=20, fill=BOTH, expand=True)

        chart2 = FigureCanvasTkAgg(fig2, master=self.scrollable_frame)
        chart2.get_tk_widget().pack(pady=20, padx=20, fill=BOTH, expand=True)

        # Update scroll region
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def show_category_chart(self):
        selected_date = self.selected_date.get()
        if not selected_date:
            messagebox.showerror("Error", "Please select a date")
            return

        # Fetch category-wise sales data for the selected date
        self.cursor.execute('''
            SELECT category, SUM(qty) as total_qty, SUM(price * qty) as total_sales
            FROM product
            WHERE Date = ?
            GROUP BY category
        ''', (selected_date,))
        category_data = self.cursor.fetchall()

        if not category_data:
            messagebox.showinfo("No Data", f"No sales data found for {selected_date}")
            return

        # Prepare data
        categories = [row[0] for row in category_data]
        quantities = [row[1] for row in category_data]
        sales = [row[2] for row in category_data]

        # Create figures
        fig, ax = plt.subplots(figsize=(10, 5))
        lines = ax.plot(categories, sales, marker='o', linestyle='-', color='#008CBA', label='Total Sales', picker=True)
        ax.set_title(f"Category-wise Sales - {selected_date}", fontsize=14, pad=20)
        ax.set_xlabel("Category", fontsize=12)
        ax.set_ylabel("Total Sales", fontsize=12)
        ax.tick_params(axis='x', rotation=45)
        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.7)

        # Add hover effect to lines using mplcursors
        cursor = mplcursors.cursor(lines, hover=True)
        cursor.connect(
            "add", lambda sel: sel.annotation.set_text(
                f"Category: {categories[sel.target.index]}\nTotal Sales: ₹{sales[sel.target.index]:.2f}"
            )
        )

        # Add click event to lines
        def on_line_click(event):
            for line in lines:
                if line.contains(event)[0]:
                    index = lines.index(line)
                    messagebox.showinfo("Category Info", f"Category: {categories[index]}\nTotal Sales: ₹{sales[index]:.2f}")

        fig.canvas.mpl_connect('pick_event', on_line_click)

        # Embed chart in Tkinter
        chart = FigureCanvasTkAgg(fig, master=self.scrollable_frame)
        chart.get_tk_widget().pack(pady=20, padx=20, fill=BOTH, expand=True)

        # Update scroll region
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
# Run the application
root = Tk()
obj = Main(root)
root.mainloop() 