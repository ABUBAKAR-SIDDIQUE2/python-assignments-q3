# Books will store here
library = []


def add_book():
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
        print("\nYour Library")
        for index, book in enumerate(library):
            print(f"{index + 1}, {book['title']} by {book['author']} ({book['publication_year']}) - {book['genre']} - {book['read_status']}")


def search_book():

    if not library:
        print("The library is empty, No books to search. \n")
        return

    while True:
        print("\nSearch by: ")
        print("1, Title")
        print("2, Author")
        print("3, EXIT")

        search_choice = int(input("\nEnter your choice: "))

        def title_search():
            title_search_input = input("\nEnter the title: ").lower()
            found = False

            for index, book in enumerate(library):
                if book["title"].lower() == title_search_input:
                    if not found:
                        print("\nMatching Books:")
                        found = True
                    print(f"{index + 1}. {book["title"]} by {book["author"]} ({book["publication_year"]}) - {book["genre"]} - {book["read_status"]}")
            if not found:
                print("\n Book not Found")

        def author_search():
            author_search_input = input("\nEnter the Author Name: ").lower()
            found = False

            for index, book in enumerate(library):
                if book["author"].lower() == author_search_input:
                    if not found:
                        print("\nMatching Books:")
                        found = True
                    print(f"{index + 1}. {book["title"]} by {book["author"]} ({book["publication_year"]}) - {book["genre"]} - {book["read_status"]}")
            if not found:
                print("\n Author not Found")

        if search_choice == 1:
            title_search()
        elif search_choice == 2:
            author_search()
        elif search_choice == 3:
            break
        else:
            print("\n Invalid choice, please try again! \n")


def display_statistics():

    if not library:
        print("\n The library is empty, No statistics to show! \n")
        
    else:
        total_books = len(library)
        read_books = sum(1 for book in library if book["read_status"])
        unread_books = total_books - read_books

        if total_books > 0:
            percentage_read_books = (read_books / total_books) * 100
        else: 
            percentage_read_books = 0

        print("\nLibrary Statistics: ")
        print(f"Total Books: {total_books}")
        print(f"Read Books: {read_books}")
        print(f"Unread Books: {unread_books}")
        print(f"Percentage Read: {percentage_read_books}")


def main():
    while True:
        print("\nWelcome to your personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display Statistics")
        print("6. EXIT \n")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_book()
        elif choice == 2:
            remove_book()
        elif choice == 3:
            search_book()
        elif choice == 4:
            view_books()
        elif choice == 5:
            display_statistics()
        elif choice == 6:
            print("Goodbye!")
            break
        else:
            print("Invalid choice, Please try again🙏")


if __name__ == "__main__":
    main()