Python Cinema Booking System

1. Project Title
Terminal-Based Cinema Booking System

2. Overview of the Project
This project is a lightweight, console-based application designed to simulate a real-world cinema seat reservation system. Built entirely in Python, it allows users to view a visual seating map, book seats, and generate physical ticket receipts.
The system prioritizes data persistence, ensuring that all bookings are saved to a local JSON database. This means seat reservations remain locked even if the application is closed and reopened. It separates the theater into "Standard" and "VIP" zones with dynamic pricing logic.

3. Features
Interactive Seating Map: Visualizes the theater layout in the terminal, showing available seats (e.g., [ A1 ]) and booked seats (e.g., [ XX ]).
Dynamic Pricing: Automatically distinguishes between Standard rows ($12.00) and VIP rows ($20.00).
Data Persistence: Uses a JSON database (cinema_data.json) to store booking states permanently.
Ticket Generation: Automatically creates a detailed .txt receipt in a dedicated tickets/ directory upon successful booking.
Input Validation: Prevents double-booking of seats and handles invalid seat IDs gracefully.
System Audit Logging: Tracks system events (startups, bookings, database loads) in a system_audit.log file.
Admin Reset: Includes a hidden option to wipe the database and reset the theater layout.

4. Technologies/Tools Used
Language: Python 3.x
Core Modules:
json (Data storage)
os (File system management)
logging (System auditing)
datetime (Timestamping tickets)

5. Steps to Install & Run the Project
Prerequisites
Ensure Python 3.6+ is installed on your system. You can check this by typing python --version in your terminal.

Installation
Download the Code:
Save the provided Python script into a file named cinema.py.
Set Up Directory:
Open your terminal or command prompt and navigate to the folder where you saved the file.
cd path/to/your/folder
Run the Application:
Execute the script using Python:
python cinema.py
(Note: On some systems, you may need to use python3 cinema.py)
Automatic Setup:
Upon the first run, the system will automatically create:
cinema_data.json (Database file)
system_audit.log (Log file)
tickets/ (Directory for receipts)

6. Instructions for Testing
Follow these steps to verify the system works as intended:
Launch the App: Run the script. You should see the main menu.
View Map: Select Option 1 to view the seating grid. Confirm that rows C and D are marked as VIP.
Book a Seat:
Select Option 2.
Enter Seat ID: A1.
Enter Name: Aadi Atharva.
Result: The system should confirm success.
Verify Persistence:
Select Option 1 again. Seat A1 should now show [ XX ].
Exit the application (Option 4).
Restart the application (python cinema.py).
Select Option 1. Seat A1 should still be marked as [ XX ].
Check Ticket:
Navigate to the tickets/ folder in your file explorer.
Open the file named Ticket_A1_John Doe.txt.
Verify the timestamp, price ($12.00), and name are correct.
Test VIP Pricing:
Book a seat in row C (e.g., C1).
Check the generated ticket; the price should be $20.00.
Reset System:
Select Option 3 and confirm with y.

View the map; all seats should return to available status.
7. Screenshots
Main Menu & Seating Map:

========================================
       [  S C R E E N  ]       
========================================
[ A1 ] [ A2 ] [ A3 ] ...  | STD  $12.00
[ B1 ] [ B2 ] [ B3 ] ...  | STD  $12.00
[ C1 ] [ C2 ] [ C3 ] ...  | VIP  $20.00
...


Ticket Receipt Example:

================================
      CINEMA TICKET RECEIPT
================================
Date:    2023-10-25 14:30:00
Guest:   Aadi Atharva
--------------------------------
Seat:    A1 (Standard)
Price:   $12.00
--------------------------------
Status:  PAID
================================

