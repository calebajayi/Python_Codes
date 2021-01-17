import sys


#   Create an instance of a ibrary to hold our items and users
class Library:
    # Define what is in the library
    def __init__(self):
        self._books = []
        self._periodicals = []
        self._users = []

#   Create functions
    def add_book(self, book):
        self._books.append(book)

    def add_user(self, user):
        self._users.append(user)

    def add_periodical(self, journal):
        self._periodicals.append(journal)

    def remove_book(self, book):
        self._books.remove(book)

    def remove_user(self, user):
        self._users.remove(user)

    def remove_periodical(self, journal):
        self._periodicals.remove(journal)

    def printbooks(self):
        print("The books we have in our library are as follows:")
        print("================================")
        for book in self._books:
            print(book)

    def printperiodicals(self):
        print("The journals we have in our library are as follows:")
        print("================================")
        for journal in self._periodicals:
            print(journal)

    def printusers(self):
        print("The users we have in our library are as follows:")
        print("================================")
        for user in self._users:
            print(user)

    def find_user(self, user_name):
        for u in self._users:
            if u.get_name() == user_name:
                print('User found in library')
                return u

        print('No such user')
        return None

    def find_u_id(self, u_id):
        for u in self._users:
            if u.get_u_id() == u_id:
                print('User found in library')
                return u

        print('No such user')
        return None

    def find_book(self, book_name):
        for m in self._books:
            if m.get_name() == book_name:
                return m

        print('No such book')
        return None

    def find_isbn(self, isbn):
        for m in self._books:
            if m.get_isbn() == isbn:
                return m

        print('No such isbn')
        return None

    def find_author(self, author):
        for m in self._books:
            if m.get_author() == author:
                return m

        print('No such author')
        return None

    def find_journal(self, journal_name):
        for k in self._periodicals:
            if k.get_name() == journal_name:
                return k

        print('No such journal')
        return None


#   Superclass to create all items in the library
class LibraryItem:
    def __init__(self, title, library_id, year):
        self._title = title
        self._library_id = library_id
        self._year = year

    def get_name(self):
        return self._title

    def get_library_id(self):
        return self._library_id

    def __str__(self):
        return 'Title: '+self._title+' LibraryId: ' + str(self._library_id)


#   Create book class
class Book(LibraryItem):
    counter = 0

    def __init__(self, title, library_id, year, author, isbn):
        LibraryItem.__init__(self, title, library_id, year)
        self._isbn = isbn
        self._author = author
        self._onloan = False
        type(self).counter += 1

    def __del__(self):
        type(self).counter -= 1
        print('Item Destructor called, Book deleted.')

    def get_name(self):
        return self._title

    def get_isbn(self):
        return self._isbn

    def get_author(self):
        return self._author

    def get_status(self):
        return self._onloan

    def __str__(self):
        return 'Title:'+self._title + ", " + 'Author:' + str(self._author) + ", " + \
               'LibraryId:' + str(self._library_id) + ' On loan: ' + str(self._onloan)


#   Create periodic class
class Periodical(LibraryItem):
    counter = 0

    def __init__(self, title, library_id, year, editor, volume, issue):
        LibraryItem.__init__(self, title, library_id, year)
        self._editor = editor
        self._issue = issue
        self._volume = volume
        type(self).counter += 1

    def __del__(self):
        type(self).counter -= 1
        print('Destructor called, Journal deleted.')

    def get_name(self):
        return self._title

#   Returned when the class object is called
    def __str__(self):
        return 'Title:'+self._title + ", " + 'Editor:' + str(self._editor) + ", " + 'LibraryId:' + str(self._library_id)


#   Create your user class
class User:
    counter = 0     # Counter to hold how many instances of the class is created

    def __init__(self, name, u_id, address):
        self._name = name
        self._u_id = u_id
        self._address = address
        self._books = None
        self._periodicals = None
        type(self).counter += 1

    def __del__(self):
        type(self).counter -= 1
        print('User Destructor called, User deleted.')

#   Define fucnitons belonging to the user class
    def get_name(self):
        return self._name

    def get_u_id(self):
        return self._u_id

    def loan_book(self, b):
        self._books = b
        b._onloan = True

    def return_book(self, b):
        self._books = b
        b._onloan = False
        self._books = None

#   Returned when the class object is called
    def __str__(self):
        return 'Name: '+self._name+'  Books on loan: ' + str(self._books)


