import sqlite3

def view_database():
    # Connect to the database
    conn = sqlite3.connect('Quiz_Bowl_Database.db')
    cursor = conn.cursor()

    # Fetch all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    if not tables:
        print("No tables found in the database.")
        conn.close()
        return

    # Print all available tables
    print("Available tables in the database:")
    for idx, table in enumerate(tables, start=1):
        print(f"{idx}. {table[0]}")
    
    # Prompt the user to choose a table
    table_choice = input("Enter the name of the table you want to view data from: ")

    # Validate table name and fetch data
    if (table_choice,) in tables:
        cursor.execute(f"SELECT * FROM {table_choice}")
        rows = cursor.fetchall()

        # Print table data
        if rows:
            print(f"\nData in table '{table_choice}':")
            for row in rows:
                print(row)
        else:
            print(f"The table '{table_choice}' is empty.")
    else:
        print("Invalid table name. Please try again.")

    # Close the database connection
    conn.close()

# Run the function
view_database()