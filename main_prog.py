
class Library:

    def __init__(self, list, name):
        self.book_list = list
        self.name = name
        self.lend_dict = {}

    def display_books(self):
        print(f"We have the following books in our library: {self.name}")
        for books in self.book_list:
            print(books)

    def lend_books(self, user, books):
        if books not in self.lend_dict.keys():
            self.lend_dict.update({books: user})
            print("Books database has been updated. You can take your book now.")
        else:
            print(f"Book is already issued by {self.lend_dict[books]}")

    def return_books(self, books):
        self.lend_dict.pop(books)
        print("Book has been removed from the book list.")

    def add_books(self, books):
        self.book_list.append(books)
        print("Book has been added to the book list.")


if __name__ == '__main__':
    moody = Library(['Atomic Habits', 'The Psychology of Money', 'To Kill a Mockingbird', 'Genuine Fraud'], 'Moody')

    while(True):
        print(f"Welcome to {moody.name} library. Select the following options to continue.")
        print("1. Display the books.")
        print("2. Lend a book.")
        print("3. Return a book")
        print("4. Add a book.")

        user_choice = int(input("Enter your choice number: "))

        if user_choice==1:
            moody.display_books()
        elif user_choice==2:
            books = input("Enter the name of the book you want to lend: ")
            user = input("Enter your name: ")
            moody.lend_books(user, books)
        elif user_choice==3:
            books = input("Enter the name of the book you want to return: ")
            moody.return_books(books)
        elif user_choice==4:
            books = input("Enter the name of the book you want to add: ")
            moody.add_books(books)
        else:
            print("Enter a valid number from the options given above.")

        print("Press 'q' to quit and 'c' to continue")
        user_choice2 = ""
        while (user_choice2 != 'q' and user_choice2 != 'c'):
            user_choice2 = input("Press to quit or continue: ")
            if user_choice2 == 'q':
                exit()
            elif user_choice2 == 'c':
                continue