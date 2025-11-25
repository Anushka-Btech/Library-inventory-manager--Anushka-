### Library-inventory-manager--Anushka-
A Python-based Library Inventory Management System with:
✓ Object-Oriented Design
✓ JSON File Persistence
✓ Exception Handling
✓ Logging
✓ Fully Functional Command Line Interface
✓ Search, Add, Issue, Return Features
✓ Clean Project Packaging

## Project Structure
library-inventory-manager-Anushka/
│
├── library_manager/
│   ├── book.py         # Book class definition
│   └── inventory.py    # Inventory manager logic
│
├── cli/
│   └── main.py         # Menu-driven CLI interface
│
├── books.json          # Database file (JSON)
├── README.md           # Project Documentation
├── requirements.txt    # Dependencies list
└── .gitignore

## Features
# Book Class
=> title, author, isbn, status fields
=> issue(), return_book(), is_available()
=> JSON serialization with to_dict()
=> str() override for clean printing

# Inventory Manager
=> Add books
=> Search by Title / ISBN
=> Issue & Return books
=> Display all books
=> Duplicate ISBN prevention
=> JSON file save/load
=> Error handling for missing/corrupt files

# CLI Interface
=> Simple numbered menu
=> Input validation
=> Live updates to JSON
=> Logging all actions

# Logging
=> All actions and exceptions are logged to:library.log