#   Initialise main program
def main():
    library = Library()
    # Add initial books to library
    book1 = Book('The Spider', 1, 2004, 'Caleb', 4369424570445)
    library.add_book(book1)
    book2 = Book('The Cheetah', 2, 2005, 'Spring', 8950724569278)
    library.add_book(book2)
    book3 = Book('The Lion', 3, 2006, 'Nathan', 2337590400375)
    library.add_book(book3)
    # Add initial journals to library
    journal1 = Periodical('Love', 50, 1990, 'Joe', 1, 1)
    library.add_periodical(journal1)
    journal2 = Periodical('Live', 51, 1991, 'Jane', 1, 1)
    library.add_periodical(journal2)
    journal3 = Periodical('Laugh', 52, 1992, 'Joy', 1, 1)
    library.add_periodical(journal3)
    # Add initial users to library
    user1 = User('Micheal', 1, 'Dublin')
    library.add_user(user1)
    user2 = User('Luke', 2, 'Cork')
    library.add_user(user2)
    user3 = User('Mathew', 3, 'Kerry')
    library.add_user(user3)

    done = False
    while not done:
        # Main Menu
        print(""" ====LIBRARY MENU====
          1. Display all available items
          2. Display all Users
          3. Add User
          4. Remove User
          5. Add Library items
          6. Remove Library items
          7. Search for a book
          8. Search for a user
          9. Loan book
          10 Return book
          11. Exit
          """)
        try:
            choice = int(input("Enter Choice:"))
            if choice == 1:
                print("===================")
                print("Books available are")
                library.printbooks()
                print("======================")
                print("Journals available are")
                library.printperiodicals()
            elif choice == 2:
                print("====================")
                print("Users in library are")
                library.printusers()
            elif choice == 3:
                print("Enter the details of the User you'd like to add")
                person_name = input("Enter name: ")
                p = library.find_user(person_name)
                if p is None:
                    address = input("Enter Address: ")
                    user_id = User.counter + 1
                    user = User(person_name, user_id, address)
                    library.add_user(user)
                else:
                    print("User already in library")
            elif choice == 4:
                try:
                    print("Enter the details of the User you'd like to delete")
                    person_name = input("Enter name: ")
                    p = library.find_user(person_name)
                    library.remove_user(p)
                except ValueError:
                    print("cant remove what doesnt exist")
            elif choice == 5:
                print("""Add library Item    
                    1. Add book
                    2. Add Journal               
                    """)
                try:
                    user_choice = int(input("Enter Choice: "))
                    if user_choice == 1:
                        book_name = input("Enter book title: ")
                        j = library.find_book(book_name)
                        if j is None:
                            year = input("Enter Year: ")
                            author = input("Enter Author: ")
                            isbn = input("Enter ISBN: ")
                            if len(isbn) == 13:
                                b_id = Book.counter + 1
                                book = Book(book_name, b_id, year, author, isbn)
                                library.add_book(book)
                            elif len(isbn) != 13:
                                print("ISBN of a book has to be 13 digits. Please try again")
                            else:
                                print("please enter a 13 digit number")
                        else:
                            print("Book already in library")
                    elif user_choice == 2:
                        journal_name = input("Enter book title")
                        k = library.find_journal(journal_name)
                        if k is None:
                            year = input("Enter Year")
                            editor = input("Enter Editor")
                            volume = int(input("Enter Volume"))
                            issue = int(input("Enter Issue"))
                            j_id = Periodical.counter + 1
                            journal = Periodical(journal_name, j_id, year, editor, volume, issue)
                            library.add_periodical(journal)
                        else:
                            print("Journal already in library")
                except ValueError:
                    print("Not an integer")
                else:
                    print("Enter number within range")

            elif choice == 6:
                print(""" library Item    
                    1. Remove book
                    2. Remove Journal               
                    """)
                try:
                    user_choice = int(input("Enter Choice"))
                    if user_choice == 1:
                        try:
                            print("Enter the details of the book you'd like to delete")
                            book_name = input('Enter book title')
                            b = library.find_book(book_name)
                            library.remove_book(b)
                        except ValueError:
                            print('cant remove what doesnt exist')
                    if user_choice == 2:
                        try:
                            print("Enter the details of the journal you'd like to delete")
                            journal_name = input('Enter journal title')
                            b = library.find_journal(journal_name)
                            library.remove_periodical(b)
                        except ValueError:
                            print("cant remove what doesnt exist")
                except ValueError:
                    print("Please enter an integer")
                else:
                    print("Enter 1 or 2")

            elif choice == 7:
                print(""" Search library Item    
                    1. By book name
                    2. By book isbn
                    3. By book Author                 
                    """)
                try:
                    user_choice = int(input("Enter Choice: "))
                    if user_choice == 1:
                        choice = input("Enter Title: ")
                        print(library.find_book(choice))
                    elif user_choice == 2:
                        choice = int(input("Enter book ISBN: "))
                        print(library.find_isbn(choice))
                    elif user_choice == 3:
                        choice = input("Enter Author: ")
                        print(library.find_author(choice))
                    else:
                        print("Enter 1 or 2 or 3 When Searching")
                except ValueError:
                    print("Please enter an integer")

            elif choice == 8:
                print(""" Search library User    
                    1. By User name
                    2. By User Id                 
                    """)
                user_choice = int(input("Enter Choice"))
                if user_choice == 1:
                    choice = input("Enter User name")
                    print(library.find_user(choice))
                if user_choice == 2:
                    choice = int(input("Enter User ID"))
                    print(library.find_u_id(choice))

            elif choice == 9:
                print("Loan Book")
                person_name = input('Enter person\'s name :')
                book_name = input('Enter book\'s Title :')
                p = library.find_user(person_name)
                m = library.find_book(book_name)
                p.loan_book(m)
            elif choice == 10:
                print("Return Book")
                person_name = input("Enter person\'s name :")
                book_name = input("Enter book\'s Title :")
                p = library.find_user(person_name)
                m = library.find_book(book_name)
                p.return_book(m)
            elif choice == 11:
                sys.exit()
            else:
                print("Please enter number betwwen 1 and 11")
        except ValueError:
            print("Not an integer. Please enter input within the range")


main()
