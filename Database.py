import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('quiz_bowl.db')
cursor = conn.cursor()

# Create the DS_3850 table
create_table_ds3850_sql = """
CREATE TABLE IF NOT EXISTS DS_3850 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    option1 TEXT NOT NULL,
    option2 TEXT NOT NULL,
    option3 TEXT NOT NULL,
    option4 TEXT NOT NULL
);
"""

cursor.execute(create_table_ds3850_sql)

# List of questions for DS 3850 course on Python basics
questions = [
    {
        "question": "What is the output of 'print(2 + 3)'?",
        "answer": "5",
        "option1": "23",
        "option2": "5",
        "option3": "Error",
        "option4": "None of the above"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "answer": "def",
        "option1": "function",
        "option2": "define",
        "option3": "def",
        "option4": "func"
    },
    {
        "question": "Which of the following is the correct syntax to print a message in Python?",
        "answer": "print('Hello, World!')",
        "option1": "echo('Hello, World!')",
        "option2": "print 'Hello, World!'",
        "option3": "console.log('Hello, World!')",
        "option4": "print('Hello, World!')"
    },
    {
        "question": "Which symbol is used to start a comment in Python?",
        "answer": "#",
        "option1": "//",
        "option2": "#",
        "option3": "/*",
        "option4": "!"
    },
    {
        "question": "What will be the output of 'print(type(3.14))'?",
        "answer": "<class 'float'>",
        "option1": "<class 'int'>",
        "option2": "<class 'str'>",
        "option3": "<class 'float'>",
        "option4": "<class 'list'>"
    },
    {
        "question": "Which of these is a mutable data type in Python?",
        "answer": "list",
        "option1": "tuple",
        "option2": "string",
        "option3": "list",
        "option4": "int"
    },
    {
        "question": "How do you start a for loop in Python?",
        "answer": "for i in range(10):",
        "option1": "for(i=0; i<10; i++)",
        "option2": "foreach i in range(10)",
        "option3": "for i in range(10):",
        "option4": "for i from 1 to 10"
    },
    {
        "question": "What will be the output of 'print(10 // 3)'?",
        "answer": "3",
        "option1": "3.33",
        "option2": "3",
        "option3": "3.0",
        "option4": "Error"
    },
    {
        "question": "Which function is used to get the length of a list?",
        "answer": "len()",
        "option1": "length()",
        "option2": "count()",
        "option3": "size()",
        "option4": "len()"
    },
    {
        "question": "What is the correct file extension for Python files?",
        "answer": ".py",
        "option1": ".python",
        "option2": ".py",
        "option3": ".pyt",
        "option4": ".pt"
    }
]

# Insert questions into DS_3850 table
insert_question_sql = """
INSERT INTO DS_3850 (question, answer, option1, option2, option3, option4)
VALUES (:question, :answer, :option1, :option2, :option3, :option4)
"""

for q in questions:
    cursor.execute(insert_question_sql, q)

print("DS_3850 table and questions inserted successfully.")

# Commit and close the connection
conn.commit()
conn.close()

