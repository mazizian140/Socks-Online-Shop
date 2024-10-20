import tkinter as tk
def main():
    window = tk.Tk()
    window.title("Great Socks")
    window.geometry("800x600")

    # Create a LABLE
    lblTitle = tk.Label(text="Socks for You")
    lblTitle.grid(column=0, row=0)

    lalAction = tk.Label(text="No Action taken")
    lalAction.grid(column=1,row=0)

    lalFN = tk.Label(text="Enter your First Name")
    lalFN.grid(column=0,row=1)

    #Create an Entry box
    firstName =tk.StringVar()  # This is the string's Variable name
    fNameEntry = tk.Entry( window, width=25,textvariable=firstName)
    fNameEntry.grid(column=0, row=2)
    
    lalLN = tk.Label(text="Enter your Last Name")
    lalLN.grid(column=0,row=3)

    lastName =tk.StringVar()  # This is the string's Variable name
    lNameEntry = tk.Entry( window, width=25,textvariable=lastName)
    lNameEntry.grid(column=0, row=4)

    lalWool = tk.Label(text="What type of wool do you want?")
    lalWool.grid(column=0,row=5)

    #Do a radio button for the Wool
    radWoolSelected = tk.IntVar()
    rad1 = tk.Radiobutton(window,text='Cashmere', value=1, variable=radWoolSelected)
    rad2 = tk.Radiobutton(window,text='Angora',   value=2, variable=radWoolSelected)
    rad3 = tk.Radiobutton(window,text='Lopi',     value=3, variable=radWoolSelected)
    rad4 = tk.Radiobutton(window,text='Llama',    value=4, variable=radWoolSelected)

    rad1.grid(column=1,row=5)
    rad2.grid(column=2,row=5)
    rad3.grid(column=3,row=5)
    rad4.grid(column=4,row=5)

    lalSize = tk.Label(text="What size do you want?")
    lalSize.grid(column=0,row=6)

    #Do a radio button for the Size
    radSizeSelected = tk.IntVar()
    radS1 = tk.Radiobutton(window,text='Small',  value=1, variable=radSizeSelected)
    radS2 = tk.Radiobutton(window,text='Medium', value=2, variable=radSizeSelected)
    radS3 = tk.Radiobutton(window,text='Large',  value=3, variable=radSizeSelected)
    radS1.grid(column=1,row=6)
    radS2.grid(column=2,row=6)
    radS3.grid(column=3,row=6)
    
    #an entry for the number of socks you want.
    labQuantity = tk.Label(text="What quantity do you want?")
    labQuantity.grid(column=0,row=7)
    
    quantity = tk.IntVar()
    quantityEntry = tk.Entry( window, width=10, textvariable=quantity)
    quantityEntry.grid(column=1, row=7)
    
    lalForDB = tk.Label(text="Do you want to add this to the Database?")
    lalForDB.grid(column=0,row=8)


    
    def clicked():
        # the varibles needed
        lName = lastName.get()
        fName = firstName.get()
        #This are numbers
        wool = radWoolSelected.get()
        size = radSizeSelected.get()
        quant = quantity.get()

        mydb = getConnection()
        mycursor = mydb.cursor()
        # Do not need ID_number in Database, it is auto_increment.
        sql = "INSERT INTO SOCKS (CustomerFirstName,CustomerLastName,TypeOfWool,SockSize,SockQuantity) VALUES (%s, %s,%s, %s, %s)"
        values=(fName, lName, wool, size, quant)
        mycursor.execute(sql,values)
        mydb.commit()
        #close the connection.
        mydb.close()
        lalAction['text'] = 'Database Updated.'
        clear()
        
    def getConnection() :
        # This function is used to get a connection to the Database BEST_SOCKS
        import mysql.connector
        #use your own user and passwd
        mydb = mysql.connector.connect(
        host="localhost",
        user="sam",
        passwd="sesame",
        auth_plugin="mysql_native_password",
        database="BEST_SOCKS"
        )
        return mydb
    
    def clear():
        #clear items
        fNameEntry.delete(first=0, last=27)
        lNameEntry.delete(first=0, last=27)
        quantityEntry.delete(first=0, last=12)
        # set radiobutton to 0 to deselect
        radWoolSelected.set(0)
        radSizeSelected.set(0) 

    btn1 = tk.Button(window, text="Add to DB", command=clicked)
    btn1.grid(column=0, row=9)

    btn2 = tk.Button(window, text="Clear Items", command=clear)
    btn2.grid(column=1, row=9)
    window.mainloop()
main()
