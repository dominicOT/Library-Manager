import csv
import tkinter as tk
from tkinter import messagebox

def add_book():
    book_id = book_id_entry.get()
    book_title = book_title_entry.get()
    book_author = book_author_entry.get()
    
    # Verify Input
    if not book_id or not book_title or not book_author:
        messagebox.showerror("Error", "Please fill all the fields!")
        return  # Exit the function if input is incomplete

    # Open CSV file in append mode
    with open("LibraryData.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([book_id, book_title, book_author, "Available"])  # Add "Available" status

    messagebox.showinfo("Success", "Book added successfully!")
    book_id_entry.delete(0, tk.END)
    book_title_entry.delete(0, tk.END)
    book_author_entry.delete(0, tk.END)


def search_book():
    search_value = search_entry.get()
    found = False
    with open("LibraryData.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if search_value.lower() in (row[0].lower(), row[1].lower(), row[2].lower()):  # Case-insensitive search
                messagebox.showinfo("Book Details", f"Book ID: {row[0]}\nTitle: {row[1]}\nAuthor: {row[2]}\nStatus: {row[3]}")
                found = True
                break  # Stop searching after a match

    if not found:
        messagebox.showerror("Error", "Book not found!")

    search_entry.delete(0, tk.END)


def delete_book():
    book_id = book_id_entry.get()
    book_title = book_title_entry.get()

    if not book_id or not book_title:
        messagebox.showerror("Error", "Please fill all the fields!")
        return

    updated_rows = []
    book_deleted = False

    with open("LibraryData.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == book_id and row[1] == book_title:
                book_deleted = True  
            else:
                updated_rows.append(row)

    if book_deleted:
        with open("LibraryData.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(updated_rows)
        messagebox.showinfo("Success", "Book deleted successfully!")
    else:
        messagebox.showerror("Error", "Book not found!")

    book_id_entry.delete(0, tk.END)
    book_title_entry.delete(0, tk.END)


def lend_book():
    book_id = book_id_entry.get()
    borrower_name = borrower_entry.get()

    if not book_id or not borrower_name:
        messagebox.showerror("Error", "Please enter Book ID and Borrower's Name!")
        return

    updated_rows = []
    book_found = False

    with open("LibraryData.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == book_id:
                if row[3] == "Available":
                    row[3] = f"Lent to {borrower_name}"
                    book_found = True
                else:
                    messagebox.showerror("Error", "Book is already lent!")
                    return
            updated_rows.append(row)

    if book_found:
        with open("LibraryData.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(updated_rows)
        messagebox.showinfo("Success", "Book lent successfully!")
    else:
        messagebox.showerror("Error", "Book not found!")

    book_id_entry.delete(0, tk.END)
    borrower_entry.delete(0, tk.END)


# GUI
root = tk.Tk()
root.title("Library Management System")
root.geometry("600x400")
root.configure(bg="white")

# Add menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

book_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Menu", menu=book_menu)
book_menu.add_command(label="Add Book", command=add_book)
book_menu.add_command(label="Delete Book", command=delete_book)
book_menu.add_command(label="Lend Book", command=lend_book)

font_settings = ("Helvetica", 14)


tk.Label(root, text="Book ID:", bg="white", font=font_settings).grid(row=0, column=0, padx=10, pady=10)
book_id_entry = tk.Entry(root, font=font_settings)
book_id_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Book Title:", bg="white", font=font_settings).grid(row=1, column=0, padx=10, pady=10)
book_title_entry = tk.Entry(root, font=font_settings)
book_title_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Book Author:", bg="white", font=font_settings).grid(row=2, column=0, padx=10, pady=10)
book_author_entry = tk.Entry(root, font=font_settings)
book_author_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Borrower's Name:", bg="white", font=font_settings).grid(row=3, column=0, padx=10, pady=10)
borrower_entry = tk.Entry(root, font=font_settings)
borrower_entry.grid(row=3, column=1, padx=10, pady=10)

tk.Button(root, text="Add Book", command=add_book, font=font_settings).grid(row=4, column=0, columnspan=2, pady=20)

tk.Label(root, text="Search Book:", bg="white", font=font_settings).grid(row=5, column=0, padx=10, pady=10)
search_entry = tk.Entry(root, font=font_settings)
search_entry.grid(row=5, column=1, padx=10, pady=10)

tk.Button(root, text="Search", command=search_book, font=font_settings).grid(row=6, column=0, columnspan=2, pady=20)

root.mainloop()
