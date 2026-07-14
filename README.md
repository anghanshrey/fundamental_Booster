<div align="center">

![Header](https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:2c5364,100:0f2027&height=220&section=header&text=FUNDAMENTAL%20BOOSTER&fontSize=42&fontColor=FFFFFF&animation=twinkling&fontAlignY=38&desc=Interactive%20Personal%20Data%20Collector%20•%20Python%20Fundamentals&descAlignY=58&descSize=16)

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=22&duration=2600&pause=700&color=2C5364&center=true&vCenter=true&multiline=true&repeat=true&width=700&height=80&lines=Variables+%2B+Data+Types+%2B+Operators;Type+Casting+%E2%86%92+int()+%2F+float();id()+%2B+type()+%E2%80%94+Peeking+Inside+Memory;Built+for+Red+%26+White+Skill+Education)](https://git.io/typing-svg)

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-✔_Completed-brightgreen?style=for-the-badge)
![Libraries](https://img.shields.io/badge/External_Libraries-None_Required-black?style=for-the-badge)
![PR](https://img.shields.io/badge/Assignment-Fundamental_Booster-2C5364?style=for-the-badge)

</div>

<div align="center">

### 🧭 Table of Contents

[Overview](#-project-overview) • [Objective](#-objective) • [Live Demo](#-example-output) • [Flow](#-program-flow) • [Features](#-features) • [Skills](#-skills-demonstrated) • [Getting Started](#-getting-started) • [Structure](#-project-structure) • [Assumptions](#️-assumptions) • [Tech Stack](#️-tech-stack) • [Contact](#-contact-me) • [Video](#-Video)

</div>

---

## 📌 Project Overview

**Fundamental Booster** is a beginner-friendly Python console application that behaves like a **live interview bot** — it interactively collects a user's personal information and demonstrates core Python fundamentals: `input()`/`print()`, variables, data types, type casting, arithmetic operators, and the built-in `type()` and `id()` functions.

It captures the user's **name, age, height, and favourite number**, then displays a formatted summary showing each value's type and memory address, along with an estimated birth year.

<table>
<tr>
<td width="25%" align="center">🧾<br/><b>Input & Output</b><br/><sub><code>input()</code> / <code>print()</code></sub></td>
<td width="25%" align="center">🧬<br/><b>Data Types & Operators</b><br/><sub>str · int · float</sub></td>
<td width="25%" align="center">🔁<br/><b>Type Casting</b><br/><sub><code>int()</code> / <code>float()</code></sub></td>
<td width="25%" align="center">🔍<br/><b>Introspection</b><br/><sub><code>type()</code> / <code>id()</code></sub></td>
</tr>
</table>

> Built for **PR. 1: Fundamental Booster — Red & White Skill Education.**

---

## 🎯 Objective

Create an Interactive Personal Data Collector application in Python that captures, processes, and displays personal information from the user using fundamental Python concepts:

- `print()` and `input()` functions
- Data types, variables, and operators
- Type casting
- Built-in `id()` and `type()` functions

---

## ✨ Features

- Collects four pieces of user data with clear, guided prompts
- Casts input to the correct data type (`str`, `int`, `float`)
- Displays each variable's value, data type, and memory address
- Calculates an approximate birth year using arithmetic operators
- Clean, formatted console output from start to finish

---

## 🌊 Program Flow

```
                    ┌─────────────────────────┐
                    │      Program Starts      │
                    │   Welcome Message Shown   │
                    └────────────┬─────────────┘
                                 ↓
                    ┌─────────────────────────┐
                    │     Collect Raw Input     │
                    │  name · age · height ·    │
                    │      favourite number     │
                    └────────────┬─────────────┘
                                 ↓
                    ┌─────────────────────────┐
                    │       Type Casting        │
                    │  int(input) → age          │
                    │  float(input) → height     │
                    │  int(input) → favnum       │
                    └────────────┬─────────────┘
                                 ↓
              ┌──────────────────┴──────────────────┐
              ↓                                      ↓
   ┌─────────────────────┐              ┌─────────────────────────┐
   │  Introspection Pass   │              │     Arithmetic Pass       │
   │  type(var) → data type │              │  curr_year − age = b_year │
   │  id(var)   → memory addr│              └────────────┬────────────┘
   └──────────┬───────────┘                             │
              └───────────────────┬─────────────────────┘
                                  ↓
                    ┌─────────────────────────┐
                    │      Display Summary      │
                    │  formatted console output │
                    └────────────┬─────────────┘
                                 ↓
                    ┌─────────────────────────┐
                    │     Goodbye Message       │
                    └─────────────────────────┘
```

| Step | Stage | Description |
|:---:|---|---|
| 1 | **Welcome & Instructions** | Display a welcome message and a brief description of the program |
| 2 | **Collect Information** | Prompt the user for name (`str`), age (`int`), height (`float`), and favourite number (`int`) |
| 3 | **Data Processing** | Compute the approximate birth year from age; capture each variable's type and memory address |
| 4 | **Display Results** | Print a user-friendly summary of all collected data and type-conversion details |
| 5 | **Exit Message** | Thank the user and end the program |

---

## 🎬 Example Output

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

> 💡 Memory addresses change every run — that's Python's memory manager at work, and this project deliberately surfaces it instead of hiding it.

---

## 🎯 Skills Demonstrated

<div align="center">

![Input Handling](https://img.shields.io/badge/Input_Handling-████████████-2C5364?style=flat-square)
![Type Casting](https://img.shields.io/badge/Type_Casting-███████████-2C5364?style=flat-square)
![f--strings](https://img.shields.io/badge/f--string_Formatting-████████████-2C5364?style=flat-square)
![Memory Introspection](https://img.shields.io/badge/Memory_Introspection_(id())-██████████-2C5364?style=flat-square)
![Arithmetic Ops](https://img.shields.io/badge/Arithmetic_Operators-███████████-2C5364?style=flat-square)

</div>

- Reading and validating user input with `input()`
- Explicit type conversion using constructor functions
- Formatting dynamic, readable output with f-strings
- Inspecting Python's internal typing and memory system live
- Deriving new values from existing ones with simple arithmetic

---

## ✅ Assignment Requirements Checklist

| Requirement (per brief) | Status |
|---|:---:|
| Use `input()` to collect name, age, height, favourite number | ✅ |
| Use `print()` to guide the user through each step | ✅ |
| Store each value in an appropriately typed variable | ✅ |
| Demonstrate an arithmetic operator (birth year calculation) | ✅ |
| Cast input to `int` / `float` explicitly | ✅ |
| Display each variable's type using `type()` | ✅ |
| Display each variable's memory address using `id()` | ✅ |
| Welcome message + exit/goodbye message | ✅ |
| Uploaded to GitHub with a descriptive README | ✅ |

---

## ✅ Video

Link : https://drive.google.com/drive/folders/1VgNOKID6L0mhJ0mrD0pcZzWWdexqvZAd?usp=sharing

## 🚀 Getting Started

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
- Your name
- Your age
- Your height (in meters)
- Your favourite number

---

## 📁 Project Structure

```
fundamental-booster/
├── fundamantal_Booster.py   # Main script
└── README.md                # Project documentation
```

---

## ⚠️ Assumptions

- The user enters valid input types when prompted (e.g., a numeric value for age); no input validation or error handling is implemented, as it wasn't part of the stated requirements.
- "Birth year" is a simple approximation (current year − age) and does not account for whether the user has already had their birthday this year.
- The reference year used for the birth-year calculation is fixed at **2026**, matching when this project was built. A fully dynamic version could use `datetime.date.today().year` instead.

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Concepts demonstrated:** `input()`/`print()`, variables & data types, type casting, arithmetic operators, `type()`, `id()`

---

## 📬 Contact Me

<div align="center">

[![Gmail](https://img.shields.io/badge/Email-shreyanghan205%40gmail.com-2C5364?style=for-the-badge&logo=gmail&logoColor=white)](mailto:shreyanghan205@gmail.com)

</div>

---

<div align="center">

*"Quality is our Motto."* — Red & White Skill Education

![Footer](https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:2c5364,100:0f2027&height=140&section=footer)

</div>
