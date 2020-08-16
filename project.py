import sqlite3
from tkinter import *
from tkinter import messagebox

#Usability of exceptional handelling
class ADDING_BOOKS:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x600+0+0")
        self.root.title("Add Book")
        self.root.configure(background='cadet blue')

        MainFrame = Frame(self.root)
        MainFrame.pack()
        TitFrame = Frame(MainFrame, padx=5, pady=5, bd=5, relief=RIDGE, )
        TitFrame.pack(side=TOP)
        labelTit = Label(TitFrame, font=('arial', 20, 'bold'), text="Add Book: Details", )
        labelTit.grid()

        DataFrame = Frame(MainFrame, bd=10, width=700, height=300, padx=16, pady=80, relief=RIDGE)
        DataFrame.pack(side=TOP)

        savedataframe = Frame(MainFrame, bd=10, width=400, height=200, padx=200, pady=50, relief=RIDGE, bg="pink")
        savedataframe.pack(side=BOTTOM)

        self.ID_label1 = Label(DataFrame, pady=5, text="Book ID:",font=("arial", 12, ) )
        self.ID_label1.grid(row=0, column=0, sticky="W")
        self.ID_entry1 = Entry(DataFrame, width=30,font=("arial", 12, ))
        self.ID_entry1.grid(row=0, column=1, sticky="W")

        self.Name_label2 = Label(DataFrame, pady=5, text="Book Name:",font=("arial", 12, ) )
        self.Name_label2.grid(row=1, column=0, sticky="W")
        self.Name_entry2 = Entry(DataFrame, width=30,font=("arial", 12, ))
        self.Name_entry2.grid(row=1, column=1, sticky="W")

        self.Pub_label3 = Label(DataFrame, pady=5, text="Publication:",font=("arial", 12, ) )
        self.Pub_label3.grid(row=2, column=0, sticky="W")
        self.Pub_entry3 = Entry(DataFrame, width=30,font=("arial", 12, ))
        self.Pub_entry3.grid(row=2, column=1, sticky="W")

        self.Quantity_label4 = Label(DataFrame, pady=5, text="Book Quantity:",font=("arial", 12, ) )
        self.Quantity_label4.grid(row=3, column=0, sticky="W")
        self.Quantity_entry4 = Entry(DataFrame, width=30,font=("arial", 12, ))
        self.Quantity_entry4.grid(row=3, column=1, sticky="W")

        self.b1 = Button(savedataframe, padx=20,pady=5, text="Add Book", command=self.save_addbook, bd=10)
        self.b1.grid(row=0, column=0)

        self.root.mainloop()

    def Execptional_handling_in_addingbook(self):
        Book_Id = self.ID_entry1.get()
        Book_Name = self.Name_entry2.get()
        Book_Publication = self.Pub_entry3.get()
        Book_Quantity = self.Quantity_entry4.get()
        if Book_Id  == '' or Book_Name== '' or Book_Publication == '' or Book_Quantity == '':
            messagebox.showerror('Oops!', 'please fill all the box')
        else:
            try:
                Book_Id = int(Book_Id)
                Book_Quantity = int(Book_Quantity)
            except Exception:
                messagebox.showerror('Warning!', "Don't use letters in BookId and Book Quantity")

    def save_addbook(self):
        self.Execptional_handling_in_addingbook()
        db = sqlite3.connect("Database.db")
        db.execute("create table if not exists Books(ID int primary key, Name varchar(40),"
                   "Publication varchar(40),Quantity int)")
        db.execute("insert into Books values(?,?,?,?)",(int(self.ID_entry1.get()), self.Name_entry2.get(),
                                                        self.Pub_entry3.get(), int(self.Quantity_entry4.get())))
        db.commit()
        db.close()
        messagebox.showinfo("Info", "Data Saved")
        self.ID_entry1.delete(0, "end")
        self.Name_entry2.delete(0, "end")
        self.Pub_entry3.delete(0, "end")
        self.Quantity_entry4.delete(0, "end")

