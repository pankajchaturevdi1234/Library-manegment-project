# Library Management System in Python

# Book class to hold book information
class Book:
    def __init__(self, title, author, available_copies):
        self.title = title
        self.author = author
        self.available_copies = available_copies

# Pre-added users
users = {
    "pankajchaturvedi": "password1",
    "sachinsharma": "password2",
    "navneetyadav": "password3",
    "sagardixit": "password4"
}

# Function to check if a user is valid
def is_valid_user(username, password):
    return users.get(username) == password

# Function to list available books
def list_books(books):
    print("\nAvailable Books:")
    for i, book in enumerate(books, start=1):
        print(f"{i}. {book.title} by {book.author} ({book.available_copies} available)")

# Function to borrow a book
def borrow_book(books):
    list_books(books)
    try:
        book_index = int(input("Enter the number of the book you want to borrow: ")) - 1
        if 0 <= book_index < len(books):
            if books[book_index].available_copies > 0:
                books[book_index].available_copies -= 1
                print(f"You have successfully borrowed {books[book_index].title}.")
            else:
                print("Sorry, this book is currently unavailable.")
        else:
            print("Invalid book choice. Please try again.")
    except ValueError:
        print("Please enter a valid number.")

# Function to add a new book
def add_book(books):
    title = input("Enter the title of the new book: ")
    author = input("Enter the author of the new book: ")
    try:
        available_copies = int(input("Enter the number of copies available: "))
        new_book = Book(title, author, available_copies)
        books.append(new_book)
        print("The book has been successfully added to the library.")
    except ValueError:
        print("Please enter a valid number for copies.")

# Function to add a new user
def add_user(users):
    new_username = input("Enter the new username: ")
    new_password = input("Enter the new password: ")
    users[new_username] = new_password
    print("The new user has been successfully added.")

# Main function
def main():
    # Pre-added books
    books = [
        Book("Think and Grow Rich", "Napoleon Hill", 5),
        Book("Rich Dad Poor Dad", "Robert Kiyosaki", 3),
        Book("The Intelligent Investor", "Benjamin Graham", 2),
        Book("The Power of Positive Thinking", "Norman Vincent Peale", 4),
        Book("Atomic Habits", "James Clear", 1),
    ]

    # User login
    while True:
        print("**********Login to access the library functions**********")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if is_valid_user(username, password):
            print(f"-------- Login successful! Welcome, {username}! --------")
            break
        else:
            print("Login failed. Please check your username and password.")

    # Menu for library management
    while True:
        print("\nLibrary Management System")
        print("1. List Books")
        print("2. Borrow a Book")
        print("3. Add a Book")
        print("4. Add a User")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                list_books(books)
            elif choice == 2:
                borrow_book(books)
            elif choice == 3:
                add_book(books)
            elif choice == 4:
                add_user(users)
            elif choice == 5:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
