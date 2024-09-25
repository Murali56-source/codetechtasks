class Library:
    def __init__(self):
        self.books = {}
    
    def add_book(self, title, author):
        self.books[title] = {'author': author, 'available': True}
        print(f"Added book: '{title}' by {author}")

    def view_books(self):
        print("\nAvailable Books:")
        for title, info in self.books.items():
            status = "Available" if info['available'] else "Not Available"
            print(f"'{title}' by {info['author']} - {status}")

    def borrow_book(self, title):
        if title in self.books:
            if self.books[title]['available']:
                self.books[title]['available'] = False
                print(f"You have borrowed '{title}'.")
            else:
                print(f"Sorry, '{title}' is currently not available.")
        else:
            print(f"'{title}' does not exist in the library.")

    def return_book(self, title):
        if title in self.books:
            if not self.books[title]['available']:
                self.books[title]['available'] = True
                print(f"You have returned '{title}'.")
            else:
                print(f"'{title}' was not borrowed.")
        else:
            print(f"'{title}' does not exist in the library.")

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Enter the book title: ")
            author = input("Enter the author's name: ")
            library.add_book(title, author)
        elif choice == '2':
            library.view_books()
        elif choice == '3':
            title = input("Enter the title of the book you want to borrow: ")
            library.borrow_book(title)
        elif choice == '4':
            title = input("Enter the title of the book you want to return: ")
            library.return_book(title)
        elif choice == '5':
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