#                  usability of exceptional handeling      ########################################################################
class ADDING_CUSTOMERS:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x600+0+0")
        self.root.title("Add customer")
        self.root.configure(background='cadet blue')
        MainFrame = Frame(self.root)
        MainFrame.pack()
        TitFrame = Frame(MainFrame, padx=5, pady=5, bd=5, relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.labelTit = Label(TitFrame, font=('arial', 20, 'bold'), text="Add Customer:(Welcome!)", )
        self.labelTit.grid()
        DataFrame = Frame(MainFrame, bd=10, width=500, height=300, padx=16, pady=80, relief=RIDGE, )
        DataFrame.pack(side=TOP)
        savedataframe = Frame(MainFrame, bd=10, width=500, height=200, padx=200, pady=50, relief=RIDGE, bg="pink")
        savedataframe.pack(side=BOTTOM)

        self.ID_label1 = Label(DataFrame, pady=5, text="Customer ID:",font=("arial", 12, ) )
        self.ID_label1.grid(row=0, column=0, sticky="W",)
        self.ID_entry1 = Entry(DataFrame, width=30,font=("arial", 12, ))
        self.ID_entry1.grid(row=0, column=1, sticky="W")

        self.Name_label2 = Label(DataFrame, pady=5, text="Name:", font=("arial", 12, ))
        self.Name_label2.grid(row=1, column=0, sticky="W")
        self.Name_entry2 = Entry(DataFrame, width=30,font=("arial", 12, ))
        self.Name_entry2.grid(row=1, column=1, sticky="W")

        self.Phone_label3 = Label(DataFrame, pady=5, text="Phone No:",font=("arial", 12, ) )
        self.Phone_label3.grid(row=2, column=0, sticky="W")
        self.Phone_entry3 = Entry(DataFrame, width=30,font=("arial", 12, ))
        self.Phone_entry3.grid(row=2, column=1, sticky="W")
        self.b1 = Button(savedataframe, text="Add Customer", command=self.save_addcustomer, bd=10)
        self.b1.grid(row=0,column=0)
        self.root.mainloop()

    def Execptional_handling_in_saving_customer(self):
        Customer_Id = self.ID_entry1.get()
        Customer_Name = self.Name_entry2.get()
        Phone = self.Phone_entry3.get()

        if Customer_Id == '' or Customer_Name == '' or Phone == '':
            messagebox.showerror('Warning!', 'please fill all the box')
        else:
            try:
                Customer_Id = int(Customer_Id)
                Phone = int(Phone)
            except Exception:
                messagebox.showerror('Warning!', "Don't use letters in Customer ID and Phone No:")

    def save_addcustomer(self):
        self.Execptional_handling_in_saving_customer()
        db = sqlite3.connect("Database.db")
        db.execute("create table if not exists Customers(ID int primary key,Name varchar(40), Phone No varchar(30))")
        db.execute("insert into Customers values(?,?,?)",(int(self.ID_entry1.get()), self.Name_entry2.get(), int(self.Phone_entry3.get())))
        db.commit()
        db.close()
        messagebox.showinfo("Info!", "Saved")
        self.ID_entry1.delete(0, "end")
        self.Name_entry2.delete(0, "end")
        self.Phone_entry3.delete(0, "end")

########## File Handling ##############################
class BOOKS_ISSUE:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x600+0+0")
        self.root.title("Issue Book")
        self.root.configure(background='cadet blue')

        MainFrame = Frame(self.root)
        MainFrame.pack()

        TitFrame = Frame(MainFrame, padx=5, pady=5, bd=5, relief=RIDGE)
        TitFrame.pack(side=TOP)
        self.labelTit = Label(TitFrame, font=('arial', 20, 'bold'), text="Book Issue: Create Your World!", )
        self.labelTit.grid()

        DataFrame = Frame(MainFrame, bd=10, width=700, height=300, padx=16, pady=80, relief=RIDGE)
        DataFrame.pack(side=TOP)

        savedataframe = Frame(MainFrame, bd=10, width=500, height=200, padx=20, pady=50, relief=RIDGE, bg="pink")
        savedataframe.pack(side=BOTTOM)

        MainFrame = Frame(self.root)
        MainFrame.pack()

        self.TID_label1 = Label(DataFrame, pady=5, text="Transaction ID:",font=("arial", 12, ) )
        self.TID_label1.grid(row=0, column=0, sticky="W")
        self.TID_entry1 = Entry(DataFrame, width=30,font=("arial", 12, ))
        self.TID_entry1.grid(row=0, column=1, sticky="W")

        self.BID_label2 = Label(DataFrame, pady=5, text="Book Id:",font=("arial", 12, ) )
        self.BID_label2.grid(row=1, column=0, sticky="W")
        self.BID_entry2 = Entry(DataFrame, width=30,font=("arial", 12, ))
        self.BID_entry2.grid(row=1, column=1, sticky="W")

        self.CID_label3 = Label(DataFrame, pady=5, text="Customer ID:",font=("arial", 12, ) )
        self.CID_label3.grid(row=2, column=0, sticky="W")
        self.CID_entry3 = Entry(DataFrame, width=30,font=("arial", 12, ))
        self.CID_entry3.grid(row=2, column=1, sticky="W")

        self.Date_label4 = Label(DataFrame, pady=5, text="Date:",font=("arial", 12, ) )
        self.Date_label4.grid(row=3, column=0, sticky="W")
        self.Date_entry4 = Entry(DataFrame, width=30,font=("arial", 12, ))
        self.Date_entry4.grid(row=3, column=1, sticky="W")

        self.b1 = Button(savedataframe, text="Issue",padx=10, command=self.save_bookissue, bd=10)
        self.b1.place(x=50, y=10)
        self.b2 = Button(savedataframe, text="Add Transaction In File", command=self.File_handling, bd=10)
        self.b2.place(x=250, y=10)

        self.root.mainloop()

    def if_statement(self):
        Transactionid = self.TID_entry1.get()
        Bookid = self.BID_entry2.get()
        Customerid = self.CID_entry3.get()
        Date = self.Date_entry4.get()


        if Transactionid == '' or Bookid == '' or Customerid == '' or Date == '':
            messagebox.showerror('Oops!', 'please fill all the box')
            return

    def File_handling(self):
        txt = open("RecentTransaction.txt", "w")
        txt.write("Transaction Id=" + str(self.TID_entry1.get()))
        txt.write(",  Book Name=" + str(self.BID_entry2.get()))
        txt.write(",  Customer ID=" + str(self.CID_entry3.get()))
        txt.write(",  Date=" + str(self.Date_entry4.get()))
        txt.close()



    def check_Bookid_during_bookissue(self):
        db = sqlite3.connect("Database.db")
        cursor = db.execute("select * from Books where ID=?", (int(self.BID_entry2.get()),))
        records = cursor.fetchall()
        if len(records) == 0:
            db.close()
            return False
        else:
            print(records)

            Bookquantity = int(records[0][3])
            db.close()
            if Bookquantity > 0:
                return True
            else:
                return False

    def check_Customerid_during_bookissue(self):
        db = sqlite3.connect("Database.db")
        db.execute("create table if not exists Customers(ID int primary key,Name varchar(40),Phone No varchar(30))")
        cursor = db.execute("select * from Customers where ID=?", (int(self.CID_entry3.get()),))
        records = cursor.fetchall()
        if len(records) == 0:
            db.close()
            return False
        else:
            db.close()
            return True

    def upddate_quantityinbooks(self):
        db = sqlite3.connect("Database.db")
        db.execute("update Books set Quantity=Quantity-1 where ID=?", (int(self.BID_entry2.get()),))
        db.commit()
        db.close()

    def save_bookissue(self):
        self.if_statement()
        db = sqlite3.connect("Database.db")
        db.execute(
            "create table if not exists Transactions(ID int primary key,BID int,"
            "CID int,Entrydate varchar(50),Returndate varchar(50))")

        if self.check_Bookid_during_bookissue() == False:
            messagebox.showinfo("Error", "Invalid ID")
            return
        if self.check_Customerid_during_bookissue() == False:
            messagebox.showinfo("Error", "Invalid ID")
            return
        self.upddate_quantityinbooks()

        db.execute("insert into Transactions values(?,?,?,?,?)",
                   (int(self.TID_entry1.get()), int(self.BID_entry2.get()), int(self.CID_entry3.get()),
                    self.Date_entry4.get(), "Not Returned"))
        db.commit()
        db.close()
        messagebox.showinfo("Info", "Data Saved")
        self.TID_entry1.delete(0, "end")
        self.BID_entry2.delete(0, "end")
        self.CID_entry3.delete(0, "end")
        self.Date_entry4.delete(0, "end")


class BOOKS_RETURN:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x600+0+0")
        self.root.title("Return Book")
        self.root.configure(background='cadet blue')
        MainFrame = Frame(self.root)
        MainFrame.pack()

        TitFrame = Frame(MainFrame, padx=5, pady=5, bd=5, relief=RIDGE)
        TitFrame.pack(side=TOP)
        self.labelTit = Label(TitFrame, font=('arial', 20, 'bold'), text="Well Done Readers!", )
        self.labelTit.grid()

        DataFrame = Frame(MainFrame, bd=10, width=700, height=300, padx=16, pady=80, relief=RIDGE)
        DataFrame.pack(side=TOP)

        savedataframe = Frame(MainFrame, bd=10, width=400, height=200, padx=200, pady=50, relief=RIDGE, bg="pink")
        savedataframe.pack(side=BOTTOM)

        self.TID_label1 = Label(DataFrame, pady=5, text="Transaction ID:",font=("arial", 12, ) )
        self.TID_label1.grid(row=0, column=0, sticky="W")
        self.TID_entry1 = Entry(DataFrame, width=30,font=("arial", 12, ))
        self.TID_entry1.grid(row=0, column=1, sticky="W")

        self.Date_label2 = Label(DataFrame, pady=5, text="Date:", font=("arial", 12, ))
        self.Date_label2.grid(row=1, column=0, sticky="W")
        self.Date_entry2 = Entry(DataFrame, width=30,font=("arial", 12, ))
        self.Date_entry2.grid(row=1, column=1, sticky="W")

        self.b1 = Button(savedataframe, padx=10,text="Issue", command=self.save_returnbook, bd=10)
        self.b1.grid(row=0, column=0)
        self.root.mainloop()

    def check_transactionid(self):
        db = sqlite3.connect("Database.db")
        cursor = db.execute("select * from Transactions where ID=?", (int(self.TID_entry1.get()),))
        records = cursor.fetchall()
        if len(records) == 0:
            db.close()
            return False
        else:
            return int(records[0][1])

    def update_quantityinbooks(self, ID):
        db = sqlite3.connect("Database.db")
        db.execute("update Books set Quantity=Quantity+1 where ID=?", (ID,))
        db.commit()
        db.close()

    def save_returnbook(self):
        db = sqlite3.connect("Database.db")
        bid = self.check_transactionid()
        if bid == False:
            messagebox.showinfo("Error", "Sorry invalid id")
            return
        self.update_quantityinbooks(bid)
        db.execute("update Transactions set Returndate=? where ID=?", (self.Date_entry2.get(),
                                                                       int(self.TID_entry1.get())))
        db.commit()
        db.close()
        messagebox.showinfo("Info", "Data Saved")

############# usability of exceptional handling #############################
class BOOKS_DELETE():
    def __init__(self):
        self.root=Tk()
        self.root.geometry("800x600+0+0")
        self.root.title("Delete Book")
        self.root.configure(background='cadet blue')
        MainFrame = Frame(self.root)
        MainFrame.pack()
        TitFrame = Frame(MainFrame, padx=5, pady=5, bd=5, relief=RIDGE)
        TitFrame.pack(side=TOP)
        self.labelTit = Label(TitFrame, font=('arial', 20, 'bold'), text="Delete Books", )
        self.labelTit.grid()

        DataFrame = Frame(MainFrame, bd=10, width=700, height=300, padx=16, pady=80, relief=RIDGE)
        DataFrame.pack(side=TOP)

        savedataframe = Frame(MainFrame, bd=10, width=500, height=200, padx=20, pady=50, relief=RIDGE, bg="pink")
        savedataframe.pack(side=BOTTOM)

        self.label1 = Label(DataFrame, pady=5, text="Book ID:",font=("arial", 12, ) )
        self.label1.grid(row=0, column=0, sticky="W")
        self.BID_entry1 = Entry(DataFrame, width=30,font=("arial", 12, ))
        self.BID_entry1.grid(row=0, column=1, sticky="W")


        self.button1=Button(savedataframe,text="Delete Book",command=self.DELETE_BOOKS,bd=10)
        self.button1.place(x=150,y=30)

    def Execptional_handling_in_deletingbooks(self):
        BookId = self.BID_entry1.get()

        if BookId == '' :
            messagebox.showerror('Error', 'please fill all the box')
        else:
            try:
                BookId = int(BookId)

            except Exception:
                messagebox.showerror('Warning!', "Don't use letters in BookId ")
    def DELETE_BOOKS(self):
        self.Execptional_handling_in_deletingbooks()
        db=sqlite3.connect("Database.db")
        db.execute("delete FROM Books where ID=?",(int(self.BID_entry1.get()),))
        db.commit()
        db.close()
        messagebox.showinfo("Info","Book Deleted")
        self.BID_entry1.delete(0,"end")


class BOOKS_TO_BE_RETURNED:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x600+0+0")
        self.root.configure(background='cadet blue')
        db = sqlite3.connect("Database.db")
        cursor = db.execute("select * from Transactions where Returndate='Not Returned'")
        records = cursor.fetchall()

        MainFrame = Frame(self.root)
        MainFrame.pack()

        TitFrame = Frame(MainFrame, padx=5, pady=5, bd=5, relief=RIDGE)
        TitFrame.pack(side=TOP)
        self.labelTit = Label(TitFrame, font=('arial', 20, 'bold'), text="Books to be returned!", )
        self.labelTit.grid()

        savedataframe = Frame(MainFrame, bd=10, width=400, padx=20, pady=80, height=400, relief=RIDGE, bg="pink")
        savedataframe.pack(side=BOTTOM)

        self.label = Listbox(savedataframe, width=40, font=('arial', 14,))
        self.label.pack(side=LEFT, fill=BOTH)
        scrollbar = Scrollbar(savedataframe)
        scrollbar.pack(side=RIGHT, fill=BOTH)
        self.label.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.label.yview)

        for row in records:
            bookname = self.BOOK_NAME(int(row[1]))
            customer_det = self.CUSTOMER_DETAILS(int(row[2]))
            customer_name = customer_det[0]
            phone_no = customer_det[1]
            self.label.insert("end", bookname + "---" + customer_name + "---" + phone_no)
        db.close()

        self.root.mainloop()

    def BOOK_NAME(self, ID):
        db = sqlite3.connect("Database.db")
        db.execute("create table if not exists Books(ID int primary key,Name varchar(40),Publication varchar(40),Quantity int)")
        cursor = db.execute("select * from Books where ID=?", (ID,))
        records = cursor.fetchall()
        book_name = records[0][1]
        db.close()
        return book_name

    def CUSTOMER_DETAILS(self, ID):
        db = sqlite3.connect("Database.db")
        cursor = db.execute("select * from Customers where ID=?", (ID,))
        records = cursor.fetchall()
        print(records)
        customer_name = records[0][1]
        phone_no = records[0][2]
        db.close()
        return (customer_name, phone_no)



