import os

books = []


# ----------------------------
# Load Books from File
# ----------------------------
def load_books():
    if os.path.exists("books.txt"):
        with open("books.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")

                if len(data) == 3:
                    books.append({
                        "id": data[0],
                        "title": data[1],
                        "author": data[2]
                    })


# ----------------------------
# Save Books to File
# ----------------------------
def save_books():
    with open("books.txt", "w") as file:
        for book in books:
            file.write(f"{book['id']},{book['title']},{book['author']}\n")


load_books()


while True:

    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # ----------------------------
    # Add Book
    # ----------------------------
    if choice == "1":

        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        books.append({
            "id": book_id,
            "title": title,
            "author": author
        })

        save_books()

        print("Book Added Successfully!")

    # ----------------------------
    # View Books
    # ----------------------------
    elif choice == "2":

        if len(books) == 0:
            print("No books available.")

        else:

            print("\n===== Book List =====")

            for book in books:

                print("----------------------")
                print("Book ID :", book["id"])
                print("Title   :", book["title"])
                print("Author  :", book["author"])

    # ----------------------------
    # Search Book
    # ----------------------------
    elif choice == "3":

        search_id = input("Enter Book ID: ")

        found = False

        for book in books:

            if book["id"] == search_id:

                print("\nBook Found")
                print("Book ID :", book["id"])
                print("Title   :", book["title"])
                print("Author  :", book["author"])

                found = True
                break

        if not found:
            print("Book not found.")

    # ----------------------------
    # Update Book
    # ----------------------------
    elif choice == "4":

        update_id = input("Enter Book ID to Update: ")

        found = False

        for book in books:

            if book["id"] == update_id:

                book["title"] = input("Enter New Title: ")
                book["author"] = input("Enter New Author: ")

                save_books()

                print("Book Updated Successfully!")

                found = True
                break

        if not found:
            print("Book not found.")

    # ----------------------------
    # Delete Book
    # ----------------------------
    elif choice == "5":

        delete_id = input("Enter Book ID to Delete: ")

        found = False

        for book in books:

            if book["id"] == delete_id:

                books.remove(book)

                save_books()

                print("Book Deleted Successfully!")

                found = True
                break

        if not found:
            print("Book not found.")

    # ----------------------------
    # Exit
    # ----------------------------
    elif choice == "6":

        print("Thank You!")
        break

    else:
        print("Invalid Choice.")