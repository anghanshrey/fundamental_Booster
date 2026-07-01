# Fundamental Booster — Interactive Personal Data Collector

A beginner-friendly Python console application that interactively collects a user's personal information and demonstrates core Python fundamentals — `input()`/`print()`, variables, data types, type casting, arithmetic operators, and the built-in `type()` and `id()` functions.

Built for **PR. 1: Fundamental Booster** — Red & White Skill Education.

1. ## Overview

This project is an **Interactive Personal Data Collector** that captures a user's name, age, height, and favourite number, then displays a formatted summary showing each value's type and memory address, along with an estimated birth year.

2. ## Objective

Create an Interactive Personal Data Collector application in Python that captures, processes, and displays personal information from the user using fundamental Python concepts:

- `print()` and `input()` functions
- Data types, variables, and operators
- Type casting
- Built-in `id()` and `type()` functions

3. ## Features

- Collects four pieces of user data with clear, guided prompts
- Casts input to the correct data type (`str`, `int`, `float`)
- Displays each variable's **value**, **data type**, and **memory address**
- Calculates an approximate **birth year** using arithmetic operators
- Clean, formatted console output from start to finish

4. ## Program Flow

| Step | Stage | Description |
|---|---|---|
| 1 | **Welcome & Instructions** | Display a welcome message and a brief description of the program |
| 2 | **Collect Information** | Prompt the user for name (`str`), age (`int`), height (`float`), and favourite number (`int`) |
| 3 | **Data Processing** | Compute the approximate birth year from age; capture each variable's type and memory address |
| 4 | **Display Results** | Print a user-friendly summary of all collected data and type-conversion details |
| 5 | **Exit Message** | Thank the user and end the program |

5. ## Getting Started

### Prerequisites

- Python 3.x
- No external libraries required

### Installation

```bash
git clone https://github.com/<your-username>/fundamental-booster.git
cd fundamental-booster
```

### Usage

```bash
python fundamantal_Booster.py
```

You'll be prompted to enter:

1. Your name
2. Your age
3. Your height (in meters)
4. Your favourite number


6. ## Example Output

```
Welcome to the interactive Personal Data Collecter!

Please enter your name: Alice
Please enter your age: 25
Please enter your height in meters: 1.68
Please enter your favourite number: 7

Thank you! Here is the information we collected:

Name: Alice (Type: <class 'str'>, Memory Address: 140703847239568)
Age: 25 (Type: <class 'int'>, Memory Address: 9793456)
Height: 1.68 (Type: <class 'float'>, Memory Address: 140703847253232)
Favourite Number: 7 (Type: <class 'int'>, Memory Address: 9793312)

Your birth year is approximately: 2001 (based on your age of 25)

Thank you for using the Personal Data Collector. Goodbye!
```

7. ## Project Video
   Project link
   
8. ## Project Structure

```
fundamental-booster/
├── fundamantal_Booster.py   # Main script
└── README.md                # Project documentation
```

9. ## Assumptions

- The user enters valid input types when prompted (e.g., a numeric value for age); no input validation or error handling is implemented, as it wasn't part of the stated requirements.
- "Birth year" is a simple approximation (`current year − age`) and does not account for whether the user has already had their birthday this year.
- The reference year used for the birth-year calculation is fixed at `2026`, matching when this project was built. A fully dynamic version could use `datetime.date.today().year` instead.

10. ## Tech Stack

- **Language:** Python 3
- **Concepts demonstrated:** `input()`/`print()`, variables & data types, type casting, arithmetic operators, `type()`, `id()`

11. ## Content Me

 Gmail : shreyanghan205@gmail.com
    

