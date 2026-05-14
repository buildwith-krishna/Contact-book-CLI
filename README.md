# 📇 Contact Book CLI — OOP Edition

> A command-line contact manager rebuilt from scratch using Object-Oriented Python — modular, clean, and fully persistent.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Platform](https://img.shields.io/badge/Platform-Termux%20%7C%20Linux%20%7C%20macOS-green?style=flat-square)
![Storage](https://img.shields.io/badge/Storage-JSON%20File--Based-orange?style=flat-square)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)
![OOP](https://img.shields.io/badge/Architecture-OOP-purple?style=flat-square)

Built entirely on **Termux (Android)**. No PC. No excuses.

---

## ✨ Features

| Feature | Description |
|---|---|
| ➕ **Add** | Save a contact with name and number |
| 📄 **View All** | Display every saved contact cleanly |
| 🔍 **Search** | Find a contact by exact name |
| ✏️ **Update** | Replace name and number safely — old entry removed |
| ❌ **Delete** | Remove a contact with confirmation prompt |
| 💾 **Persistent Storage** | JSON file-based — data survives restarts |
| ⚠️ **Input Validation** | Empty input caught on every operation |

---

## 🏗️ Architecture

```
oops-contact_book/
├── config.py      # FILE_NAME constant
├── storage.py     # load() and save() — handles all JSON I/O
├── structure.py   # ContactBook class — all CRUD methods
└── main.py        # Main class (inherits ContactBook) + menu loop
```

### How it's structured

- **`config.py`** — single source of truth for the filename
- **`storage.py`** — separation of concerns; all storage logic lives here
- **`structure.py`** — `ContactBook` class owns all contact operations
- **`main.py`** — `Main` inherits `ContactBook`, drives the menu loop

---

## ⚙️ Tech Stack

- **Language** — Python 3
- **Storage** — JSON (file-based, local)
- **Interface** — CLI (standard input/output)
- **Architecture** — OOP (Inheritance, Composition, Separation of Concerns)

---

## 📦 Installation & Usage

```bash
git clone https://github.com/buildwith-krishna/oops-contact_book
cd oops-contact_book
python main.py
```

---

## 🖥️ CLI Flow

```
<<--Contact Book->>
1. Add a contact
2. Show all contacts
3. Search a contact
4. Update a contact
5. Delete a contact
6. Exit
```

---

## 🧠 OOP Concepts Applied

| Concept | Where |
|---|---|
| **Class** | `ContactBook` in `structure.py` |
| **Inheritance** | `Main` inherits `ContactBook` in `main.py` |
| **Composition** | `ContactBook` uses `storage.py` — HAS A storage system, not IS A |
| **Separation of Concerns** | Storage, logic, and UI each in their own file |
| **Input Validation** | Every method guards against empty input before processing |
| **Flag Pattern** | `in_contacts` flag avoids mutating a dict during iteration |

---

## 👨‍💻 Author

**Krishna Pandey** — [@buildwith-krishna](https://github.com/buildwith-krishna)

> *"Same project. Better architecture. That's growth."*
