# library_manager/book.py
from dataclasses import dataclass, asdict

@dataclass
class Book:
    title: str
    author: str
    isbn: str
    status: str = "available"  # "available" or "issued"

    def __post_init__(self):
        # Basic normalization
        self.title = self.title.strip()
        self.author = self.author.strip()
        self.isbn = self.isbn.strip()

    def __str__(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - {self.status}"

    def to_dict(self):
        """Return a JSON-serializable dict."""
        return asdict(self)

    @classmethod
    def from_dict(cls, d):
        """Create a Book from a dict (used when loading from JSON)."""
        return cls(
            title=d.get("title", "").strip(),
            author=d.get("author", "").strip(),
            isbn=d.get("isbn", "").strip(),
            status=d.get("status", "available")
        )

    def is_available(self):
        return self.status == "available"

    def issue(self):
        if not self.is_available():
            raise ValueError(f"Book '{self.title}' is already issued.")
        self.status = "issued"

    def return_book(self):
        if self.is_available():
            raise ValueError(f"Book '{self.title}' is already available.")
        self.status = "available"


