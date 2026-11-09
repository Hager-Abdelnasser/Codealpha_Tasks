<div align="center">

# 🐍 Python Programming Internship Projects

**A collection of Python projects built during the CodeAlpha Python Programming Internship**

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Tasks](https://img.shields.io/badge/Tasks%20Completed-4%2F4-success)
![Dependencies](https://img.shields.io/badge/Dependencies-None-lightgrey)
![CodeAlpha](https://img.shields.io/badge/CodeAlpha-Internship-orange)

</div>

---

## 📌 Overview

This repository contains my work for the **CodeAlpha Python Programming Internship**. It includes **four console-based projects** that cover Python fundamentals: control flow, data structures, functions, file handling, regular expressions, and clean code organization. Every project runs with the Python standard library only.

## 📑 Table of Contents
- [Projects at a Glance](#-projects-at-a-glance)
- [Task 1: Hangman Game](#-task-1-hangman-game)
- [Task 2: Stock Portfolio Tracker](#-task-2-stock-portfolio-tracker)
- [Task 3: Email Extractor](#-task-3-email-extractor-task-automation)
- [Task 4: Basic Chatbot](#-task-4-basic-chatbot)
- [Getting Started](#-getting-started)
- [Repository Structure](#-repository-structure)
- [Skills Demonstrated](#-skills-demonstrated)
- [Author](#-author)

## 🗂️ Projects at a Glance

| # | Project | Description | Key Concepts |
|---|---------|-------------|--------------|
| 1 | [Hangman Game](./Task1_HangmanGame) | Guess the hidden word with 6 lives | `random`, loops, strings, lists |
| 2 | [Stock Portfolio Tracker](./Task2_StockPortfolioTracker) | Calculate total investment and export results | dictionaries, file handling, `csv` |
| 3 | [Email Extractor](./Task3_EmailExtractor) | Extract unique emails from a text file | `re`, `os`, `sys`, file handling |
| 4 | [Basic Chatbot](./Task4_BasicChatbot) | Rule-based chatbot with predefined replies | `if-elif`, functions, loops |

---

## 🎮 Task 1: Hangman Game

A text-based word guessing game where the player guesses one letter at a time.

**Features**
- Random word from a list of 5 predefined words
- Maximum of 6 incorrect guesses
- ASCII-art hangman that updates after each wrong guess
- Input validation and a play-again option

**Run**
```bash
cd Task1_HangmanGame
python hangman_game.py
```

**Sample**
```text
Word: p _ p _ _ _ n _
Guessed letters: n o p t y
Wrong guesses left: 4

Enter a letter:
```

---

## 📈 Task 2: Stock Portfolio Tracker

A command-line tool that calculates total investment value from user-entered stocks, using a hardcoded price dictionary (`AAPL`, `TSLA`, `GOOGL`, `MSFT`, `AMZN`).

**Features**
- Interactive input of stock symbols and quantities
- Formatted summary table with total investment
- Optional export to `.txt` or `.csv`
- Validation for unknown symbols and invalid quantities

**Run**
```bash
cd Task2_StockPortfolioTracker
python stock_portfolio_tracker.py
```

**Sample**
```text
Stock      Qty       Price           Value
----------------------------------------------
AAPL         2      180.00          360.00
TSLA         1      250.00          250.00
----------------------------------------------
TOTAL INVESTMENT                        610.00
```

---

## 📧 Task 3: Email Extractor (Task Automation)

An automation script that scans a `.txt` file, extracts every email address using regular expressions, and saves the unique results to another file.

**Features**
- Regex-based detection (supports `+` tags and multi-level domains)
- Removes duplicates, lowercases, and sorts results
- Custom input/output paths via command line
- Auto-creates a sample `input.txt` if none exists

**Run**
```bash
cd Task3_EmailExtractor
python email_extractor.py                      # input.txt -> emails.txt
python email_extractor.py my_file.txt out.txt  # custom files
```

**Sample**
```text
Found 4 unique email address(es):
  - admin@my-company.org
  - hager@example.com
  - marketing.team+news@sub.domain.co.uk
  - support@codealpha.tech

Saved to 'emails.txt'
```

---

## 🤖 Task 4: Basic Chatbot

A rule-based chatbot that replies to predefined messages in a continuous conversation loop.

**Features**
- Replies to `hello`, `how are you`, and `bye`
- Extra commands: `what is your name`, `time`, `date`, `help`, `thanks`
- Case-insensitive matching and a friendly fallback reply
- Logic separated into a reusable `get_response()` function

**Run**
```bash
cd Task4_BasicChatbot
python basic_chatbot.py
```

**Sample**
```text
You: hello
Bot: Hi!
You: how are you
Bot: I'm fine, thanks!
You: bye
Bot: Goodbye!
```

---

## 🚀 Getting Started

**Prerequisites:** Python 3.8 or higher. No external libraries are needed.

```bash
git clone https://github.com/Hager-Abdelnasser/CodeAlpha_PythonProgramming.git
cd CodeAlpha_PythonProgramming
```

Then open any task folder and run its script as shown above.

## 📁 Repository Structure

```text
CodeAlpha_PythonProgramming/
├── README.md
├── Task1_HangmanGame/
│   └── hangman_game.py
├── Task2_StockPortfolioTracker/
│   └── stock_portfolio_tracker.py
├── Task3_EmailExtractor/
│   └── email_extractor.py
└── Task4_BasicChatbot/
    └── basic_chatbot.py
```

## 🧠 Skills Demonstrated

- Python fundamentals: variables, loops, conditionals, functions
- Data structures: lists, dictionaries, sets
- File handling: reading and writing `.txt` and `.csv`
- Regular expressions and text processing
- Input validation and error handling
- Clean, modular, well-documented code

## 👩‍💻 Author

**Hager Abdelnasser**
Data Engineering & Analytics | Faculty of Computers & Information, Ain Shams University

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?logo=linkedin&logoColor=white)](https://linkedin.com/in/hager-abdelnasser9)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?logo=github&logoColor=white)](https://github.com/Hager-Abdelnasser)

---

<div align="center">⭐ If you like this repository, give it a star! ⭐</div>
