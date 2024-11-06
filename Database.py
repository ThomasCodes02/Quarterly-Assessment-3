import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('quiz_bowl.db')
cursor = conn.cursor()

# Create tables
# DS 3850 - Python Basics
cursor.execute("""
CREATE TABLE IF NOT EXISTS DS_3850 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    option1 TEXT NOT NULL,
    option2 TEXT NOT NULL,
    option3 TEXT NOT NULL,
    option4 TEXT NOT NULL
);
""")

# DS 4220 - R Basics
cursor.execute("""
CREATE TABLE IF NOT EXISTS DS_4220 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    option1 TEXT NOT NULL,
    option2 TEXT NOT NULL,
    option3 TEXT NOT NULL,
    option4 TEXT NOT NULL
);
""")

# DS 4210 - Business Intelligence Basics
cursor.execute("""
CREATE TABLE IF NOT EXISTS DS_4210 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    option1 TEXT NOT NULL,
    option2 TEXT NOT NULL,
    option3 TEXT NOT NULL,
    option4 TEXT NOT NULL
);
""")

# MKT 3400 - Marketing Basics
cursor.execute("""
CREATE TABLE IF NOT EXISTS MKT_3400 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    option1 TEXT NOT NULL,
    option2 TEXT NOT NULL,
    option3 TEXT NOT NULL,
    option4 TEXT NOT NULL
);
""")

# Insert questions
# DS 3850 - Python Basics Questions
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

# DS 4220 - R Basics Questions
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

# DS 4210 - Business Intelligence Basics Questions
questions_ds4210 = [
    {
        "question": "What is the primary purpose of Business Intelligence (BI)?",
        "answer": "To support decision-making",
        "option1": "To store large volumes of data",
        "option2": "To support decision-making",
        "option3": "To manage employees",
        "option4": "To create advertising campaigns"
    },
    {
        "question": "Which of the following is a commonly used BI tool?",
        "answer": "Tableau",
        "option1": "Photoshop",
        "option2": "Excel",
        "option3": "Tableau",
        "option4": "Notepad"
    },
    {
        "question": "What does ETL stand for in the context of BI?",
        "answer": "Extract, Transform, Load",
        "option1": "Extract, Transfer, Load",
        "option2": "Extract, Transform, Load",
        "option3": "Evaluate, Test, Learn",
        "option4": "Encrypt, Transform, Load"
    },
    {
        "question": "Which type of analytics focuses on historical data to explain what happened?",
        "answer": "Descriptive Analytics",
        "option1": "Predictive Analytics",
        "option2": "Descriptive Analytics",
        "option3": "Prescriptive Analytics",
        "option4": "Cognitive Analytics"
    },
    {
        "question": "What is a data warehouse?",
        "answer": "A centralized storage for data",
        "option1": "A physical room for storing documents",
        "option2": "A system for cloud storage",
        "option3": "A centralized storage for data",
        "option4": "A tool for data visualization"
    },
    {
        "question": "Which tool is commonly used for data visualization in BI?",
        "answer": "Power BI",
        "option1": "MS Word",
        "option2": "Power BI",
        "option3": "Notepad",
        "option4": "Adobe Acrobat"
    },
    {
        "question": "What is data mining?",
        "answer": "The process of discovering patterns in large datasets",
        "option1": "The process of storing data",
        "option2": "The process of retrieving data",
        "option3": "The process of discovering patterns in large datasets",
        "option4": "The process of deleting redundant data"
    },
    {
        "question": "Which of these is an example of predictive analytics?",
        "answer": "Forecasting future sales",
        "option1": "Visualizing past trends",
        "option2": "Generating reports",
        "option3": "Forecasting future sales",
        "option4": "Describing past events"
    },
    {
        "question": "What is the main purpose of a KPI in BI?",
        "answer": "To measure performance",
        "option1": "To increase revenue",
        "option2": "To measure performance",
        "option3": "To analyze competition",
        "option4": "To hire employees"
    },
    {
        "question": "Which of these is a BI technique used to clean and structure raw data?",
        "answer": "Data preprocessing",
        "option1": "Data sampling",
        "option2": "Data visualization",
        "option3": "Data preprocessing",
        "option4": "Data modeling"
    }
]

