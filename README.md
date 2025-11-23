Hotel Management System (CLI)

📌 Project Overview

The Hotel Management System is a Python-based console application designed to streamline the daily operations of a small hotel. It provides a user-friendly interface for receptionists to manage room availability, book guests into specific rooms, and process check-outs efficiently.

The system utilizes Python's core data structures to ensure fast data retrieval and manipulation, replacing manual pen-and-paper ledgers with a digital solution.

🚀 Features

Real-Time Status Dashboard: View the current occupancy status of all rooms instantly.

Room Booking: Assign guests to specific rooms with validation to prevent double-booking.

Check-Out System: Process guest departures and automatically reset room status to "Available."

Input Validation: Robust error handling for non-numeric inputs or invalid room numbers.

Dynamic Data Handling: Uses Python dictionaries for efficient state management.

🛠️ Tech Stack

Language: Python 3.x

Interface: Command Line Interface (CLI)

Storage: In-memory dictionary (Runtime storage)

💻 Installation & Usage

Prerequisites

Ensure you have Python installed on your system. You can check this by running:

python --version


Running the Application

Download the script (e.g., hotel_system.py).

Open your terminal or command prompt.

Navigate to the folder containing the file.

Run the following command:

python hotel_system.py


How to Use

Menu: Upon launching, you will see a main menu with options 1-4.

Display: Select 1 to see which rooms are free and which are occupied.

Booking: Select 2, enter a valid room number (e.g., 101), and the guest's name.

Check-out: Select 3 and enter the room number to release the room.

Exit: Select 4 to close the program.

🔮 Future Improvements

Integration with a database (SQL/SQLite) for persistent storage.

Calculation of billing and room charges based on duration.

Implementation of a Graphical User Interface (GUI) using Tkinter.
