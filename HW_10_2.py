class Book:
    def __init__(self, title: str, author, pages: int, rating: float):
        self._title = title
        self._author = author
        self._pages = pages
        self._rating = rating

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def pages(self):
        return self._pages

    @property
    def rating(self):
        return self._rating

    def get_info(self):
        return f"'{self.title}' by {self.author.name}, {self.pages} pages of {self.rating} rating"


class FictionBook(Book):
    def __init__(self, title: str, author, pages: int, rating: float):
        super().__init__(title, author, pages, rating)

    def get_info(self):
        return f"'{self.title}' by {self.author.name}, {self.pages} pages"


class NonFictionBook(Book):
    def __init__(self, title: str, author, pages: int, rating: float):
        super().__init__(title, author, pages, rating)

    def get_info(self):
        return f"'{self.title}' by {self.author.name}, {self.pages} pages"


class Author:
    def __init__(self, name: str, surname: str, country: str, birth_year: int):
        self._name = name
        self._surname = surname
        self._country = country
        self._birth_year = birth_year
        self._books = []

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def country(self):
        return self._country

    @property
    def birth_year(self):
        return self._birth_year

    @property
    def books(self):
        return self._books

    def add_book(self, book):
        self._books.append(book)

    def get_books(self):
        return self._books

    def get_info(self):
        return f"{self.name}, born in {self.birth_year}, books: {[book.title for book in self.books]}"


def main():
    authors = {}
    books = []

    while True:
        print("\n1. Add Author")
        print("2. Add Fiction Book")
        print("3. Add Non-Fiction Book")
        print("4. List Authors")
        print("5. List Books")
        print("6. Exit")
        choice = input("Enter your choice: ")
        #name: str, surname: str, country: str, birth_year: int
        if choice == "1":
            name = input("Enter author name: ")
            surname = input("Enter author surname: ")
            country = input("Enter author country: ")
            birth_year = int(input("Enter author birth year: "))
            if name not in authors:
                authors[name] = Author(name, surname, country, birth_year)
                print(f"Author '{name}' added.")
            else:
                print(f"Author '{name}' already exists.")

        elif choice == "2":
            title = input("Enter book title: ")
            author_name = input("Enter author name: ")
            if author_name in authors:
                pages = int(input("Enter number of pages: "))
                rating = float(input("Enter rating: "))
                book = FictionBook(title, authors[author_name], pages, rating)
                authors[author_name].add_book(book)
                books.append(book)
                print(f"Fiction Book '{title}' by {author_name} added.")
            else:
                print(f"Author '{author_name}' does not exist. Please add the author first.")

        elif choice == "3":
            title = input("Enter book title: ")
            author_name = input("Enter author name: ")
            if author_name in authors:
                pages = int(input("Enter number of pages: "))
                rating = float(input("Enter rating: "))
                book = NonFictionBook(title, authors[author_name], pages, rating)
                authors[author_name].add_book(book)
                books.append(book)
                print(f"Non-Fiction Book '{title}' by {author_name} added.")
            else:
                print(f"Author '{author_name}' does not exist. Please add the author first.")

        elif choice == "4":
            if authors:
                for author in authors.values():
                    print(author.get_info())
            else:
                print("No authors available.")

        elif choice == "5":
            if books:
                for book in books:
                    print(book.get_info())
            else:
                print("No books available.")

        elif choice == "6":
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
