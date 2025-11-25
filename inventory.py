# library_manager/inventory.py
import json
from pathlib import Path
from typing import List, Optional
import logging

from .book import Book

logger = logging.getLogger(__name__)

class LibraryInventory:
    def __init__(self, storage_path: Path):
        self.storage_path = storage_path
        self.books: List[Book] = []

    def add_book(self, book: Book):
        if self.search_by_isbn(book.isbn) is not None:
            raise ValueError(f"A book with ISBN {book.isbn} already exists.")
        self.books.append(book)
        logger.info("Added book: %s", book)

    def search_by_title(self, query: str) -> List[Book]:
        q = query.strip().lower()
        return [b for b in self.books if q in b.title.lower()]

    def search_by_isbn(self, isbn: str) -> Optional[Book]:
        isbn = isbn.strip()
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def display_all(self) -> List[str]:
        return [str(b) for b in self.books]

    def issue_book(self, isbn: str):
        book = self.search_by_isbn(isbn)
        if book is None:
            raise LookupError(f"No book found with ISBN {isbn}")
        book.issue()
        logger.info("Issued book: %s", book)

    def return_book(self, isbn: str):
        book = self.search_by_isbn(isbn)
        if book is None:
            raise LookupError(f"No book found with ISBN {isbn}")
        book.return_book()
        logger.info("Returned book: %s", book)

    def save_to_file(self):
        try:
            data = [b.to_dict() for b in self.books]
            self.storage_path.parent.mkdir(parents=True, exist_ok=True)
            with self.storage_path.open("w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            logger.info("Catalog saved to %s", self.storage_path)
        except Exception as e:
            logger.error("Failed to save catalog: %s", e)
            raise

    def load_from_file(self):
        if not self.storage_path.exists():
            logger.info("Catalog file %s not found. Starting with empty inventory.", self.storage_path)
            self.books = []
            return

        try:
            with self.storage_path.open("r", encoding="utf-8") as f:
                data = json.load(f)
            # Validate and convert
            loaded_books = []
            for item in data:
                try:
                    loaded_books.append(Book.from_dict(item))
                except Exception as e:
                    logger.error("Failed to parse book entry %s: %s", item, e)
            self.books = loaded_books
            logger.info("Loaded %d books from %s", len(self.books), self.storage_path)
        except (json.JSONDecodeError, ValueError) as e:
            logger.error("Catalog file %s is corrupted: %s", self.storage_path, e)
            # Option: backup corrupted file
            backup = self.storage_path.with_suffix(self.storage_path.suffix + ".corrupt")
            try:
                self.storage_path.replace(backup)
                logger.info("Corrupted file renamed to %s", backup)
            except Exception as ex:
                logger.error("Failed to backup corrupted file: %s", ex)
            self.books = []
        except Exception as e:
            logger.error("Unexpected error loading catalog: %s", e)
            self.books = []


