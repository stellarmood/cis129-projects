# Constants for sections
SECTION_A = 'A'
SECTION_B = 'B'
SECTION_C = 'C'

# Constants for ticket prices
PRICE_A = 20
PRICE_B = 15
PRICE_C = 10

# Constants for seat capacities
SEATS_A = 300
SEATS_B = 500
SEATS_C = 200

def get_valid_integer(prompt, max_value):
    """Prompts user for an integer input and validates it."""
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value <= max_value:
                return value
            else:
                print(f"Please enter a value between 0 and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calculate_income(tickets_sold, price_per_ticket):
    """Calculates income from tickets sold based on price per ticket."""
    return tickets_sold * price_per_ticket

def main():
    print("Welcome to the Theater Ticket Sales Program!")
    print(f"Section {SECTION_A}: ${PRICE_A} per seat, {SEATS_A} seats available")
    print(f"Section {SECTION_B}: ${PRICE_B} per seat, {SEATS_B} seats available")
    print(f"Section {SECTION_C}: ${PRICE_C} per seat, {SEATS_C} seats available")
    
    # Get number of tickets sold for each section
    tickets_sold_A = get_valid_integer(f"Enter the number of tickets sold for section {SECTION_A}: ", SEATS_A)
    tickets_sold_B = get_valid_integer(f"Enter the number of tickets sold for section {SECTION_B}: ", SEATS_B)
    tickets_sold_C = get_valid_integer(f"Enter the number of tickets sold for section {SECTION_C}: ", SEATS_C)
    
    # Calculate income for each section
    income_A = calculate_income(tickets_sold_A, PRICE_A)
    income_B = calculate_income(tickets_sold_B, PRICE_B)
    income_C = calculate_income(tickets_sold_C, PRICE_C)
    
    # Calculate subtotals and total
    subtotal_A = income_A
    subtotal_B = subtotal_A + income_B
    subtotal_C = subtotal_B + income_C
    total_income = subtotal_C

    # Display results
    print(f"\nIncome Summary:")
    print(f"Section {SECTION_A}: {tickets_sold_A} tickets sold, ${income_A} generated")
    print(f"Section {SECTION_B}: {tickets_sold_B} tickets sold, ${income_B} generated")
    print(f"Section {SECTION_C}: {tickets_sold_C} tickets sold, ${income_C} generated")
    print(f"Total income: ${total_income}")

if __name__ == "__main__":
    main()