class library():
    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x600+0+0")
        self.root.title("Library Management System")
        self.root.configure(background='cadet blue')
        MainFrame = Frame(self.root)
        MainFrame.pack()
        TitFrame = Frame(MainFrame, padx=5, pady=5, bd=5, relief=RIDGE,)
        TitFrame.pack(side=TOP)
        labelTit = Label(TitFrame, font=('arial', 20, 'bold'), text="Library Management System!", )
        labelTit.grid()
        DataFrame = Frame(MainFrame, bd=12, width=600, height=500, padx=10, pady=10, relief=RIDGE, bg="pink")
        DataFrame.pack(side=TOP)

        self.adding_book_button1 = Button(DataFrame, text="Add Book", command=ADDING_BOOKS, bd=10,font=("arial", 12, ))
        self.adding_book_button1.place(x=30, y=60)
        self.adding_customers_button2 = Button(DataFrame, text="Add customer",
                                               command=ADDING_CUSTOMERS, bd=10,font=("arial", 12, ))
        self.adding_customers_button2.place(x=30, y=140)
        self.book_issue_button3 = Button(DataFrame, text="Issue Book", command=BOOKS_ISSUE, bd=10,font=("arial", 12, ))
        self.book_issue_button3.place(x=30, y=220)
        self.book_return_button4 = Button(DataFrame, text="Return Book",
                                          command=BOOKS_RETURN, bd=10,font=("arial", 12, ))
        self.book_return_button4.place(x=30, y=300)
        self.book_delete_button5 = Button(DataFrame, text="Delete Book", command=BOOKS_DELETE, bd=10,font=("arial", 12))
        self.book_delete_button5.place(x=30, y=380)
        self.books_return_button6 = Button(DataFrame, text="Books to be returned",
                                           command=BOOKS_TO_BE_RETURNED, bd=10,font=("arial", 12, ))
        self.books_return_button6.place(x=300, y=380)
        self.root.mainloop()
object=library()




