# Project-28

## 🔐 Password Manager V2

A desktop password manager built with Python and Tkinter that generates, saves, and retrieves passwords using a local JSON file.

## Features

- 🔑 **Generate** secure random passwords (letters, numbers, symbols)
- 💾 **Save** website credentials to a local `data.json` file
- 🔍 **Search** saved credentials by website name
- 📋 **Auto-copies** generated password to clipboard

## Requirements

```bash
pip install pyperclip
```

> Python's `tkinter` and `json` modules are included in the standard library.

## Setup

1. Clone or download the project
2. Add a `logo.png` image to the project folder
3. Install dependencies:
```bash
pip install pyperclip
```
4. Run the app:
```bash
python main.py
```

## File Structure

```
password-manager/
├── main.py       # Main application
├── data.json     # Auto-created on first save
└── logo.png      # App logo image
```

## Usage

| Action | How |
|--------|-----|
| **Save** | Enter website + email + password → click **Add** |
| **Generate** | Click **Generate Password** → auto-fills and copies |
| **Search** | Enter website name → click **Search** |

## Notes

- Passwords are stored locally in `data.json` — keep this file secure
- Search is case-insensitive and supports partial matches
- Email/username field persists between entries for convenience
