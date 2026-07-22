# ConfigCraft---Production-Ready-CLI-Settings-Manager

ConfigCraft is a lightweight, production-grade Command-Line Interface (CLI) application built in Python. It manages system and user configurations efficiently using an interactive menu, mimicking how professional cloud and DevOps tools (like AWS CLI or Docker) handle environment states.

---

## 🚀 Key Features

- **Persistent Storage:** Configurations are saved directly onto the hard drive in a structured `user_config.json` file, ensuring data persists across terminal sessions.
- **Interactive CLI Menu:** A user-friendly, loop-driven keyboard menu allowing seamless navigation for CRUD operations.
- **Defensive Programming & Validation:** Built-in safeguards against corrupted files, empty inputs, duplication, and automatically normalizes whitespace and casings (`.strip()` and `.lower()`).
- **Robust Error Handling:** Utilizes structured conditional gates to prevent application crashes during invalid operations.

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Core Modules:** `json` (Data Serialization), `os` (File System Verification), `sys` (Process Management)

---

## 💻 How To Run

1. Clone this repository:
   ```bash
   git clone https://github.com
   ```
2. Navigate to the project directory:
   ```bash
   cd ConfigCraft
   ```
3. Run the application:
   ```bash
   python config_manager.py
   ```

---

## 📸 Sample Usage & Output

```text
========================================
⚙️  CONFIGCRAFT: CLI SETTINGS MANAGER
========================================
1. ➕ Add New Setting
2. 🔄 Update Existing Setting
3. 🗑️ Delete a Setting
4. 📋 View All Settings
5. 🚪 Exit
========================================
Enter your choice (1-5): 1
Enter Setting Name (Key): theme
Enter Value: dark

✅ Success: 'theme' configured to 'dark'.
```

---

## 🎯 Future Enhancements
- [ ] Add base64 encryption for sensitive configuration values (like passwords/tokens).
- [ ] Implement support for exporting configurations to `.env` or `.yaml` formats.

---
💡 *Built as part of an advanced exploration into Python structures, data persistence, and robust CLI software engineering.*
