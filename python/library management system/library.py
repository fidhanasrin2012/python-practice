books = []

while True:

    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = {
            "id": book_id,
            "title": title,
            "author": author
        }

        books.append(book)

        print("Book added successfully!")

    elif choice == "2":

        if len(books) == 0:
            print("No books available.")

        else:

            print("\n===== Book List =====")

            for book in books:

                print("Book ID :", book["id"])
                print("Title   :", book["title"])
                print("Author  :", book["author"])
                print("-------------------------")

    elif choice == "3":

        if len(books) == 0:

            print("No books available.")

        else:

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

    elif choice == "4":

        print("Thank you!")
        break

    else:

        print("Invalid choice.")