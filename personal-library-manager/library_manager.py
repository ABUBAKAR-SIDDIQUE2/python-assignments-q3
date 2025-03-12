# Books will store here
library = []


def library_manager():
    print()
    title = input("Enter Book Title: ")
    author = input("Enter the Author name: ")
    publication_year = int(input("Enter the Publication Year: "))
    genre = input("Enter the Genre: ")
    read_status_input = input("Have you read the book? (yes/no): ").strip().lower()
    read_status = read_status_input == "yes"

    book = {
        "title": title,
        "author": author,
        "publication_year": publication_year,
        "genre": genre,
        "read_status": read_status
    }

    library.append(book)
    print(f"\n Book {title} added to library \n")


def remove_book():
    if not library:
        print("\n The library is empty, No books to remove! \n")
        return
    
    title_or_author_remove = input("Enter title or author to remove the book: ")

    for book in library:
        if book["title"].lower() == title_or_author_remove.lower() or book["author"].lower() == title_or_author_remove.lower():
            library.remove(book)
            print(f"Book {book["title"]} by {book["author"]} removed from library")
            return

    print(f"Title or Author \"{title_or_author_remove}\" not found in the library.")


def view_books():
    if not library:
        print("\n The library is empty! \n")

    else:
        print("\nLibrary Books\n")
        for index, book in enumerate(library):
            print(f"{index + 1}, {book['title']} | {book['author']} | {book['publication_year']} | {book['genre']} | Read {book['read_status']}")


def main():
    while True:
        print("Library Manager")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Display all books")
        print("4. EXIT \n")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            library_manager()
        elif choice == 2:
            remove_book()
        elif choice == 3:
            view_books()
        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice, Please try again🙏")


if __name__ == "__main__":
    main()