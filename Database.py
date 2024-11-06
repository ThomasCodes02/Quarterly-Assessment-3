import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('quiz_bowl.db')
cursor = conn.cursor()

# Create the DS_3850 table for Python basics
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

# Create the DS_4220 table for R basics
create_table_ds4220_sql = """
CREATE TABLE IF NOT EXISTS DS_4220 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    option1 TEXT NOT NULL,
    option2 TEXT NOT NULL,
    option3 TEXT NOT NULL,
    option4 TEXT NOT NULL
);
"""
cursor.execute(create_table_ds4220_sql)

# List of questions for DS 3850 course on Python basics
questions_ds3850 = [
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
for q in questions_ds3850:
    cursor.execute(insert_question_sql, q)

# List of questions for DS 4220 course on R basics
questions_ds4220 = [
    {
        "question": "What is the correct operator for assignment in R?",
        "answer": "<-",
        "option1": "=",
        "option2": "->",
        "option3": ":=",
        "option4": "<-"
    },
    {
        "question": "Which function is used to display the structure of an R object?",
        "answer": "str()",
        "option1": "structure()",
        "option2": "typeof()",
        "option3": "str()",
        "option4": "class()"
    },
    {
        "question": "How do you create a sequence of numbers from 1 to 10 in R?",
        "answer": "1:10",
        "option1": "1..10",
        "option2": "seq(1, 10)",
        "option3": "range(1, 10)",
        "option4": "1:10"
    },
    {
        "question": "What function in R combines elements into a vector?",
        "answer": "c()",
        "option1": "combine()",
        "option2": "c()",
        "option3": "concat()",
        "option4": "vector()"
    },
    {
        "question": "Which function is used to read a CSV file in R?",
        "answer": "read.csv()",
        "option1": "read.csv()",
        "option2": "read.table()",
        "option3": "read()",
        "option4": "csv.read()"
    },
    {
        "question": "How do you get the first six rows of a dataset in R?",
        "answer": "head()",
        "option1": "first()",
        "option2": "head()",
        "option3": "start()",
        "option4": "top()"
    },
    {
        "question": "Which function provides summary statistics in R?",
        "answer": "summary()",
        "option1": "summarize()",
        "option2": "summary()",
        "option3": "describe()",
        "option4": "stats()"
    },
    {
        "question": "How do you create a dataframe in R?",
        "answer": "data.frame()",
        "option1": "data.frame()",
        "option2": "frame()",
        "option3": "data()",
        "option4": "df()"
    },
    {
        "question": "How can you check for missing values in R?",
        "answer": "is.na()",
        "option1": "is.null()",
        "option2": "is.empty()",
        "option3": "is.na()",
        "option4": "missing()"
    },
    {
        "question": "What symbol is used to access elements within a list in R?",
        "answer": "$",
        "option1": "#",
        "option2": "@",
        "option3": "$",
        "option4": "%"
    }
]

# Insert questions into DS_4220 table
insert_question_ds4220_sql = """
INSERT INTO DS_4220 (question, answer, option1, option2, option3, option4)
VALUES (:question, :answer, :option1, :option2, :option3, :option4)
"""
for q in questions_ds4220:
    cursor.execute(insert_question_ds4220_sql, q)

print("DS_3850 and DS_4220 tables with questions inserted successfully.")

# Commit and close the connection
conn.commit()
conn.close()


