from datetime import datetime, timedelta

def display_current_datetime():
  
    current_date = datetime.now()
    formatted_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_current_date}")

def calculate_future_date():
  
    while True:
        try:
            days_to_add_str = input("Enter the number of days to add to the current date: ")
            days_to_add = int(days_to_add_str)
            break # Exit loop if input is valid
        except ValueError:
            print("Invalid input. Please enter an integer for the number of days.")

    current_datetime_for_future_calc = datetime.now()

    future_date = current_datetime_for_future_calc + timedelta(days=days_to_add)

    formatted_future_date = future_date.strftime("%Y-%m-%d")

    # Print the future date
    print(f"Future date: {formatted_future_date}")

# --- Main execution block ---
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()