# cli/main.py
import logging
from pathlib import Path
from library_manager.inventory import LibraryInventory
from library_manager.book import Book

LOG_FILE = Path.cwd() / "library.log"
CATALOG_FILE = Path.cwd() / "books.json"

def configure_logging():
    logging.basicConfig(
        filename=str(LOG_FILE),
        level=logging.INFO,
        format="%(asctime)s %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    # Also log to console for convenience
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter("%(levelname)s: %(message)s")
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)

def prompt_non_empty(prompt_text):
    while True:
        val = input(prompt_text).strip()
        if val:
            return val
        print("Input cannot be empty. Try again.")

def main():
    configure_logging()
    logger = logging.getLogger(__name__)

    inventory = LibraryInventory(CATALOG_FILE)
    try:
        inventory.load_from_file()
    except Exception as e:
        logger.error("Error loading catalog: %s", e)

    MENU = """
Library Inventory Manager
1. Add Book
2. Issue Book
3. Return Book
4. View All Books
5. Search by Title
6. Search by ISBN
7. Exit
Choose an option (1-7): """

    while True:
        try:
            choice = input(MENU).strip()
            if choice == "1":
                title = prompt_non_empty("Title: ")
                author = prompt_non_empty("Author: ")
                isbn = prompt_non_empty("ISBN: ")
                book = Book(title=title, author=author, isbn=isbn)
                try:
                    inventory.add_book(book)
                    inventory.save_to_file()
                    print("Book added successfully.")
                except ValueError as ve:
                    print("Error:", ve)
            elif choice == "2":
                isbn = prompt_non_empty("ISBN to issue: ")
                try:
                    inventory.issue_book(isbn)
                    inventory.save_to_file()
                    print("Book issued.")
                except Exception as e:
                    print("Error:", e)
            elif choice == "3":
                isbn = prompt_non_empty("ISBN to return: ")
                try:
                    inventory.return_book(isbn)
                    inventory.save_to_file()
                    print("Book returned.")
                except Exception as e:
                    print("Error:", e)
            elif choice == "4":
                all_books = inventory.display_all()
                if not all_books:
                    print("No books in inventory.")
                else:
                    print("\n".join(all_books))
            elif choice == "5":
                q = prompt_non_empty("Search title (partial allowed): ")
                results = inventory.search_by_title(q)
                if results:
                    for b in results:
                        print(b)
                else:
                    print("No matching books found.")
            elif choice == "6":
                isbn = prompt_non_empty("Search ISBN: ")
                b = inventory.search_by_isbn(isbn)
                if b:
                    print(b)
                else:
                    print("No book found with that ISBN.")
            elif choice == "7":
                print("Exiting. Goodbye!")
                break
            else:
                print("Invalid option, choose 1-7.")
        except KeyboardInterrupt:
            print("\nInterrupted. Exiting.")
            break
        except Exception as e:
            logger.error("Unexpected error in CLI: %s", e)
            print("An error occurred:", e)

if __name__ == "__main__":
    main()

