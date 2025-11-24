Project Statement: Cinema Booking System

1. Problem Statement

Managing cinema seat reservations manually or through spreadsheet-based systems is prone to human error, resulting in double-bookings, revenue loss, and customer dissatisfaction. Additionally, without a persistent digital database, reservation data is at risk of being lost during power outages or system restarts. There is a need for a reliable, automated system that can visualize seat availability in real-time, enforce pricing rules based on seat quality (VIP vs. Standard), and generate immediate proof of purchase while ensuring data integrity across sessions.

2. Scope of the Project

This project aims to deliver a Minimum Viable Product (MVP) of a terminal-based booking management system.

In-Scope:

Inventory Management: Real-time tracking of 40 seats (5 rows x 8 columns).

Tiered Pricing Logic: Automated price calculation distinguishing between Standard rows and VIP rows.

Data Persistence: Implementation of a file-based storage system (JSON) to retain booking status after application closure.

Transaction Proof: Automatic generation of individual text-file receipts for every successful booking.

System Auditing: Basic logging of system events for maintenance and debugging.

Out-of-Scope:

Graphical User Interface (GUI) or Web Interface.

Integration with live payment gateways (Credit Card/PayPal).

User account management (Login/Registration for customers).

Multi-hall support (currently limited to a single cinema hall instance).

3. Target Users

Ticket Counter Staff: The primary users who interact with the terminal to view available seats and process bookings for walk-in customers.

Cinema Administrators: Users responsible for resetting the system, managing the "day-to-day" operations, and auditing the logs.

Small Theater Owners: Business owners looking for a lightweight, cost-effective solution to digitize their seating operations without complex infrastructure.

4. High-Level Features

Visual Seating Map: A text-based graphical representation of the cinema layout, using indicators to differentiate between available seats ([ A1 ]) and booked seats ([ XX ]).

Smart Booking Engine: A validation system that prevents double-booking and ensures valid seat selection.

Dynamic Pricing Model: Automatic assignment of premium prices to specific "VIP" rows (Rows C & D) versus standard pricing for others.

Digital Receipt Generation: Creation of timestamped, unique .txt files for every transaction to serve as physical tickets.

Fail-Safe Data Storage: A robust JSON backend that automatically saves state changes, ensuring zero data loss during application restarts.