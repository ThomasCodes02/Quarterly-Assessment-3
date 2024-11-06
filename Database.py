import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('quiz_bowl.db')
cursor = conn.cursor()

# List of course names (tables)
courses = ["Math", "Science", "History", "Literature", "Geography"]

# SQL command template to create each course table
create_table_sql = """
CREATE TABLE IF NOT EXISTS {course} (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    option1 TEXT NOT NULL,
    option2 TEXT NOT NULL,
    option3 TEXT NOT NULL,
    option4 TEXT NOT NULL
);
"""

# Create each table
for course in courses:
    cursor.execute(create_table_sql.format(course=course))

print("Database and tables created successfully.")

# Commit and close the connection
conn.commit()
conn.close()
