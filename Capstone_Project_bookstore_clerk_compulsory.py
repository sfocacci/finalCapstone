import sqlite3

#create a database called ebookstore
try:
    db = sqlite3.connect('ebookstore_db')
    cursor = db.cursor()
    # create a new table if one has not previously been made
    cursor.execute('''CREATE TABLE IF NOT EXISTS books(
        ID VARCHAR(4) PRIMARY KEY NOT NULL, 
        TITLE VARCHAR(25) NOT NULL, 
        AUTHOR VARCHAR(15), 
        QTY INTEGER(2))
        ''')
    db.commit #commit the action so not lost

# if the database is not found then display an error using error function
except Exception as error:
    db.rollback()
    raise error
finally:
    db.close #close the database

##########################################################################################################################################
###DEFINING FUNCTIONS

#function to add a ebook
def add_book():

    #get user input: id, title, author, qty
    id = input('Enter new book ID:\n').lower()
    title = input('Enter new book title:\n').lower()
    author = input("Enter book author:\n").lower()
    qty = int(input(f'How many copies of {title} are available?:\n'))
    # new information is then commited to the database using sqlite3 INSERT
    # the values are taken from the previously input data.
    cursor.execute('''INSERT INTO books(ID,TITLE,AUTHOR,QTY)
    VALUES(?,?,?,?)''',(id,title,author,qty))
    db.commit() #commit so changes are not lost

    # confirm book entry to user
    return print(f"\n- Book {id}, {title} has been added successfully! -\n")

#function to update ebook information
#allows change of field for value stored about each ebook
def update_info():
    
    # identify eBook that requires updated  information
    book_to_modify = input(
        "Please enter the book ID you wish to update.\nBook ID: ").lower()
    
    # identify field that needs an update
    field_not_chosen = True
    while field_not_chosen:
        field_to_update = input("\nEnter field that requires an update.\n"
            +"id - Update ID code.\n"
            +"title - to change a books title.\n"
            +"author - to change the Author.\n"
            +"qty - to update stock quantities.\n"
            +"Field to update is: "
            ).lower()

        # after a field has been selected the user is asked for 
        # the new information and the book is updated using UPDATE
        if field_to_update == 'id':
            updated_value = input(
                "Enter a new ID:\n")
            cursor.execute(
                '''UPDATE books SET ID = ? WHERE ID = ?''',
                (updated_value,book_to_modify,))#write to table
            db.commit #commit changes
            field_not_chosen = False #exit while loop

        elif field_to_update == 'title':
            updated_value = input(
                "Enter updated book title:\n")
            cursor.execute('''UPDATE books SET TITLE = ? WHERE ID = ?''',
            (updated_value,book_to_modify,))#write to table
            db.commit
            field_not_chosen = False #exit while loop

        elif field_to_update == 'author':
            updated_value = input(
                "Enter updated author name:\n")
            cursor.execute('''UPDATE books SET AUTHOR = ? WHERE ID = ?''',
            (updated_value,book_to_modify,))#write to table
            db.commit
            field_not_chosen = False #exit while loop

        elif field_to_update == 'qty':
            updated_value = input(
                "Enter new value for updated quantitiy:\n")
            cursor.execute('''UPDATE books SET QTY = ? WHERE ID = ?''',
            (updated_value,book_to_modify)) #write to table

            db.commit # commit so changes are not lost
            field_not_chosen = False #exit while loop

        # mistake code; ask user for correct input
        else:
            print("Sorry, input not understood. Try again...")

    # confirm updated information to user
    return print("\n - You have succeffully updated your book! - \n")
        

# define function to remove entry from table
def delete_book():

    # Identify the ebook user would like to delete
    id_not_chosen = True
    while id_not_chosen:
        id_to_delete = input(
            "Enter book ID you wish to delete.\n").lower()
        
        cursor.execute(
            '''SELECT ID,TITLE,AUTHOR,QTY FROM books WHERE ID = ?''',
            (id_to_delete,)) #write to table
         
        # delete entry using prepared book_id info
        cursor.execute('''DELETE FROM books WHERE ID = ?''',(id_to_delete,)) #delete from table
        # commit the update
        db.commit
        # confim success to user
        return print(f"\n- You have successfully deleted Book ID {id_to_delete}! -\n")

#define function to search for book
def search_book():
    # user is first ask how they wish to search the database
    id_not_chosen = True
    while id_not_chosen == True:
        id = input(
        "Please enter the book ID you would like to search for.\n").upper()
    
        cursor.execute(
            '''SELECT ID,TITLE,AUTHOR,QTY FROM books WHERE ID = ?'''
            ,(id,))
        # the infomation is saved in book
        book = cursor.fetchall()
        print(book)
        id_not_chosen = False

    else:
        print("ID not recognised. Try again") #error messgae if ID doesn't exist
        id_not_chosen = True
    

#==========Main Menu=============

#Insert books into  table
cursor = db.cursor()

#create python variables to store programmer data
#book 1
id1 = "3001"
title1 = "A Tale of Two Cities"
author1 = "Charles Dickens"
qty1 = 30

#book 2
id2 = "3002"
title2 = "Harry Potter and the Philosopher's Stone"
author2 = "J. K. Rowling"
qty2 = 40

#book 3
id3 = "3003"
title3 = "The Lion the Witch and the Wardrobe"
author3 = "C. S. Lewis"
qty3 = 25

#book 4
id4 = "3004"
title4 = "The Lord of The Rings"
author4 = "J. R. R. Tolkien"
qty4 = 37

#book 5
id5 = "3005"
title5 = "Alice in Wonderland"
author5 = "Lewis Carrol"
qty5 = 12



#Insert programmer 1
cursor.execute('''INSERT INTO books(id, title , author, qty)
               VALUES(?,?,?,?)''', (id1, title1, author1, qty1 ))
print('Book 1 inserted into table.')

#Insert programmer 2
cursor.execute('''INSERT INTO books(id, title , author, qty)
               VALUES(?,?,?,?)''', (id2, title2, author2, qty2 ))
print('Book 2 inserted into table.')

#Insert programmer 3
cursor.execute('''INSERT INTO books(id, title , author, qty)
               VALUES(?,?,?,?)''', (id3, title3, author3, qty3 ))
print('Book 3 inserted into table.')

#Insert programmer 3
cursor.execute('''INSERT INTO books(id, title , author, qty)
               VALUES(?,?,?,?)''', (id4, title4, author4, qty4 ))
print('Book 4 inserted into table.')

#Insert programmer 3
cursor.execute('''INSERT INTO books(id, title , author, qty)
               VALUES(?,?,?,?)''', (id5, title5, author5, qty5))
print('Book 5 inserted into table.')

db.commit()

username_needed = True

#define LOGIN loop
while username_needed:
    username = input("Please enter your username:\nUsername: ")
    print(f'Hello {username}!') #confirm user login
    username_needed = False


# once login sequence has been completed the menu is presented to the user
while username_needed == False:
    menu = input('''Select from the menu below:
    add - Add new book
    update - Update a book field
    search - Search for an book
    delete - Delete a book
    exit - Exit
    Type Selection here: ''').lower()

    if menu == "add":
        add_book()

    elif menu == "update":
        update_info()
    
    elif menu == "search":
        search_book()

    elif menu == "delete":
        delete_book()
    
    elif menu == "exit":
        print("Thank you. Goodbye!")
        exit()

    else:
        print("\n- Menu option not recognised,Try again. -")