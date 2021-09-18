from tkinter import *
import sqlite3

root = Tk()
# root.title = 'Using Databases'
root.geometry('400x500')

# Create Table
"""
c.execute('''CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
    )''')
"""
# Create function for sunmitting database
def submit():
# Create a database or connect to database
    conn = sqlite3.connect('Address_book.db')

# Create cursor
    c = conn.cursor()

# Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
        {
            'f_name': f_name.get(),
            'l_name': l_name.get(),
            'address': address.get(),
            'city': city.get(),
            'state': state.get(),
            'zipcode': zipcode.get()
        })

# Commit changes
    conn.commit()

# Close Connection
    conn.close()

    # Clear the text box
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

def query():
# Create a database or connect to database
    conn = sqlite3.connect('Address_book.db')

# Create cursor
    c = conn.cursor()

# Query Database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()

    # Loop through records
    print_records = ''
    for record in records:
        print_records += f"{str(record[6])} Name: {str(record[0])} {str(record[1])}\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

# Commit changes
    conn.commit()

# Close Connection
    conn.close()

# Create function to deelte a record
def delete():
    conn = sqlite3.connect('Address_book.db')
    c = conn.cursor()
    c.execute(f'DELETE from addresses WHERE oid = {delete_box.get()}')

    conn.commit()
    conn.close()

def update():
    conn = sqlite3.connect('Address_book.db')
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("""UPDATE addresses SET
        first_name = :first,
        last_name= :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode

        WHERE oid = :oid""",
        {
            'first': f_name_editor.get(),
            'last': l_name_editor.get(),
            'address': address_editor.get(),
            'city': city_editor.get(),
            'state': state_editor.get(),
            'zipcode': zipcode_editor.get(),
            'oid':record_id
        })

    conn.commit()
    conn.close()
    editor.destroy()

def edit():
    global editor
    editor = Tk()
    editor.title('Update Record')
    editor.geometry('400x300')

# Create a database or connect to database
    conn = sqlite3.connect('Address_book.db')

# Create cursor
    c = conn.cursor()

    record_id = delete_box.get()
# Query Database
    c.execute(f"SELECT * FROM addresses WHERE oid = {record_id}")
    records = c.fetchall()

    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10,0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1, padx=20)

# Create text box label
    f_name_label = Label(editor, text='First Name')
    f_name_label.grid(row=0, column=0, pady=(10,0))
    l_name_label = Label(editor, text='Last Name')
    l_name_label.grid(row=1, column=0)
    address_label = Label(editor, text='Address')
    address_label.grid(row=2, column=0)
    city_label = Label(editor, text='City')
    city_label.grid(row=3, column=0)
    state_label = Label(editor, text='State')
    state_label.grid(row=4, column=0)
    zipcode_label = Label(editor, text='Zipcode')
    zipcode_label.grid(row=5, column=0)

    # Create a Save button to save record
    edit_btn = Button(editor, text='Save Record', command=update)
    edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

    # Loop through result
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    conn.close()


f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10,0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)
state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

# Create text box label
f_name_label = Label(root, text='First Name')
f_name_label.grid(row=0, column=0, pady=(10,0))
l_name_label = Label(root, text='Last Name')
l_name_label.grid(row=1, column=0)
address_label = Label(root, text='Address')
address_label.grid(row=2, column=0)
city_label = Label(root, text='City')
city_label.grid(row=3, column=0)
state_label = Label(root, text='State')
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text='Zipcode')
zipcode_label.grid(row=5, column=0)
delete_box_label = Label(root, text='Select ID:')
delete_box_label.grid(row=9, column=0, pady=5)

# Create submit Button
submit_button = Button(root, text="Add Record To Database",command=submit)
submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

query_btn = Button(root, text='Show Records', command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=127)

# Create a delete Button
delete_btn = Button(root, text='Delete a Record', command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=124)

# Create a update button
update_btn = Button(root, text='Edit Record', command=edit)
update_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=134)

mainloop()

