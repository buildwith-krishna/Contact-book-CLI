# 📇 Contact Book CLI — OOP Edition

> A command-line contact manager rebuilt in Python using Object-Oriented Programming — cleaner architecture, same zero fluff.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Platform](https://img.shields.io/badge/Platform-Termux%20%7C%20Linux%20%7C%20macOS-green?style=flat-square)
![Storage](https://img.shields.io/badge/Storage-JSON%20File--Based-orange?style=flat-square)
![Architecture](https://img.shields.io/badge/Architecture-OOP-purple?style=flat-square)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)

Built entirely on **Termux (Android)**. No PC. No excuses.

---

## ✨ Features

| Feature | Description |
|---|---|
| ➕ **Add** | Store name and phone number for any contact |
| 📄 **View All** | Display every saved contact in a clean format |
| 🔍 **Search** | Find contacts instantly by name |
| ✏️ **Update** | Modify an existing contact's name and number |
| ❌ **Delete** | Remove entries with a confirmation prompt |
| 💾 **Persistent Storage** | JSON file-based storage — data survives restarts |
| ⚠️ **Input Validation** | Handles empty fields and invalid inputs gracefully |

---

## ⚙️ Tech Stack

- **Language** — Python 3
- **Storage** — JSON (file-based, local)
- **Interface** — CLI (standard input/output)
- **Architecture** — Object-Oriented Programming (OOP)

---

## 📦 Installation & Usage

```bash
# Clone the repository
git clone https://github.com/buildwith-krishna/oops-contact-book

# Navigate into the project
cd oops-contact-book

# Run
python main.py
```

---

## 🖥️ CLI Flow

```
<<--Contact Book-->>
1. Add a contact
2. Show all contacts
3. Search a contact
4. Update a contact
5. Delete a contact
6. Exit
```

---

## 📁 Project Structure

```
oops-contact-book/
├── main.py          # Entry point — menu loop via Main class
├── structure.py     # ContactBook class — all CRUD methods
├── storage.py       # load() and save() helpers for JSON I/O
├── data.json        # Stored contacts (auto-created)
└── README.md
```

---

## 🏗️ Architecture

This version is a full OOP refactor of the original procedural contact book.

- **`storage.py`** — handles all JSON read/write logic via `load()` and `save()`
- **`structure.py`** — defines the `ContactBook` class with all CRUD operations as methods
- **`main.py`** — defines the `Main` class, which inherits from `ContactBook` and runs the menu loop

This separation keeps concerns clean: storage logic, business logic, and UI flow each live in their own layer.

---

## 🧠 Concepts Practiced

- Object-Oriented Programming (classes, inheritance)
- JSON data management (`json.dump` / `json.load`)
- File I/O with persistent read-write cycles
- Modular code separation across multiple files
- CLI-based program flow and menu design
- Input validation and basic exception handling

---

## ✅ Completed Scope

- [x] Add / View / Search / Update / Delete contacts
- [x] JSON-based persistent storage
- [x] Confirmation prompt on delete
- [x] Input validation and error handling
- [x] OOP refactor with class inheritance
- [x] Modular file structure (main, structure, storage)
- [x] Clean, readable CLI interface

**This project is complete as designed.**

---

## 👨‍💻 Author

**Krishna Pandey** — [@buildwith-krishna](https://github.com/buildwith-krishna)

> *"Building backend systems step by step — with focus on logic, structure, and real-world usability. Even from a phone."*
