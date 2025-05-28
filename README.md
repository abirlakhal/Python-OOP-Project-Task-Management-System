# Python-OOP-Project-Task-Management-System
This project is designed to showcase practical use of **Object-Oriented Programming (OOP)** in Python by simulating a task management system for a software company. It demonstrates concepts such as class design, object interaction, encapsulation, error handling, and command-based user interfaces.
---

## 🏗️ Project Structure

- **Task Class**: Models tasks with fields like description, assigned programmer, workload, and status.
- **OrderBook Class**: Manages all tasks, organizes them by programmer, and allows analytical operations.
- **Main Application**: Command-line interface to interact with the task system and handle user input errors.

---

## 🧱 Features Implemented

### ✅ Task Class (`Task`)
- Unique ID for each task (auto-incremented).
- Description, workload (estimated hours), assigned programmer.
- Status: finished or unfinished (defaults to unfinished).
- Methods to:
  - Check if finished
  - Mark task as finished

### ✅ OrderBook Class (`OrderBook`)
- Add tasks to the system.
- Retrieve:
  - All tasks
  - Tasks by programmer
  - List of programmers
  - Tasks grouped by programmer
- Mark task as finished by ID.
- Filter:
  - Finished tasks
  - Unfinished tasks
- Programmer-specific status summary (counts and workload).
- Dictionary of programmers with assigned task IDs.

### ✅ Main Application (`main.py`)
- Interactive cmd interface with the following commands:
0: exit
1: add order
2: list finished tasks
3: list unfinished tasks
4: mark task as finished
5: programmers
6: status of programmer
