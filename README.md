[README.md](https://github.com/user-attachments/files/29695595/README.md)
# Bank-System-Management# 🏦 Banking Management System

An advanced, secure, and interactive Banking Management System built from scratch using **Python**. The application leverages Core **Object-Oriented Programming (OOP)** principles to handle robust backend financial logic and utilizes a local CSV file as a lightweight data storage system. The entire application is wrapped in a modern, user-friendly **Streamlit** web interface.

---

## ✨ Key Features

- **🔐 Secure User Authentication:** Multi-bank selection with encrypted-like verification for user credentials against the database.
- **💼 Account Management:** Create new bank accounts or securely delete existing ones directly through the user interface.
- **💸 Financial Operations:** Real-time deposits and withdrawals with robust error handling (e.g., preventing negative inputs or overdrafts).
- **📊 CSV Database Integration:** Efficient tracking of user data, passwords, and balances using custom file handling mechanisms (`Names.csv`).
- **🎨 Interactive Web GUI:** Clean and responsive navigation using Streamlit components and sidebar routing.

---

## 🛠️ Tech Stack & Architecture

- **Language:** Python
- **Frontend / GUI:** Streamlit
- **Data Storage:** CSV (Tab-separated values)
- **Design Pattern:** Object-Oriented Programming (Inheritance, Encapsulation)

### Code Structure Architecture

- `Bank_System`: The core engine managing global system actions (Login, Create, Update, Delete).
- `Bank_Account`: Inherits from the main system to manage unique instance properties like balance manipulation and credentials verification.
- `Streamlit Routing`: Dedicated modules for modular page rendering (`Login`, `Register`, `Operations`).
