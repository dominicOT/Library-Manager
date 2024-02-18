import csv
from tkinter import *
from tkinter import messagebox


def add_book():
    book_id = book_id_entry.get()
    book_title = book_title_entry.get()
    book_author = book_author_entry.get()
    
    #VERIFY INPUT
    if not book_id or not book_title or not book_author:
        messagebox.showerror("Error", "Please fill all the fields!")
    else:
        #Open CSV file in append mode
        with open("library.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([book_id, book_title, book_author])
        messagebox.showinfo("Success", "Book added successfully!")
        book_id_entry.delete(0, END)
        book_title_entry.delete(0, END)
        book_author_entry.delete(0, END)

#search for book
def search_book():
    search_value = search_entry.get()
    with open("library.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if search_value in row:
                messagebox.showinfo("Book Details", f"Book ID: {row[0]}\nTitle: {row[1]}\nAuthor: {row[2]}")
                #clear search box
                search_entry.delete(0, END)
                return
#BOOK NOT FOUND
        messagebox.showerror("Error", "Book not found!")
        search_entry.delete(0, END)

#GUI
root = Tk()
root.title("Library Management System")
root.geometry("400x300")
root.configure(bg="white")

Label(root, text="Book ID:", bg="white").grid(row=0, column=0, padx=7, pady=7)
book_id_entry = Entry(root)
book_id_entry.grid(row=0, column=1, padx=7, pady=7)

Label(root, text="Book Title:", bg="white").grid(row=1, column=0, padx=7, pady=7)
book_title_entry = Entry(root)
book_title_entry.grid(row=1, column=1, padx=7, pady=7)

Label(root, text="Book Author:", bg="white").grid(row=2, column=0, padx=5, pady=5)
book_author_entry = Entry(root)
book_author_entry.grid(row=2, column=1, padx=5, pady=5)

Label(root, text="Search:", bg="white").grid(row=3, column=0, padx=5, pady=5)
search_entry = Entry(root)
search_entry.grid(row=3, column=1, padx=5, pady=5)

# Create the buttons
add_button = Button(root, text="Add Book", command=add_book, bg="blue", fg="white")
add_button.grid(row=4, column=0, padx=9, pady=9)

search_button = Button(root, text="Search Book", command=search_book, bg="blue", fg="white")
search_button.grid(row=4, column=1, padx=9, pady=9)

root.mainloop()
