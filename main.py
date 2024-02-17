import csv
from tkinter import *
from tkinter import messagebox

# Function to add a book to the library
def add_book():
    # Get the values from the entry boxes
    book_id = book_id_entry.get()
    book_title = book_title_entry.get()
    book_author = book_author_entry.get()
    
    # Check if any field is empty
    if book_id == "" or book_title == "" or book_author == "":
        messagebox.showerror("Error", "Please fill all the fields!")
    else:
        # Open the CSV file in append mode
        with open("library.csv", "a") as file:
            writer = csv.writer(file)
            # Write the values to the file
            writer.writerow([book_id, book_title, book_author])
        # Show a success message
        messagebox.showinfo("Success", "Book added successfully!")
        # Clear the entry boxes
        book_id_entry.delete(0, END)
        book_title_entry.delete(0, END)
        book_author_entry.delete(0, END)

# Function to search for a book
def search_book():
    # Get the value to search from the entry box
    search_value = search_entry.get()
    
    # Open the CSV file in read mode
    with open("library.csv", "r") as file:
        reader = csv.reader(file)
        # Loop through the rows in the file
        for row in reader:
            # If the search value matches any of the fields
            if search_value in row:
                # Show the book details in a message box
                messagebox.showinfo("Book Details", f"Book ID: {row[0]}\nTitle: {row[1]}\nAuthor: {row[2]}")
                # Clear the search entry box
                search_entry.delete(0, END)
                return
        # If no match was found, show an error message
        messagebox.showerror("Error", "Book not found!")
        # Clear the search entry box
        search_entry.delete(0, END)

# Create the GUI
root = Tk()
root.title("Library Management System")

# Create the labels and entry boxes
Label(root, text="Book ID:").grid(row=0, column=0)
book_id_entry = Entry(root)
book_id_entry.grid(row=0, column=1)

Label(root, text="Title:").grid(row=1, column=0)
book_title_entry = Entry(root)
book_title_entry.grid(row=1, column=1)

Label(root, text="Author:").grid(row=2, column=0)
book_author_entry = Entry(root)
book_author_entry.grid(row=2, column=1)

Label(root, text="Search:").grid(row=3, column=0)
search_entry = Entry(root)
search_entry.grid(row=3, column=1)

# Create the buttons
add_button = Button(root, text="Add Book", command=add_book)
add_button.grid(row=4, column=0)

search_button = Button(root, text="Search Book", command=search_book)
search_button.grid(row=4, column=1)

root.mainloop()