# MKT 3400 - Marketing Basics Questions
questions_mkt3400 = [
    {
        "question": "What is the '4 Ps' concept in marketing?",
        "answer": "Product, Price, Place, Promotion",
        "option1": "Product, Price, Place, Promotion",
        "option2": "People, Process, Product, Place",
        "option3": "Product, Price, People, Place",
        "option4": "Process, Product, Price, Promotion"
    },
    {
        "question": "Which of these is an example of a marketing strategy?",
        "answer": "Social media advertising",
        "option1": "Hiring employees",
        "option2": "Inventory management",
        "option3": "Social media advertising",
        "option4": "Product assembly"
    },
    {
        "question": "What does SWOT stand for in marketing?",
        "answer": "Strengths, Weaknesses, Opportunities, Threats",
        "option1": "Strengths, Weaknesses, Opportunities, Threats",
        "option2": "Sales, Worth, Operations, Team",
        "option3": "Services, Work, Objectives, Targets",
        "option4": "Solutions, Workforce, Opportunities, Trends"
    },
    {
        "question": "What is market segmentation?",
        "answer": "Dividing a market into distinct groups of buyers",
        "option1": "Setting a market price",
        "option2": "Dividing a market into distinct groups of buyers",
        "option3": "Increasing brand loyalty",
        "option4": "Improving customer satisfaction"
    },
    {
        "question": "Which of the following is a type of consumer market?",
        "answer": "Personal consumption",
        "option1": "Wholesale",
        "option2": "Personal consumption",
        "option3": "B2B transactions",
        "option4": "Real estate investment"
    },
    {
        "question": "What is brand positioning?",
        "answer": "Establishing a brand's identity in the market",
        "option1": "Selling the product",
        "option2": "Determining the price",
        "option3": "Establishing a brand's identity in the market",
        "option4": "Selecting target markets"
    },
    {
        "question": "Which is an example of a pricing strategy?",
        "answer": "Penetration pricing",
        "option1": "Product placement",
        "option2": "Penetration pricing",
        "option3": "Market segmentation",
        "option4": "Supply chain management"
    },
    {
        "question": "What does CRM stand for?",
        "answer": "Customer Relationship Management",
        "option1": "Customer Retention Management",
        "option2": "Customer Relationship Marketing",
        "option3": "Customer Relationship Management",
        "option4": "Client Retention Marketing"
    },
    {
        "question": "What is the purpose of a target market?",
        "answer": "To focus marketing efforts on a specific group",
        "option1": "To increase product prices",
        "option2": "To establish production goals",
        "option3": "To focus marketing efforts on a specific group",
        "option4": "To hire sales staff"
    },
    {
        "question": "What is product life cycle?",
        "answer": "Stages a product goes through from introduction to decline",
        "option1": "Product manufacturing process",
        "option2": "Stages a product goes through from introduction to decline",
        "option3": "Product branding process",
        "option4": "Product segmentation technique"
    }
]

# SQL Template for Inserting Questions
insert_question_sql_template = """
INSERT INTO {table} (question, answer, option1, option2, option3, option4)
VALUES (:question, :answer, :option1, :option2, :option3, :option4)
"""

# Insert Questions for Each Course
for table_name, questions in {
    "DS_3850": questions_ds3850,
    "DS_4220": questions_ds4220,
    "DS_4210": questions_ds4210,
    "MKT_3400": questions_mkt3400
}.items():
    insert_question_sql = insert_question_sql_template.format(table=table_name)
    for question in questions:
        cursor.execute(insert_question_sql, question)

print("All tables created and questions inserted successfully.")

# Commit and close the connection
conn.commit()
conn.close()




