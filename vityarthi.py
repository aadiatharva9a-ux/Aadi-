import os
import json
import logging
from datetime import datetime
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("system_audit.log"),
        logging.StreamHandler()
    ]
)

CONFIG = {
    "ROWS": 5,
    "COLS": 8,
    "VIP_ROW_START": 3, # Rows 3 and 4 are VIP
    "PRICE_STD": 12.00,
    "PRICE_VIP": 20.00,
    "DB_FILE": "cinema_data.json",
    "TICKET_DIR": "tickets"
}

class Seat:
    """Represents a single seat in the theater."""
    def __init__(self, row_id, col_id, price, is_vip=False):
        self.row_id = row_id      # e.g., "A"
        self.col_id = col_id      # e.g., 1
        self.price = price
        self.is_vip = is_vip
        self.is_booked = False
        self.booked_by = None

    def get_id(self):
        """Returns seat code, e.g., 'A1'"""
        return f"{self.row_id}{self.col_id}"

    def to_dict(self):
        """Serialization for JSON storage."""
        return {
            "id": self.get_id(),
            "price": self.price,
            "is_vip": self.is_vip,
            "is_booked": self.is_booked,
            "booked_by": self.booked_by
        }

class CinemaHall:
    """Manages the grid of seats and booking logic."""
    def __init__(self):
        self.seats = {} 
        self.load_data()

    def _initialize_fresh_hall(self):
        """Creates a new empty theater grid."""
        logging.info("Initializing new theater layout...")
        self.seats = {}
        row_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        for r in range(CONFIG["ROWS"]):
            r_char = row_letters[r]
            is_vip = r >= CONFIG["VIP_ROW_START"]
            price = CONFIG["PRICE_VIP"] if is_vip else CONFIG["PRICE_STD"]
            
            for c in range(1, CONFIG["COLS"] + 1):
                seat = Seat(r_char, c, price, is_vip)
                self.seats[seat.get_id()] = seat

    def book_seat(self, seat_id, customer_name):
        """Logic to lock a seat."""
        seat_id = seat_id.upper()
        
        if seat_id not in self.seats:
            return False, "Invalid Seat ID."
        
        seat = self.seats[seat_id]
        if seat.is_booked:
            return False, f"Seat {seat_id} is already booked by {seat.booked_by}."
        

        seat.is_booked = True
        seat.booked_by = customer_name
        self.save_data()
        
        logging.info(f"Booking confirmed: {seat_id} for {customer_name}")
        return True, f"Success! Seat {seat_id} booked for ${seat.price}"

    def display_hall(self):
        """Visualizes the seating chart."""
        print("\n" + "="*40)
        print("       [  S C R E E N  ]       ")
        print("="*40)
        
        row_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for r in range(CONFIG["ROWS"]):
            r_char = row_letters[r]
            row_display = ""
            for c in range(1, CONFIG["COLS"] + 1):
                seat_id = f"{r_char}{c}"
                seat = self.seats[seat_id]
                
                if seat.is_booked:
                    symbol = "[ XX ]"
                else:
                    symbol = f"[{seat_id}]" if c < 10 else f"[{seat_id}]"
                
                row_display += symbol + " "

            price = self.seats[f"{r_char}1"].price
            label = "VIP " if self.seats[f"{r_char}1"].is_vip else "STD "
            print(f"{row_display} | {label} ${price}")
        print("="*40 + "\n")

    def save_data(self):
        """Saves current state to JSON."""
        data = {k: v.to_dict() for k, v in self.seats.items()}
        with open(CONFIG["DB_FILE"], 'w') as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        """Loads state from JSON if it exists."""
        if not os.path.exists(CONFIG["DB_FILE"]):
            self._initialize_fresh_hall()
            return

        try:
            with open(CONFIG["DB_FILE"], 'r') as f:
                raw_data = json.load(f)
                self.seats = {}
                for s_id, props in raw_data.items():
                    r_id = s_id[0]
                    c_id = int(s_id[1:])
                    seat = Seat(r_id, c_id, props['price'], props['is_vip'])
                    seat.is_booked = props['is_booked']
                    seat.booked_by = props['booked_by']
                    self.seats[s_id] = seat
            logging.info("Database loaded successfully.")
        except Exception as e:
            logging.error(f"Error loading database: {e}")
            self._initialize_fresh_hall()


class BookingApp:
    def __init__(self):
        self.cinema = CinemaHall()
        if not os.path.exists(CONFIG["TICKET_DIR"]):
            os.makedirs(CONFIG["TICKET_DIR"])

    def generate_ticket(self, name, seat_id):
        """Creates a physical text file receipt."""
        seat = self.cinema.seats[seat_id]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        ticket_content = f"""
        ================================
             CINEMA TICKET RECEIPT
        ================================
        Date:    {timestamp}
        Guest:   {name}
        --------------------------------
        Seat:    {seat_id} ({'VIP' if seat.is_vip else 'Standard'})
        Price:   ${seat.price:.2f}
        --------------------------------
        Status:  PAID
        ================================
        Please show this at the entrance.
        """
        
        filename = f"{CONFIG['TICKET_DIR']}/Ticket_{seat_id}_{name}.txt"
        with open(filename, "w") as f:
            f.write(ticket_content)
        print(f"\n[INFO] Receipt generated: {filename}")

    def run(self):
        while True:
            print("\n--- CINEMA BOOKING SYSTEM ---")
            print("1. View Seating Map")
            print("2. Book a Seat")
            print("3. Reset System (Admin)")
            print("4. Exit")
            
            choice = input("Enter choice: ")
            
            if choice == "1":
                self.cinema.display_hall()
            
            elif choice == "2":
                self.cinema.display_hall()
                s_id = input("Enter Seat Number (e.g., A1): ").strip()
                name = input("Enter Customer Name: ").strip()
                
                success, msg = self.cinema.book_seat(s_id, name)
                print(f"\n>> {msg}")
                
                if success:
                    self.generate_ticket(name, s_id.upper())
            
            elif choice == "3":
                confirm = input("Are you sure you want to clear all bookings? (y/n): ")
                if confirm.lower() == 'y':
                    self.cinema._initialize_fresh_hall()
                    self.cinema.save_data()
                    print("System reset complete.")
            
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid option.")

if __name__ == "__main__":
    app = BookingApp()

    app.run()
