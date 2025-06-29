from tkinter import*
from PIL import Image,ImageTk,ImageDraw
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class PharmacyManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1525x800+0+0")

        # =================Add Medicine variable==============
        self.addMed_var = StringVar()
        self.refMed_var = StringVar()

        # =================Main Variable==================
        self.ref_var = StringVar()
        self.cmpName_var = StringVar()
        self.typeMed_var = StringVar()
        self.medName_var = StringVar()
        self.lot_var = StringVar()
        self.issuedate_var = StringVar()
        self.expdate_var = StringVar()
        self.uses_var = StringVar()
        self.sideEffects_var = StringVar()
        self.warning_var = StringVar()
        self.dosage_var = StringVar()
        self.price_var = StringVar()
        self.quantity_var = StringVar()

        lbltitle = Label(self.root, text = "PHARMACY MANAGEMENT SYSTEM", bd=15, relief=RIDGE, bg="white",  # Title
                         fg="navy", font=("times new roman", 50, "bold"), padx=2, pady=4)
        lbltitle.pack(side = TOP, fill = X)

        img1 = Image.open(r"C:\Users\Asus\Desktop\code 1\PharmacyManagementSystem\logo.png") # Logo Location and Size
        img1 = img1.resize((80,80))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        b1 = Button(self.root, image = self.photoimg1, borderwidth = 0) # Logo Button
        b1.place(x = 55, y = 16)

        # =====================Data Frame=====================
        DataFrame = Frame(self.root, bd = 15, relief = RIDGE, padx = 20)
        DataFrame.place(x = 0, y = 120, width = 1530, height = 400)

        DataFrameLeft = LabelFrame(DataFrame, bd = 10, relief = RIDGE, padx = 20, text = "Medicine Information",
                                   fg = "darkgreen", font = ("arial",18,"bold"))
        DataFrameLeft.place(x = 0, y = 5, width = 900, height = 350)

        DataFramerRight = LabelFrame(DataFrame, bd = 10, relief = RIDGE, padx = 20, text = "Medicine Add Department",
                                   fg = "darkgreen", font = ("arial",18,"bold"))
        DataFramerRight.place(x = 910, y = 5, width = 550, height = 350)

        # =====================Button Frame====================
        ButtonFrame = Frame(self.root, bd = 15, relief = RIDGE, padx = 20)
        ButtonFrame.place(x = 0, y = 520, width = 1530, height = 70)

        # =====================Main Button 1======================
        buttonAddData = Button(ButtonFrame, command = self.add_data, text = "Add Medicine", font = ("arial",15,"bold"), width = 14, bg = "navy", fg = "white")
        buttonAddData.grid(row = 0, column = 0, padx = 2)

        buttonUpdateMedicine = Button(ButtonFrame, command = self.update, text = "Update", font = ("arial",15,"bold"), width = 11, bg = "navy", fg = "white")
        buttonUpdateMedicine.grid(row = 0, column = 1, padx = 2)

        buttonDeleteMedicine = Button(ButtonFrame, command = self.delete, text = "Delete", font = ("arial",15,"bold"), width = 11, bg = "navy", fg = "white")
        buttonDeleteMedicine.grid(row = 0, column = 2, padx = 2)

        buttonResetMedicine = Button(ButtonFrame, command = self.reset, text = "Reset", font = ("arial",15,"bold"), width = 11, bg = "navy", fg = "white")
        buttonResetMedicine.grid(row = 0, column = 3, padx = 2)

        buttonExitMedicine = Button(ButtonFrame, text = "Exit", font = ("arial",15,"bold"), width = 11, bg = "navy", fg = "white")
        buttonExitMedicine.grid(row = 0, column = 4, padx = 2)

        # =======================Search===============================
        labelSearch = Label(ButtonFrame, text = "Search By", font = ("arial",15,"bold"), width = 14, bg = "green", fg = "white")
        labelSearch.grid(row = 0, column = 5, padx = 2)

        # variable
        self.search_var = StringVar()

        search_combo = ttk.Combobox(ButtonFrame, textvariable = self.search_var, width = 10, font = ("arial",13,"bold"), state = "readonly")
        search_combo.grid(row = 0, column = 6) 
        search_combo["values"] = ("RefNo", "MedName", "Lot")
        search_combo.current(0)

        # variable
        self.searchTxt_var = StringVar()

        textSearch = Entry (ButtonFrame, textvariable = self.searchTxt_var, bd = 3, relief = RIDGE, width = 12, font = ("arial",13,"bold"))
        textSearch.grid(row = 0, column = 7)

        # ======================Main Button 2==============================
        buttonSearch = Button(ButtonFrame, command = self.search_data, text = "Search", font = ("arial",15,"bold"), width = 11, bg = "navy", fg = "white")
        buttonSearch.grid(row = 0, column = 8, padx = 2)

        buttonShowAll = Button(ButtonFrame, command = self.fetch_data, text = "Show All", font = ("arial",15,"bold"), width = 11, bg = "navy", fg = "white")
        buttonShowAll.grid(row = 0, column = 9, padx = 2)

        # ======================Data Frame Left===============================
        labelrefno = Label(DataFrameLeft, text = "Reference No:", font = ("arial",12,"bold"), padx = 2, pady = 5) # Reference No
        labelrefno.grid(row = 0, column = 0, padx = 5, sticky = W)

        conn = mysql.connector.connect(host = "localhost", username  = "root", password = "kunal@007", database = "mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select Ref from pharma")
        ref = my_cursor.fetchall()
        #ref = [item[0] for item in ref] # coverting the list of tuples to a flat list

        ref_combo = ttk.Combobox(DataFrameLeft, textvariable = self.ref_var, width = 25, font = ("arial",12,"bold"), state = "readonly")
        ref_combo.grid(row = 0, column = 1) 
        ref_combo["values"] = ref
        ref_combo.current(0)

        labelcomapanyname = Label(DataFrameLeft, text = "Company Name:", font = ("arial",12,"bold"), padx = 2, pady = 5) # Company Name
        labelcomapanyname.grid(row = 1, column = 0, padx = 5, sticky = W)
        textSearch = Entry (DataFrameLeft, textvariable = self.cmpName_var, width = 27, font = ("arial",12,"bold"))
        textSearch.grid(row = 1, column = 1)

        labeltypeofmedicine = Label(DataFrameLeft, text = "Type of Medicine:", font = ("arial",12,"bold"), padx = 2, pady = 5) # Type of Medicine
        labeltypeofmedicine.grid(row = 2, column = 0, padx = 5, sticky = W)
        ref_combo = ttk.Combobox(DataFrameLeft, textvariable = self.typeMed_var, width = 25, font = ("arial",12,"bold"), state = "readonly")
        ref_combo.grid(row = 2, column = 1) 
        ref_combo["values"] = ("Tablet", "Liquid", "Capsules", "Topical Medicine", "Drops", "Inhaler", "Injection")
        ref_combo.current(0)

        # ==================Add Medicine=====================

        labelmedicinename = Label(DataFrameLeft, text = "Medicine Name", font = ("arial",12,"bold"), padx = 2, pady = 5) # Medicine Name
        labelmedicinename.grid(row = 3, column = 0, padx = 5, sticky = W)

        conn = mysql.connector.connect(host = "localhost", username  = "root", password = "kunal@007", database = "mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select MedName from pharma")
        med = my_cursor.fetchall()

        ref_combo = ttk.Combobox(DataFrameLeft, textvariable = self.medName_var, width = 25, font = ("arial",12,"bold"), state = "readonly")
        ref_combo.grid(row = 3, column = 1) 
        ref_combo["values"] = med
        ref_combo.current(0)

        labellotno = Label(DataFrameLeft, text = "Lot No:", font = ("arial",12,"bold"), padx = 2, pady = 5) # Lot No
        labellotno.grid(row = 4, column = 0, padx = 5, sticky = W)
        textSearch = Entry (DataFrameLeft, textvariable = self.lot_var, width = 27, font = ("arial",12,"bold"))
        textSearch.grid(row = 4, column = 1)
     
        labelIssuedate = Label(DataFrameLeft, text = "Issue Date:", font = ("arial",12,"bold"), padx = 2, pady = 5) # Issue Date
        labelIssuedate.grid(row = 5, column = 0, padx = 5, sticky = W)
        textSearch = Entry (DataFrameLeft, textvariable = self.issuedate_var, width = 27, font = ("arial",12,"bold"))
        textSearch.grid(row = 5, column = 1)

        labelExpirydate = Label(DataFrameLeft, text = "Expiry Date:", font = ("arial",12,"bold"), padx = 2, pady = 5) # Expiry Date
        labelExpirydate.grid(row = 6, column = 0, padx = 5, sticky = W)
        textSearch = Entry (DataFrameLeft, textvariable = self.expdate_var, width = 27, font = ("arial",12,"bold"))
        textSearch.grid(row = 6, column = 1)

        labelUses = Label(DataFrameLeft, text = "Uses:", font = ("arial",12,"bold"), padx = 2, pady = 5) # Uses
        labelUses.grid(row = 7, column = 0, padx = 5, sticky = W)
        textSearch = Entry (DataFrameLeft, textvariable = self.uses_var, width = 27, font = ("arial",12,"bold"))
        textSearch.grid(row = 7, column = 1)

        labelSideEffects = Label(DataFrameLeft, text = "Side Effects:", font = ("arial",12,"bold"), padx = 2, pady = 5) # Side Effects
        labelSideEffects.grid(row = 8, column = 0, padx = 5, sticky = W)
        textSearch = Entry (DataFrameLeft, textvariable = self.sideEffects_var, width = 27, font = ("arial",12,"bold"))
        textSearch.grid(row = 8, column = 1)

        labelPrecWarning = Label(DataFrameLeft, text = "Precaution & Warning:", font = ("arial",12,"bold"), padx = 2, pady = 5) # Precaution & Warning
        labelPrecWarning.grid(row = 0, column = 2, padx = 5, sticky = W)
        textSearch = Entry (DataFrameLeft, textvariable = self.warning_var, width = 27, font = ("arial",12,"bold"))
        textSearch.grid(row = 0, column = 3)

        labelDosage = Label(DataFrameLeft, text = "Dosage:", font = ("arial",12,"bold"), padx = 2, pady = 5) # Dosage
        labelDosage.grid(row = 1, column = 2, padx = 5, sticky = W)
        textSearch = Entry (DataFrameLeft, textvariable = self.dosage_var, width = 27, font = ("arial",12,"bold"))
        textSearch.grid(row = 1, column = 3)

        labelprice = Label(DataFrameLeft, text = "Price:", font = ("arial",12,"bold"), padx = 2, pady = 5) # Price
        labelprice.grid(row = 2, column = 2, padx = 5, sticky = W)
        textSearch = Entry (DataFrameLeft, textvariable = self.price_var, width = 27, font = ("arial",12,"bold"))
        textSearch.grid(row = 2, column = 3)

        labelquantity = Label(DataFrameLeft, text = "Quantity:", font = ("arial",12,"bold"), padx = 2, pady = 5) # Quantity
        labelquantity.grid(row = 3, column = 2, padx = 5, sticky = W)
        textSearch = Entry (DataFrameLeft, textvariable = self.quantity_var, width = 27, font = ("arial",12,"bold"))
        textSearch.grid(row = 3, column = 3)

        # =================Images (Medicine Information Section)=================
        img2 = Image.open(r"C:\Users\Asus\Desktop\code 1\PharmacyManagementSystem\tablet.png") # tablet Location and Size
        img2 = img2.resize((150,130))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        b1 = Button(self.root, image = self.photoimg2, borderwidth = 0) # tablet Button
        b1.place(x = 475, y = 320)

        img3 = Image.open(r"C:\Users\Asus\Desktop\code 1\PharmacyManagementSystem\laboratory.png") # laboratory Location and Size
        img3 = img3.resize((150,130))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        b1 = Button(self.root, image = self.photoimg3, borderwidth = 0) # laboratory Button
        b1.place(x = 620, y = 320)

        img4 = Image.open(r"C:\Users\Asus\Desktop\code 1\PharmacyManagementSystem\medicine.png") #  medicine Location and Size
        img4 = img4.resize((150,130))
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1 = Button(self.root, image = self.photoimg4, borderwidth = 0) # medicine Button
        b1.place(x = 770, y = 320)

        # ======================Data Frame Right================================
        labelref = Label(DataFramerRight, text = "Reference No:", font = ("arial",12,"bold"), padx = 2, pady = 5) # Reference No
        labelref.place(x = 0, y = 80)
        textref = Entry (DataFramerRight, textvariable = self.refMed_var, width = 17, font = ("arial",12,"bold"))
        textref.place(x = 135, y = 80)

        labelmedicine_name = Label(DataFramerRight, text = "Medicine Name:", font = ("arial",12,"bold"), padx = 2, pady = 5) # Medicine Name
        labelmedicine_name.place(x = 0, y = 110)
        textmedicine_name = Entry (DataFramerRight, textvariable = self.addMed_var, width = 17, font = ("arial",12,"bold"))
        textmedicine_name.place(x = 135, y = 110)

        # ====================Images (Medicine Add Department Section)=====================
        img5 = Image.open(r"C:\Users\Asus\Desktop\code 1\PharmacyManagementSystem\pills.png") #  medicine Location and Size
        img5 = img5.resize((135,75))
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1 = Button(self.root, image = self.photoimg5, borderwidth = 0) # medicine Button
        b1.place(x = 980, y = 170) 

        img6 = Image.open(r"C:\Users\Asus\Desktop\code 1\PharmacyManagementSystem\pharmacy.png") #  medicine Location and Size
        img6 = img6.resize((160,75))
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b1 = Button(self.root, image = self.photoimg6, borderwidth = 0) # medicine Button
        b1.place(x = 1120, y = 170) 

        img7 = Image.open(r"C:\Users\Asus\Desktop\code 1\PharmacyManagementSystem\logo2.png") #  medicine Location and Size
        img7 = img7.resize((165,150))
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b1 = Button(self.root, image = self.photoimg7, borderwidth = 0) # medicine Button
        b1.place(x = 1290, y = 170) 

        # ======================Right Side Frame===========================
        side_frame = Frame(DataFramerRight, bd = 4, relief = RIDGE, bg = "White") # Table 
        side_frame.place(x = 0, y = 150, width = 290, height = 160)

        sc_x = ttk.Scrollbar(side_frame, orient = HORIZONTAL) # Scroll Bar
        sc_x.pack(side = BOTTOM, fill = X)
        sc_y = ttk.Scrollbar(side_frame, orient = VERTICAL)
        sc_y.pack(side = RIGHT, fill = Y)

        self.medicine_table = ttk.Treeview(side_frame, column = ("ref","medicine_name"), xscrollcommand = sc_x.set, yscrollcommand = sc_y.set) 
        sc_x.config(command = self.medicine_table.xview)
        sc_y.config(command = self.medicine_table.yview)

        self.medicine_table.heading("ref", text = "Ref") # Table Headings
        self.medicine_table.heading("medicine_name", text = "Medicine Name")

        self.medicine_table["show"] = "headings"
        self.medicine_table.pack(fill = BOTH, expand = 1)

        self.medicine_table.column("ref", width = 100)
        self.medicine_table.column("medicine_name", width = 100)

        self.medicine_table.bind("<ButtonRelease-1>", self.Medget_cursor)

        # ========================Medicine Add Button==================
        down_frame = Frame(DataFramerRight, bd = 4, relief = RIDGE, bg = "navy")
        down_frame.place(x = 330, y = 150, width = 135, height = 160)

        buttonAddMed = Button(down_frame, text = "Add", font = ("arial",12,"bold"), width = 12, bg = "green", fg = "white", pady = 4, command = self.AddMed)
        buttonAddMed.grid(row = 0, column = 0)

        buttonUpdateMed = Button(down_frame, text = "Update", font = ("arial",12,"bold"), width = 12, bg = "green", fg = "white", pady = 4, command = self.UpdateMed)
        buttonUpdateMed.grid(row = 1, column = 0)

        buttonDeleteMed = Button(down_frame, text = "Delete", font = ("arial",12,"bold"), width = 12, bg = "green", fg = "white", pady = 4, command = self.DeleteMed)
        buttonDeleteMed.grid(row = 2, column = 0)

        buttonClearMed = Button(down_frame, text = "Clear", font = ("arial",12,"bold"), width = 12, bg = "green", fg = "white", pady = 4, command = self.ClearMed)
        buttonClearMed.grid(row = 3, column = 0)

        # ============================Frame Details==========================
        FrameDetails = Frame(self.root, bd = 15, relief = RIDGE)
        FrameDetails.place(x = 0, y = 580, width = 1530, height = 210)

        # ======================== Main Table & Scrollbar====================
        table_frame = Frame(FrameDetails, bd = 15, relief = RIDGE, padx = 20)
        table_frame.place(x = 0, y = 1, width = 1500, height = 180)
        
        scroll_x = ttk.Scrollbar(FrameDetails, orient = HORIZONTAL)
        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y = ttk.Scrollbar(FrameDetails, orient = VERTICAL)
        scroll_y.pack(side = RIGHT, fill = Y)

        self.pharmacy_table = ttk.Treeview(table_frame, column = ("ref", "companyname", "type", "tabletname", "lotno", "issuedate",
                                                                   "expdate", "uses", "sideeffect", "warning", "dosage", "price", "quantity"),
                                                                   xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)
        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)

        scroll_x.config(command = self.pharmacy_table.xview)
        scroll_y.config(command = self.pharmacy_table.yview)

        self.pharmacy_table["show"] = "headings"

        self.pharmacy_table.heading("ref", text = "Reference No")
        self.pharmacy_table.heading("companyname", text = "Company Name")
        self.pharmacy_table.heading("type", text = "Type of Medicine")
        self.pharmacy_table.heading("tabletname", text = "Tablet Name")
        self.pharmacy_table.heading("lotno", text = "Lot No")
        self.pharmacy_table.heading("issuedate", text = "Issue Date")
        self.pharmacy_table.heading("expdate", text = "Expiry Date")
        self.pharmacy_table.heading("uses", text = "Uses")
        self.pharmacy_table.heading("sideeffect", text = "Side Effects")
        self.pharmacy_table.heading("warning", text = "Precaution & Warning")
        self.pharmacy_table.heading("dosage", text = "Dosage")
        self.pharmacy_table.heading("price", text = "Price")
        self.pharmacy_table.heading("quantity", text = "Quantity")
        self.pharmacy_table.pack(fill = BOTH, expand = 1)

        self.pharmacy_table.column("ref", width = 100)
        self.pharmacy_table.column("companyname", width = 120)
        self.pharmacy_table.column("type", width = 120)
        self.pharmacy_table.column("tabletname", width = 120)
        self.pharmacy_table.column("lotno", width = 100)
        self.pharmacy_table.column("issuedate", width = 100)
        self.pharmacy_table.column("expdate", width = 100)
        self.pharmacy_table.column("uses", width = 100)
        self.pharmacy_table.column("sideeffect", width = 100)
        self.pharmacy_table.column("warning", width = 150)
        self.pharmacy_table.column("dosage", width = 100)
        self.pharmacy_table.column("price", width = 100)
        self.pharmacy_table.column("quantity", width = 100)
        self.fetch_datMed()
        self.fetch_data()
        self.pharmacy_table.bind("<ButtonRelease-1>",self.get_cursor)

    # ==================Add Medicine Functionality Declaration================

    def AddMed(self):
        try:
            conn = mysql.connector.connect(host = "localhost", username  = "root", password = "kunal@007", database = "mydata")
            my_cursor = conn.cursor()
            print("Database Connected Successfully.....")
            my_cursor.execute("insert into pharma(Ref, MedName) values(%s,%s)", (self.refMed_var.get(), self.addMed_var.get()))
            conn.commit()
            self.fetch_datMed()
            #self.Medget_cursor() 
            conn.close()
            messagebox.showinfo("Success", "Medicine Added")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    def fetch_datMed(self):
        conn = mysql.connector.connect(host = "localhost", username  = "root", password = "kunal@007", database = "mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from pharma")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for i in rows:
                self.medicine_table.insert("",END, values = i)
            conn.commit()
        conn.close()    

    # ==============MedgetCursor==================
    def Medget_cursor(self, event =""):
        cursor_row = self.medicine_table.focus()
        content = self.medicine_table.item(cursor_row)
        row = content["values"]
        self.refMed_var.set(row[0])
        self.addMed_var.set(row[1])
    
    def UpdateMed(self):
        if self.refMed_var.get() == "" or self.addMed_var.get() == "":
            messagebox.showerror("Error", "All Fields are Required")
        else:
            conn = mysql.connector.connect(host = "localhost", username  = "root", password = "kunal@007", database = "mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("update pharma set MedName = %s where Ref = %s", (self.addMed_var.get(),self.refMed_var.get(),))
            conn.commit()
            self.fetch_datMed()
            conn.close()

            messagebox.showinfo("Success","Medicine has been Updated")

    def DeleteMed(self):
        conn = mysql.connector.connect(host = "localhost", username  = "root", password = "kunal@007", database = "mydata")
        my_cursor = conn.cursor()

        sql = "delete from pharma where Ref = %s"
        val = (self.refMed_var.get(),)
        my_cursor.execute(sql,val)
        conn.commit()
        self.fetch_datMed()
        conn.close()
    
    def ClearMed(self):
        self.refMed_var.set("")
        self.addMed_var.set("")

    # =======================Main Table===================
    def add_data(self):
        if self.ref_var.get() == "" or self.lot_var.get() == "":
            messagebox.showerror("Error","All Fields are Required")
        else:
            conn = mysql.connector.connect(host = "localhost", username  = "root", password = "kunal@007", database = "mydata")
            my_cursor = conn.cursor()
            print("Database Connected Successfully.....")
            my_cursor.execute("insert into pharmacy values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                                                                                self.ref_var.get(), 
                                                                                                self.cmpName_var.get(),
                                                                                                self.typeMed_var.get(),
                                                                                                self.medName_var.get(),
                                                                                                self.lot_var.get(),
                                                                                                self.issuedate_var.get(),
                                                                                                self.expdate_var.get(),
                                                                                                self.uses_var.get(),
                                                                                                self.sideEffects_var.get(),
                                                                                                self.warning_var.get(),
                                                                                                self.dosage_var.get(),
                                                                                                self.price_var.get(),
                                                                                                self.quantity_var.get()
                                                                                                ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Data has been Inserted")

    def fetch_data(self):
        conn = mysql.connector.connect(host = "localhost", username  = "root", password = "kunal@007", database = "mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from pharmacy")
        row = my_cursor.fetchall()
        if len(row) != 0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in row:
                self.pharmacy_table.insert("",END, values = i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.pharmacy_table.focus()
        content = self.pharmacy_table.item(cursor_row)
        row = content["values"]
        self.ref_var.set(row[0])
        self.cmpName_var.set(row[1])
        self.typeMed_var.set(row[2])
        self.medName_var.set(row[3])
        self.lot_var.set(row[4])
        self.issuedate_var.set(row[5])
        self.expdate_var.set(row[6])
        self.uses_var.set(row[7])
        self.sideEffects_var.set(row[8])
        self.warning_var.set(row[9])
        self.dosage_var.set(row[10])
        self.price_var.set(row[11])
        self.quantity_var.set(row[12])

    def update(self):
        if self.ref_var.get() == "" or self.lot_var.get() == "":
            messagebox.showerror("Error", "All Fields are Required")
        else:
            conn = mysql.connector.connect(host = "localhost", username  = "root", password = "kunal@007", database = "mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("update pharmacy set cmpName = %s, TypeMed = %s, MedName = %s, Lot = %s, IssueDate = %s, ExpDate = %s, Uses = %s, sideEffects = %s, warning = %s, dosage = %s, price = %s, quantity = %s where refNo = %s", (
                                                                                                                                                                                                                                            self.cmpName_var.get(),
                                                                                                                                                                                                                                            self.typeMed_var.get(),
                                                                                                                                                                                                                                            self.medName_var.get(),
                                                                                                                                                                                                                                            self.lot_var.get(),
                                                                                                                                                                                                                                            self.issuedate_var.get(),
                                                                                                                                                                                                                                            self.expdate_var.get(),
                                                                                                                                                                                                                                            self.uses_var.get(),
                                                                                                                                                                                                                                            self.sideEffects_var.get(),
                                                                                                                                                                                                                                            self.warning_var.get(),
                                                                                                                                                                                                                                            self.dosage_var.get(),
                                                                                                                                                                                                                                            self.price_var.get(),
                                                                                                                                                                                                                                            self.quantity_var.get(),
                                                                                                                                                                                                                                            self.ref_var.get()
                                                                                                                                                                                                                                        ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("UPDATED","Record has been updated successfully")

    def delete(self):
        conn = mysql.connector.connect(host = "localhost", username  = "root", password = "kunal@007", database = "mydata")
        my_cursor = conn.cursor()
        sql = "delete from pharmacy where refNo = %s"
        val = (self.ref_var.get(),)
        my_cursor.execute(sql,val)
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("DELETED","Record has been deleted successfully")

    def reset(self):
        #self.ref_var.set("")
        self.cmpName_var.set("")
        #self.typeMed_var.set("")
        #self.medName_var.set("")
        self.lot_var.set("")
        self.issuedate_var.set("")
        self.expdate_var.set("")
        self.uses_var.set("")
        self.sideEffects_var.set("")
        self.warning_var.set("")
        self.dosage_var.set("")
        self.price_var.set("")
        self.quantity_var.set("")

    def search_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="kunal@007", database="mydata")
        my_cursor = conn.cursor()
        search_column = self.search_var.get()  
        search_text = self.searchTxt_var.get()
        if not search_column or not search_text:
            messagebox.showwarning("Input Error", "Please provide both search column and search text.")
            return
        query = f"SELECT * FROM pharmacy WHERE {search_column} LIKE %s"
        value = (f"%{search_text}%",)
        my_cursor.execute(query, value) 
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())  
            for row in rows:
                self.pharmacy_table.insert("", END, values=row)
        conn.commit()
        conn.close() 


if __name__ == "__main__":
    root = Tk()
    obj = PharmacyManagementSystem(root)
    root.mainloop()