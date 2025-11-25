### 📚 Library Inventory Manager – Anushka

A simple Python-based command-line Library Inventory Manager.  
This project manages books in a library with features like adding books, issuing, returning, searching, and storing data in JSON format.

Designed as a B.Tech 1st year Python assignment 3rd with proper OOP concepts, file handling, exception handling, and logging.

---

## 🚀 Features

## Book Management
- Add new books  
- Issue a book  
- Return a book  
- Check availability  
- Convert book object to dictionary  

## Inventory Management
- Store all books in a list  
- Search by title  
- Search by ISBN  
- Display all books  

## JSON File Storage
- Automatically saves book data to `books.json`  
- Loads data when application starts  
- Handles missing or corrupted files with try–except  

## Logging
Uses Python's `logging` module:
- INFO logs for normal actions  
- ERROR logs for file issues  

A file named `library.log` is created automatically.

## Menu-Driven CLI
- Simple text-based interface  
- Input validation  
- User-friendly messages  

---

## Folder Structure
library-inventory-manager-Anushka/
│
├── books.json
├── README.md
├── requirements.txt
├── .gitignore
│
├── library_manager/
│ ├── init.py
│ ├── book.py
│ └── inventory.py
│
└── cli/
└── main.py


---

## Requirements

Project uses only Python's built-in libraries:
- `json`
- `pathlib`
- `logging`

---
## How to Run the Project
Open terminal inside the project folder and run:
python -m cli.main

You will see this menu:

Library Inventory Manager
1.Add Book
2.Issue Book
3.Return Book
4.View All Books
5.Search by Title
6.Search by ISBN

## Error Handling
Missing JSON file → program creates a new one
Corrupted JSON → displays message and resets file
Wrong input → safely handled with try–except
Exit

