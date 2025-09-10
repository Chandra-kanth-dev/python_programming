'''ou are building a Library Management System in Python. The system should store books in a dictionary where:
Key → Book ID
Value → Book Title
Write a Python program to perform the following operations using Dictionaries:
Add a book to the library (Book ID, Title).
Remove a book using Book ID.
Search for a book by Book ID and display the title.
Update the title of a book (e.g., correction in title).
Display all books in the library.
Count the total number of books in the library.
Check if a book title exists in the library (reverse lookup).'''
def add_book(book_id,titile,d):
    d[book_id]=titile
    
def remove_book(book_id,d):
    d.remove(book_id)
    
def search_print(d,key):
    if key in d.keys():
        print(key,"---->",d[key])
    else:
        print("not found")
def update_title(book_id,title,d):
    d[book_id]=title
def display_books(d):
    print(d)
def count_books(d):
    print(len(d))
def does_exists(d,title):
    print("the title exists in dictionary is",title in d.values())
d={
    "101":"python",
    "102":"java",
    "103":"c++"
}


while True:
    print("\n1. Add book\n2. Remove book\n3. Search book\n4. Update title\n5. Display all books\n6. Count books\n7. Check title exists\n8. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        add_book(book_id, title, d)
        print("Book added.")
    elif choice == 2:
        book_id = input("Enter Book ID to remove: ")
        remove_book(book_id, d)
    elif choice == 3:
        book_id = input("Enter Book ID to search: ")
        search_print(d, book_id)
    elif choice == 4:
        book_id = input("Enter Book ID to update: ")
        title = input("Enter new title: ")
        update_title(book_id, title, d)
    elif choice == 5:
        display_books(d)
    elif choice == 6:
        count_books(d)
    elif choice == 7:
        title = input("Enter title to check: ")
        does_exists(d, title)
    elif choice == 8:
        break
    else:
        print("Enter a valid choice.")
