import sqlite3

def create_database():
    # Connect Database
    conn = sqlite3.connect('Quiz_Bowl_Database.db')
    cursor = conn.cursor()

    # Create Tables
    create_tables_sql = {
        "DS_3850": """
        CREATE TABLE IF NOT EXISTS DS_3850 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            option1 TEXT NOT NULL,
            option2 TEXT NOT NULL,
            option3 TEXT NOT NULL,
            option4 TEXT NOT NULL
        );
        """,
        "DS_4220": """
        CREATE TABLE IF NOT EXISTS DS_4220 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            option1 TEXT NOT NULL,
            option2 TEXT NOT NULL,
            option3 TEXT NOT NULL,
            option4 TEXT NOT NULL
        );
        """,
        "DS_4210": """
        CREATE TABLE IF NOT EXISTS DS_4210 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            option1 TEXT NOT NULL,
            option2 TEXT NOT NULL,
            option3 TEXT NOT NULL,
            option4 TEXT NOT NULL
        );
        """,
        "MKT_3400": """
        CREATE TABLE IF NOT EXISTS MKT_3400 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            option1 TEXT NOT NULL,
            option2 TEXT NOT NULL,
            option3 TEXT NOT NULL,
            option4 TEXT NOT NULL
        );
        """,
        "HIST_1310": """
        CREATE TABLE IF NOT EXISTS HIST_1310 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            option1 TEXT NOT NULL,
            option2 TEXT NOT NULL,
            option3 TEXT NOT NULL,
            option4 TEXT NOT NULL
        );
        """
    }

    for table_sql in create_tables_sql.values():
        cursor.execute(table_sql)

    print("Tables created successfully.")

    conn.commit()
    conn.close()
    
if __name__ == "__main__":
    create_database()
