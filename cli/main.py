from library_manager.inventory import LibraryInventory
from library_manager.book import Book

def main():
    inventory = LibraryInventory()

    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                title = input("Title: ")
                author = input("Author: ")
                isbn = input("ISBN: ")
                book = Book(title, author, isbn)
                inventory.add_book(book)
                print("Book added successfully!")

            elif choice == "2":
                isbn = input("Enter ISBN to issue: ")
                books = inventory.search_by_isbn(isbn)
                if books:
                    if books[0].issue():
                        inventory.save_books()
                        print("Book issued successfully!")
                    else:
                        print("Book is already issued.")
                else:
                    print("Book not found.")

            elif choice == "3":
                isbn = input("Enter ISBN to return: ")
                books = inventory.search_by_isbn(isbn)
                if books:
                    books[0].return_book()
                    inventory.save_books()
                    print("Book returned successfully!")
                else:
                    print("Book not found.")

            elif choice == "4":
                for book in inventory.display_all():
                    print(book)

            elif choice == "5":
                term = input("Enter title or ISBN to search: ")
                results = inventory.search_by_title(term) + inventory.search_by_isbn(term)
                for book in results:
                    print(book)
                if not results:
                    print("No books found.")

            elif choice == "6":
                print("Exiting...")
                break

            else:
                print("Invalid choice. Try again.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
